#!/usr/bin/env python3
"""New BC map features, drawn as new metatiles in a town's secondary tileset and placed on its map:

- RICHMOND: a Steveston salmon cannery on pilings at the shore of the north-east pond (red
  board-and-batten walls, white trim, grey roof), as the Gulf of Georgia Cannery stands on the river.
- COQUIHALLA (Route 111): sagebrush shrubs replace the pebbles on the badland sands.
- VICTORIA: arbutus trees (peeling red bark, glossy crowns) on the grass by the shore.

The pebble and grass metatiles live in the shared general tileset, so each feature gets its own
metatiles in the map's secondary tileset (the free tiles past the animated ones) and only that
map's cells change. Everything starts from upstream (needs the pret `upstream` remote), so the script
is idempotent. Run from the repo root: python3 atlas/bc_tiles.py [--preview out.png]
"""
import io
import math
import os
import struct
import subprocess
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
COVERED = 1  # metatile layer type: both layers under sprites (layer 0 bottom, layer 1 middle)


def git_show(rel):
    return subprocess.run(['git', 'show', 'upstream/master:' + rel], cwd=ROOT, capture_output=True, check=True).stdout


GENERAL = Image.open(io.BytesIO(git_show('data/tilesets/primary/general/tiles.png'))).load()
GENERAL_META = git_show('data/tilesets/primary/general/metatiles.bin')


def general_tile(tid, hf=0, vf=0):
    return [[GENERAL[(tid % 16) * 8 + (7 - x if hf else x), (tid // 16) * 8 + (7 - y if vf else y)] for x in range(8)] for y in range(8)]


def general_entries(mid):
    return list(struct.unpack('<8H', GENERAL_META[mid * 16:mid * 16 + 16]))


class Tileset:
    """A secondary tileset rebuilt from upstream; new tiles go into blank, unreferenced slots."""

    def __init__(self, name, reserved=()):
        self.rel = 'data/tilesets/secondary/%s/' % name
        self.img = Image.open(io.BytesIO(git_show(self.rel + 'tiles.png')))
        self.px = self.img.load()
        self.meta = bytearray(git_show(self.rel + 'metatiles.bin'))
        self.attr = bytearray(git_show(self.rel + 'metatile_attributes.bin'))
        tw, n = self.img.width // 8, (self.img.width // 8) * (self.img.height // 8)
        used = {(v & 0x3ff) - 0x200 for v in struct.unpack('<%dH' % (len(self.meta) // 2), self.meta) if v & 0x3ff >= 0x200}
        blank = lambda t: all(self.px[(t % tw) * 8 + x, (t // tw) * 8 + y] == 0 for x in range(8) for y in range(8))
        self.free = [t for t in range(1, n) if t not in used and t not in reserved and blank(t)]
        self.made = {}

    def tile(self, cell, pal):
        """Tilemap entry for an 8x8 cell of palette indices (0 = see-through), reusing flipped copies."""
        if not any(any(r) for r in cell):
            return 0
        for hf in (0, 1):
            for vf in (0, 1):
                key = tuple(tuple((cell[7 - y if vf else y][7 - x if hf else x]) for x in range(8)) for y in range(8))
                if key in self.made:
                    return self.made[key] | hf << 10 | vf << 11 | pal << 12
        assert self.free, self.rel + ': out of free tiles'
        t = self.free.pop(0)
        tw = self.img.width // 8
        for y in range(8):
            for x in range(8):
                self.px[(t % tw) * 8 + x, (t // tw) * 8 + y] = cell[y][x]
        self.made[tuple(map(tuple, cell))] = 0x200 + t
        return 0x200 + t | pal << 12

    def metatile(self, entries, attr):
        mid = 0x200 + len(self.meta) // 16
        assert mid < 0x3ff, self.rel + ': out of metatiles'
        self.meta += struct.pack('<8H', *entries)
        self.attr += struct.pack('<H', attr)
        return mid

    def block(self, art, pal, under, attr):
        """Metatiles for art (rows of palette indices, a multiple of 16 each way) drawn on layer 1 over
        the layer-0 entries `under` (a function of the metatile's column and row). Returns rows of ids."""
        ids = []
        for my in range(len(art) // 16):
            row = []
            for mx in range(len(art[0]) // 16):
                top = [self.tile([[art[my * 16 + ty * 8 + y][mx * 16 + tx * 8 + x] for x in range(8)] for y in range(8)], pal)
                       for ty in (0, 1) for tx in (0, 1)]
                row.append(self.metatile(under(mx, my) + top, attr))
            ids.append(row)
        return ids

    def save(self):
        self.img.save(P(self.rel, 'tiles.png'))
        open(P(self.rel, 'metatiles.bin'), 'wb').write(self.meta)
        open(P(self.rel, 'metatile_attributes.bin'), 'wb').write(self.attr)


class Layout:
    def __init__(self, name):
        self.rel = 'data/layouts/%s/map.bin' % name
        self.w = next(l['width'] for l in __import__('json').load(open(P('data/layouts/layouts.json')))['layouts']
                      if l.get('blockdata_filepath') == self.rel)
        self.cells = list(struct.unpack('<%dH' % (len(git_show(self.rel)) // 2), git_show(self.rel)))

    def get(self, x, y):
        return self.cells[y * self.w + x]

    def put(self, x, y, mid, collision=None):
        v = self.cells[y * self.w + x]
        if collision is not None:
            v = v & ~0xc00 | collision << 10
        self.cells[y * self.w + x] = v & ~0x3ff | mid

    def save(self):
        open(P(self.rel), 'wb').write(struct.pack('<%dH' % len(self.cells), *self.cells))


def canvas(w, h):
    return [[0] * w for _ in range(h)]


def noise(x, y, k=0):
    """Deterministic 0..1 hash noise, so the art is the same on every run."""
    n = (x * 374761393 + y * 668265263 + k * 2147483647) & 0xffffffff
    n = (n ^ (n >> 13)) * 1274126177 & 0xffffffff
    return (n ^ (n >> 16)) / 0xffffffff


def clumps(c, blobs, shades, k):
    """Fill overlapping round clumps, lit from the top left: shades = (highlight, light, mid, dark)."""
    hi, light, mid, dark = shades
    h, w = len(c), len(c[0])
    for y in range(h):
        for x in range(w):
            best = None
            for (cx, cy, r) in blobs:
                d = math.hypot(x + 0.5 - cx, y + 0.5 - cy)
                if d <= r and (best is None or cy > best[1]):  # lower clumps sit in front
                    best = (cx, cy, r)
            if not best:
                continue
            cx, cy, r = best
            lit = ((cx - x - 0.5) + (cy - y - 0.5)) / r + (noise(x, y, k) - 0.5) * 0.7
            if math.hypot(x + 0.5 - cx, y + 0.5 - cy) > r - 1 and (x + 0.5 > cx or y + 0.5 > cy):
                v = dark
            elif lit > 0.75:
                v = hi
            elif lit > 0.1:
                v = light
            elif lit > -0.6:
                v = mid
            else:
                v = dark
            c[y][x] = v


# ---- RICHMOND cannery (petalburg tileset, primary palette 1) ------------------------------------
# Palette 1: 1 white, 2-7 light to dark greys, 8 navy outline, 9/10 water blues, 11-14 reds.
def cannery():
    W, H = 64, 48
    c = canvas(W, H)
    # Roof (side gable, ridge running left-right): ridge rows 1-2, slope to the eaves at row 15.
    for y in range(1, 16):
        inset = max(0, 3 - y // 4)
        for x in range(1 + inset, W - 1 - inset):
            if y == 1 or x in (1 + inset, W - 2 - inset):
                v = 8
            elif y == 2:
                v = 3
            elif y >= 14:
                v = 7 if y == 15 else 6
            else:
                v = 6 if x % 4 == 0 else (4 if y < 6 else 5)
            c[y][x] = v
    # Roof vent / cupola at the ridge centre.
    for y in range(0, 4):
        for x in range(28, 36):
            c[y][x] = 8 if y == 0 or x in (28, 35) else (2 if y == 1 else 5)
    # Walls: red board and batten, white trim boards at the corners and under the eaves.
    for y in range(16, 37):
        for x in range(2, W - 2):
            if y == 16:
                v = 1
            elif x in (2, 3, W - 4, W - 3):
                v = 1 if x in (3, W - 4) else 8
            else:
                v = 14 if x % 4 == 1 else 13
            c[y][x] = v
    # A row of small white-framed windows.
    for wx in (6, 13, 20, 39, 46, 53):
        for y in range(19, 25):
            for x in range(wx, wx + 5):
                c[y][x] = 1 if y in (19, 24) or x in (wx, wx + 4) else (9 if y < 22 else 10)
    # Wide loading door in the middle, white frame, dark planks.
    for y in range(22, 37):
        for x in range(26, 38):
            if y == 22 or x in (26, 37):
                v = 1
            else:
                v = 7 if x % 3 else 8
            c[y][x] = v
    # Wharf deck edge.
    for y in (37, 38):
        for x in range(0, W):
            c[y][x] = 8 if y == 38 else 4
    # Pilings into the water, with a light edge.
    for px_ in range(2, W, 6):
        for y in range(39, 47):
            c[y][px_] = 5
            c[y][px_ + 1] = 8
    return c


# ---- COQUIHALLA sagebrush (mauville tileset, primary palette 3) ---------------------------------
# Palette 3: 2/3/4/5 silver to mid greys, 7 sage green, 8 dark outline, 13/14 browns.
def sagebrush():
    c = canvas(16, 16)
    blobs = [(5.0, 9.0, 3.6), (11.0, 9.0, 3.6), (8.0, 6.0, 4.0), (8.0, 10.5, 3.6), (3.5, 11.5, 2.4), (12.5, 11.5, 2.4)]
    clumps(c, blobs, (7, 7, 4, 5), 3)
    for y in range(16):  # ragged, feathery edges and silver flecks
        for x in range(16):
            if not c[y][x]:
                continue
            edge = any(not (0 <= x + dx < 16 and 0 <= y + dy < 16 and c[y + dy][x + dx]) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            if edge and noise(x, y, 11) > 0.55 and y < 12:
                c[y][x] = 0
            elif not edge and noise(x, y, 12) > 0.86:
                c[y][x] = 2
            elif not edge and noise(x, y, 13) > 0.85:
                c[y][x] = 5
    for y in range(len(c)):  # a darker rim along the bottom of the shrub
        for x in range(16):
            if c[y][x] and (y + 1 == 16 or not c[y + 1][x]):
                c[y][x] = 8
    for (x, y) in ((6, 14), (7, 14), (9, 14), (10, 13), (5, 13)):  # woody stems
        if not c[y][x]:
            c[y][x] = 14
    return c


def sand_with_shadow():
    """Layer 0 for the shrub: the pebble's sand tiles (palette 5) with a soft shadow under it."""
    e = general_entries(0x0e2)[:4]
    cells = []
    for k, v in enumerate(e):
        cell = general_tile(v & 0x3ff, v >> 10 & 1, v >> 11 & 1)
        ox, oy = (k % 2) * 8, (k // 2) * 8
        for y in range(8):
            for x in range(8):
                if ((ox + x + 0.5 - 8) / 6.5) ** 2 + ((oy + y + 0.5 - 13.5) / 2.2) ** 2 <= 1:
                    cell[y][x] = 14
        cells.append(cell)
    return cells


# ---- VICTORIA arbutus (slateport tileset, primary palette 2) ------------------------------------
# Palette 2: 1-4 leaf greens light to dark, 5/9 peach, 7/10 red-brown bark, 8 dark brown.
def arbutus():
    c = canvas(32, 32)
    # Trunk: two leaning stems from one base, splitting into branches; cinnamon bark, peach where peeled.
    stems = [((15.5, 31.0), (15.0, 26.0), (12.5, 20.0), (8.0, 13.0)), ((16.0, 27.0), (19.5, 20.0), (23.0, 12.0)),
             ((14.0, 21.0), (15.5, 15.0), (14.5, 7.0)), ((12.0, 18.5), (6.0, 17.0))]
    for path in stems:
        for (x0, y0), (x1, y1) in zip(path, path[1:]):
            steps = int(max(abs(x1 - x0), abs(y1 - y0)) * 2) + 1
            for i in range(steps + 1):
                t = i / steps
                x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
                width = 2.6 if y > 25 else (2.0 if y > 18 else 1.4)
                for dx in range(-2, 3):
                    xi, yi = int(x + dx), int(y)
                    if abs(x + dx - x) <= width and 0 <= xi < 32 and 0 <= yi < 32:
                        side = (xi + 0.5) - x
                        c[yi][xi] = 8 if abs(side) > width - 0.6 else (9 if side < -0.3 and noise(xi, yi, 9) > 0.4 else (10 if side < 0.5 else 7))
    # Crown: broad, uneven clumps with gaps so the red limbs show.
    crown = canvas(32, 32)
    blobs = [(7.0, 9.0, 5.0), (4.0, 13.5, 3.5), (10.5, 12.0, 3.5), (15.0, 5.0, 5.0), (22.5, 8.0, 5.5), (27.0, 13.0, 3.5),
             (19.5, 12.5, 3.5)]
    clumps(crown, blobs, (1, 2, 3, 4), 5)
    for y in range(32):
        for x in range(32):
            gap = noise(x // 3, y // 3, 7) > 0.86 and 6 < y < 17
            if crown[y][x] and not gap:
                c[y][x] = crown[y][x]
    for y in range(25, 32):  # base flare and a dark root line on the grass
        for x in range(12, 21):
            if c[y][x] == 0 and y == 31 and 12 < x < 20:
                c[y][x] = 8
    return c


def preview(path, items):
    """Preview images: (art, palette file) pairs side by side at 4x."""
    out = Image.new('RGB', (sum(len(a[0]) * 4 + 8 for a, _ in items), 48 * 4), (90, 140, 200))
    x0 = 0
    for art, palf in items:
        pal = [tuple(map(int, l.split())) for l in open(P(palf)).read().replace('\r', '').split('\n')[3:19]]
        for y, row in enumerate(art):
            for x, v in enumerate(row):
                if v:
                    for dy in range(4):
                        for dx in range(4):
                            out.putpixel((x0 + x * 4 + dx, y * 4 + dy), pal[v])
        x0 += len(art[0]) * 4 + 8
    out.save(path)


def main():
    # RICHMOND: cannery against the south shore of the north-east pond (x 21-24, y 6-8). The pond's
    # west columns (x 19-20) stay open water, so the item ball on its north bank is still reachable.
    pet = Tileset('petalburg')
    water = general_entries(0x0a1)[:4]
    ids = pet.block(cannery(), 1, lambda mx, my: water, COVERED << 12)
    town = Layout('PetalburgCity')
    for my, row in enumerate(ids):
        for mx, mid in enumerate(row):
            assert town.get(21 + mx, 6 + my) & 0x3ff == 0x0a1, 'RICHMOND pond moved'
            town.put(21 + mx, 6 + my, mid, collision=1)
    pet.save()
    town.save()

    # COQUIHALLA: every sand pebble on the route becomes a sagebrush. Mauville animates its tiles
    # 96-159 (flowers), so those slots are never used.
    mau = Tileset('mauville', reserved=range(96, 160))
    shadow = [mau.tile(cell, 5) for cell in sand_with_shadow()]
    sage = mau.block(sagebrush(), 3, lambda mx, my: shadow, general_entries_attr(0x0e2))[0][0]
    n = 0
    for name in ('Route111', 'Route111_NoMirageTower'):
        route = Layout(name)
        for i, v in enumerate(route.cells):
            if v & 0x3ff == 0x0e2:
                route.cells[i] = v & ~0x3ff | sage
                n += 1
        route.save()
    mau.save()

    # VICTORIA: arbutus on the shore grass. Slateport animates tiles 224-227 (balloons).
    sla = Tileset('slateport', reserved=range(224, 228))
    grass = general_entries(0x001)[:4]
    tree = sla.block(arbutus(), 2, lambda mx, my: grass, COVERED << 12)
    city = Layout('SlateportCity')
    for (x, y) in ARBUTUS:
        for my in (0, 1):
            for mx in (0, 1):
                assert city.get(x + mx, y + my) & 0x3ff == 0x001, 'VICTORIA grass at %d,%d moved' % (x + mx, y + my)
                city.put(x + mx, y + my, tree[my][mx], collision=1)
    sla.save()
    city.save()

    if '--preview' in sys.argv:
        preview(sys.argv[sys.argv.index('--preview') + 1],
                [(cannery(), 'data/tilesets/primary/general/palettes/01.pal'),
                 (sagebrush(), 'data/tilesets/primary/general/palettes/03.pal'),
                 (arbutus(), 'data/tilesets/primary/general/palettes/02.pal')])
    print('bc tiles: RICHMOND cannery, %d sagebrush on the COQUIHALLA, %d arbutus in VICTORIA' % (n, len(ARBUTUS)))


def general_entries_attr(mid):
    a = git_show('data/tilesets/primary/general/metatile_attributes.bin')
    return struct.unpack('<H', a[mid * 2:mid * 2 + 2])[0]


# Top-left cells of the 2x2 arbutus trees in VICTORIA (grass, off every path and event).
ARBUTUS = [(36, 14), (32, 14), (20, 21), (20, 32), (2, 29)]

main()
