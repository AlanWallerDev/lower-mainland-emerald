#!/usr/bin/env python3
"""Battle intros for the story legendaries, drawn as glowing BC line art in the style of the
originals (graphics/battle_transitions/groudon.*, kyogre.*):

- GROUDON slot (spirit bear): a bear paw print inside a ring.
- KYOGRE slot (glass sponge reef): the lattice skeleton of a vase-shaped glass sponge.

These intros light the picture by palette cycling: each palette row moves a bright band along the
colour indices. Line pixels take an index that steps with distance from the centre, so the light
pulses outward through the lines. Index 15 is the black background. The tileset is written like
upstream's (greyscale PNG, grey = index * 17) and the tilemap keeps each cell's palette bits.

Starts from upstream for the cell palette bits (needs the pret `upstream` remote); idempotent.
Run from the repo root: python3 atlas/make_transitions.py [--preview out.png]
"""
import io
import math
import os
import struct
import subprocess
import sys

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REL = 'graphics/battle_transitions/'
SS = 4
BG = 15
CX, CY = 120, 80
MAX_TILES = 600  # BG0 char base 2 up to screen base 26 holds 640 tiles


def git_show(path):
    return subprocess.run(['git', 'show', 'upstream/master:' + path], cwd=ROOT, capture_output=True, check=True).stdout


def s(pts):
    return [(x * SS, y * SS) for x, y in pts]


def paw(mask, w):
    """Spirit bear: paw print (palm pad, four toes, claws) inside a ring."""
    d = ImageDraw.Draw(mask)
    d.ellipse(s([(80, 80), (160, 140)]), outline=255, width=w)
    for (x, y) in ((74, 60), (100, 40), (140, 40), (166, 60)):
        d.ellipse(s([(x - 12, y - 15), (x + 12, y + 15)]), outline=255, width=w)
        ang = math.atan2(y - 110, x - CX)
        x1, y1 = x + 16 * math.cos(ang), y + 19 * math.sin(ang)
        d.line(s([(x1, y1), (x1 + 9 * math.cos(ang), y1 + 9 * math.sin(ang))]), fill=255, width=w)
    d.ellipse(s([(CX - 104, CY - 78), (CX + 104, CY + 78)]), outline=255, width=w)


def sponge(mask, w):
    """Glass sponge reef: a vase of fused silica lattice, square grid inside a flared outline."""
    d = ImageDraw.Draw(mask)
    outline = [(58, 14), (182, 14), (166, 70), (156, 150), (84, 150), (74, 70)]
    d.polygon(s(outline), outline=255, width=w)
    grid = Image.new('L', (240 * SS, 160 * SS), 0)
    g = ImageDraw.Draw(grid)
    for x in range(58, 190, 14):
        g.line(s([(x, 14), (x, 150)]), fill=255, width=w)
    for y in range(28, 150, 14):
        g.line(s([(50, y), (190, y)]), fill=255, width=w)
    for k in range(-160, 240, 28):  # the diagonal struts that brace the real lattice
        g.line(s([(k, 150), (k + 136, 14)]), fill=255, width=max(1, w // 2))
    inside = Image.new('L', grid.size, 0)
    ImageDraw.Draw(inside).polygon(s(outline), fill=255)
    mask.paste(255, (0, 0), Image.composite(grid, Image.new('L', grid.size, 0), inside))
    # Rubble mounds of the reef at the foot.
    d.arc(s([(10, 130), (90, 190)]), 180, 360, fill=255, width=w)
    d.arc(s([(150, 130), (230, 190)]), 180, 360, fill=255, width=w)


def build(name, draw, lo, n):
    """Draw, colour by distance bands (indices lo .. lo+n-1), tile and write name.png/.bin."""
    mask = Image.new('L', (240 * SS, 160 * SS), 0)
    draw(mask, 3 * SS)
    mask = mask.resize((240, 160), Image.LANCZOS).load()
    img = [[BG] * 256 for _ in range(256)]
    for y in range(160):
        for x in range(240):
            if mask[x, y] >= 110:
                # Constant within a tile keeps the tile count down; bands step outward.
                tx, ty = x // 8 * 8 + 4, y // 8 * 8 + 4
                band = int(math.hypot(tx - CX, (ty - CY) * 1.3) / 9)
                img[y][x] = lo + band % n
    cells = [struct.unpack('<H', git_show(REL + name + '.bin')[i * 2:i * 2 + 2])[0] for i in range(1024)]

    def tile(i):
        cx, cy = (i % 32) * 8, (i // 32) * 8
        return tuple(img[cy + y][cx + x] for y in range(8) for x in range(8))

    def flips(t):
        rows = [t[r * 8:r * 8 + 8] for r in range(8)]
        return [(t, 0, 0), (tuple(p for r in rows for p in reversed(r)), 1, 0),
                (tuple(p for r in reversed(rows) for p in r), 0, 1),
                (tuple(p for r in reversed(rows) for p in reversed(r)), 1, 1)]

    tiles, index, out = [], {}, []
    for i, v in enumerate(cells):
        t = tile(i)
        hit = next(((index[f], hf, vf) for f, hf, vf in flips(t) if f in index), None)
        if hit is None:
            index[t] = len(tiles)
            tiles.append(t)
            hit = (index[t], 0, 0)
        out.append(hit[0] | hit[1] << 10 | hit[2] << 11 | (v & 0xf000))
    if len(tiles) > MAX_TILES:
        sys.exit('make_transitions: %s needs %d tiles (max %d)' % (name, len(tiles), MAX_TILES))
    rows = (len(tiles) + 7) // 8
    sheet = Image.new('L', (64, rows * 8), BG * 17)
    sp = sheet.load()
    for k, t in enumerate(tiles):
        for j, p in enumerate(t):
            sp[(k % 8) * 8 + j % 8, (k // 8) * 8 + j // 8] = p * 17
    sheet.save(os.path.join(ROOT, REL, name + '.png'))
    with open(os.path.join(ROOT, REL, name + '.bin'), 'wb') as f:
        f.write(b''.join(struct.pack('<H', v) for v in out))
    print('transition %s: %d tiles' % (name, len(tiles)))
    return img


def preview(img, pal, path):
    v = open(os.path.join(ROOT, REL, pal)).read().split()[3:]
    cols = [tuple(map(int, v[i * 3:i * 3 + 3])) for i in range(16)]
    im = Image.new('RGB', (240, 160))
    for y in range(160):
        for x in range(240):
            im.putpixel((x, y), cols[img[y][x]])
    im.resize((480, 320), Image.NEAREST).save(path)


def rehue(name, fn):
    """Rewrite an upstream intro palette with each colour's brightness kept and its hue changed."""
    v = git_show(REL + name).decode().split()
    head, nums = v[:3], v[3:]
    out = []
    for i in range(0, len(nums), 3):
        r, g, b = map(int, nums[i:i + 3])
        out.append('%d %d %d' % fn(max(r, g, b)))
    with open(os.path.join(ROOT, REL, name), 'w', newline='\r\n') as f:
        f.write('\n'.join(head + out) + '\n')


# The bear glows amber (drought and fire), the reef cyan (the sea); upstream had blue and red.
for part in ('pt1', 'pt2'):
    rehue('groudon_%s.pal' % part, lambda m: (m, m * 7 // 10, m // 5))
    rehue('kyogre_%s.pal' % part, lambda m: (m // 6, m * 9 // 10, m))

g = build('groudon', paw, 2, 10)
k = build('kyogre', sponge, 4, 11)
if '--preview' in sys.argv:
    base = sys.argv[sys.argv.index('--preview') + 1]
    preview(g, 'groudon_pt1.pal', base.replace('.png', '_bear.png'))
    preview(k, 'kyogre_pt1.pal', base.replace('.png', '_reef.png'))
