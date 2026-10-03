#!/usr/bin/env python3
"""Stand-in sprites for every organism: front, animated front, back, icon, footprint and palettes.

Shapes come from the Living Atlas body family (quadruped, flier, swimmer, ...); colors from the
organism's types. Run from the repo root: python3 atlas/make_sprites.py
"""
import colorsys
import json
import os
import re
import zlib

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)


def read(p):
    with open(P(p), encoding='utf-8') as f:
        return f.read()


def write(p, s):
    with open(P(p), 'w', encoding='utf-8') as f:
        f.write(s)


species = {s['id']: s for s in json.load(open(P('atlas', 'data', 'species.json'), encoding='utf-8'))}
fills = {t['name']: t['fill'] for t in json.load(open(P('atlas', 'data', 'types.json'), encoding='utf-8'))['types']}
smap = json.load(open(P('atlas', 'species_map.json'), encoding='utf-8'))

BG = (152, 208, 160)  # transparent index 0
TRANSPARENT, OUTLINE, BASE, SHADE, LIGHT, ALT, ALT_SHADE, ALT_LIGHT, WHITE, BLACK, ACCENT = range(11)


def hexrgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def shade(rgb, f):
    h, l, s = colorsys.rgb_to_hls(*[c / 255 for c in rgb])
    l = max(0, min(1, l * f if f < 1 else l + (1 - l) * (f - 1)))
    return tuple(int(round(c * 255)) for c in colorsys.hls_to_rgb(h, l, s))


def hue(rgb, d):
    h, l, s = colorsys.rgb_to_hls(*[c / 255 for c in rgb])
    return tuple(int(round(c * 255)) for c in colorsys.hls_to_rgb((h + d) % 1, l, s))


def palette_for(s, shiny=False):
    a = hexrgb(fills[s['types'][0]])
    b = hexrgb(fills[s['types'][1]]) if len(s['types']) > 1 else shade(a, 1.45)
    if a == b:
        b = shade(a, 1.45)
    if shiny:
        a, b = hue(a, 0.33), hue(b, 0.33)
    pal = [BG, shade(a, 0.35), a, shade(a, 0.7), shade(a, 1.35), b, shade(b, 0.7), shade(b, 1.35),
           (248, 248, 248), (24, 24, 32), (232, 96, 88)]
    pal += [(0, 0, 0)] * (16 - len(pal))
    return pal


def rnd(seed):
    """Small deterministic PRNG so every build makes the same art."""
    x = zlib.crc32(seed.encode()) or 1
    while True:
        x ^= (x << 13) & 0xffffffff
        x ^= x >> 17
        x ^= (x << 5) & 0xffffffff
        yield (x & 0xffff) / 0xffff


class Canvas:
    """Draws body parts as masks at 2x, then downsamples, shades and outlines."""

    def __init__(self):
        self.body = Image.new('L', (128, 128), 0)
        self.alt = Image.new('L', (128, 128), 0)
        self.acc = Image.new('L', (128, 128), 0)
        self.eyes = []
        self.d = ImageDraw.Draw(self.body)
        self.da = ImageDraw.Draw(self.alt)
        self.dc = ImageDraw.Draw(self.acc)

    @staticmethod
    def _s(pts):
        return [v * 2 for v in pts]

    def ell(self, x0, y0, x1, y1, layer='body'):
        self._draw(layer).ellipse(self._s([x0, y0, x1, y1]), fill=255)

    def poly(self, pts, layer='body'):
        self._draw(layer).polygon(self._s([c for p in pts for c in p]), fill=255)

    def line(self, pts, w, layer='body'):
        self._draw(layer).line(self._s([c for p in pts for c in p]), fill=255, width=w * 2, joint='curve')
        for (x, y) in pts:
            self._draw(layer).ellipse(self._s([x - w / 2, y - w / 2, x + w / 2, y + w / 2]), fill=255)

    def rect(self, x0, y0, x1, y1, layer='body'):
        self._draw(layer).rectangle(self._s([x0, y0, x1, y1]), fill=255)

    def eye(self, x, y, big=False):
        self.eyes.append((x, y, big))

    def _draw(self, layer):
        return {'body': self.d, 'alt': self.da, 'acc': self.dc}[layer]

    def render(self, back=False):
        size = (64, 64)
        body = self.body.resize(size, Image.LANCZOS).point(lambda v: 255 if v > 110 else 0)
        alt = self.alt.resize(size, Image.LANCZOS).point(lambda v: 255 if v > 110 else 0)
        acc = self.acc.resize(size, Image.LANCZOS).point(lambda v: 255 if v > 110 else 0)
        bp, ap, cp = body.load(), alt.load(), acc.load()
        im = Image.new('P', size, 0)
        px = im.load()
        inside = lambda x, y: 0 <= x < 64 and 0 <= y < 64 and (bp[x, y] or ap[x, y] or cp[x, y])
        for y in range(64):
            for x in range(64):
                if not inside(x, y):
                    continue
                if cp[x, y]:
                    px[x, y] = ACCENT
                    continue
                isalt = bool(ap[x, y])
                lit = not inside(x - 2, y - 2)
                dark = not inside(x + 2, y + 2) or (back and not inside(x - 3, y))
                if isalt:
                    px[x, y] = ALT_LIGHT if lit else ALT_SHADE if dark else ALT
                else:
                    px[x, y] = LIGHT if lit else SHADE if dark else BASE
        for y in range(64):
            for x in range(64):
                if not inside(x, y) and any(inside(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    px[x, y] = OUTLINE
        if not back:
            for (x, y, big) in self.eyes:
                r = 2 if big else 1
                for dy in range(-r, r + 1):
                    for dx in range(-r, r + 1):
                        if 0 <= x + dx < 64 and 0 <= y + dy < 64:
                            px[x + dx, y + dy] = BLACK
                if 0 <= x - (1 if big else 0) < 64 and 0 <= y - 1 < 64:
                    px[x - (1 if big else 0), y - 1] = WHITE
        return im


# ---- body families. Each draws facing left (front sprites look toward the player's side).

def quadruped(c, s, r):
    big = 0.8 + 0.2 * next(r)
    leg = 6 + int(5 * next(r))
    c.ell(16, 26, 52, 46)                       # body
    c.ell(18, 36, 44, 47, 'alt')                # belly
    for x in (20, 28, 40, 47):                  # legs
        c.rect(x - 2, 40, x + 2, 46 + leg)
    c.line([(50, 30), (58, 24 - 6 * next(r))], 4)   # tail
    c.ell(6, 16, 26, 34)                        # head
    c.poly([(10, 18), (13, 9), (17, 17)])       # ear
    c.poly([(18, 17), (22, 9), (24, 18)])
    c.ell(3, 25, 11, 31, 'alt')                 # muzzle
    c.eye(12, 23)


def primate(c, s, r):
    c.ell(20, 22, 44, 48)
    c.ell(24, 30, 40, 46, 'alt')
    c.line([(22, 26), (12, 42), (14, 50)], 5)
    c.line([(42, 26), (52, 42), (50, 50)], 5)
    c.line([(26, 46), (24, 60)], 6)
    c.line([(38, 46), (40, 60)], 6)
    c.ell(22, 6, 42, 26)
    c.ell(26, 14, 38, 24, 'alt')
    c.eye(29, 15)
    c.eye(36, 15)


def dinosaur(c, s, r):
    c.ell(18, 22, 46, 44)
    c.poly([(42, 30), (62, 46), (60, 50), (40, 40)])
    c.line([(26, 40), (24, 60)], 7)
    c.line([(38, 40), (40, 60)], 7)
    c.line([(20, 30), (12, 18)], 9)
    c.ell(2, 6, 22, 22)
    c.ell(20, 30, 40, 42, 'alt')
    c.poly([(26, 22), (30, 16), (34, 22), (38, 17), (42, 24)], 'alt')
    c.eye(9, 11)


def flier(c, s, r):
    up = next(r) > 0.4
    c.ell(16, 26, 46, 46)                       # body
    c.ell(18, 34, 40, 46, 'alt')                # breast
    c.poly([(44, 34), (60, 40), (58, 44), (44, 42)])   # tail
    if up:
        c.poly([(26, 30), (46, 6), (52, 12), (40, 34)])
    else:
        c.poly([(24, 30), (54, 28), (50, 40), (28, 40)])
    c.ell(8, 14, 26, 32)                        # head
    c.poly([(9, 22), (1, 25), (9, 27)], 'acc')  # beak
    c.line([(26, 46), (25, 56)], 2)
    c.line([(34, 46), (35, 56)], 2)
    c.eye(14, 21)


def insect(c, s, r):
    larva = 'aterpillar' in s['name'] or 'Larva' in s['name'] or 'Worm' in s['name'] or s.get('stage') == 'Caterpillar'
    if larva:
        for i in range(6):
            x = 10 + i * 8
            c.ell(x - 6, 34 - 3 * (i % 2), x + 6, 48 - 3 * (i % 2), 'alt' if i % 2 else 'body')
        c.ell(2, 28, 16, 44)
        c.eye(7, 34)
        return
    winged = 'Sky' in s['types']
    if winged:
        c.poly([(28, 30), (14, 4), (40, 10)], 'alt')
        c.poly([(34, 30), (60, 8), (58, 30)], 'alt')
        c.poly([(30, 34), (16, 56), (36, 46)], 'alt')
    for i, x in enumerate((24, 32, 40)):
        c.line([(x, 38), (x - 8 + 4 * i, 56)], 2)
        c.line([(x, 38), (x + 4 + 2 * i, 56)], 2)
    c.ell(30, 28, 58, 46)          # abdomen
    c.ell(20, 28, 34, 42)          # thorax
    c.ell(10, 26, 22, 38)          # head
    c.line([(14, 28), (6, 14)], 1)
    c.line([(18, 27), (16, 12)], 1)
    c.eye(13, 31, big=True)


def many_legged(c, s, r):
    crab = s['group'] in ('Crustacean', 'Chelicerate')
    for i in range(4):
        y = 34 + i * 4
        c.line([(30, y), (16 - 2 * i, y + 8), (10 - 2 * i, y + 18)], 2)
        c.line([(34, y), (48 + 2 * i, y + 8), (54 + 2 * i, y + 18)], 2)
    if crab:
        c.line([(24, 32), (10, 22)], 4)
        c.ell(2, 12, 14, 24, 'alt')
        c.line([(40, 32), (54, 22)], 4)
        c.ell(50, 12, 62, 24, 'alt')
        c.ell(14, 24, 50, 46)
    else:
        c.ell(30, 26, 56, 48)
        c.ell(14, 28, 32, 42)
        c.ell(36, 32, 50, 44, 'alt')
    c.eye(22, 32)
    c.eye(27, 31)


def swimmer(c, s, r):
    whale = s['group'] == 'Mammal'
    if whale:
        c.ell(4, 24, 52, 48)
        c.ell(8, 38, 44, 49, 'alt')
        c.poly([(48, 34), (62, 22), (60, 36), (62, 50), (48, 40)])
        c.poly([(24, 44), (30, 56), (34, 46)])
        c.eye(14, 34)
        return
    seahorse = 'eahorse' in s['name']
    if seahorse:
        c.line([(30, 14), (34, 30), (30, 44), (36, 54), (42, 50)], 8)
        c.ell(22, 8, 38, 20)
        c.line([(24, 14), (12, 16)], 3)
        c.eye(28, 13)
        return
    long = next(r)
    c.ell(6, 26, 46 + 8 * long, 46)
    c.ell(10, 38, 40, 46, 'alt')
    c.poly([(44 + 8 * long, 36), (62, 22), (62, 50)])
    c.poly([(20, 28), (30, 14), (36, 28)])
    c.poly([(22, 44), (26, 54), (32, 44)])
    c.eye(14, 33, big=True)


def soft_bodied(c, s, r):
    g, n = s['group'], s['name']
    if g == 'Cnidarian' or 'Jelly' in n or 'Siphonophore' in n or "Man O'" in n:
        c.ell(10, 8, 54, 36)
        c.ell(16, 24, 48, 36, 'alt')
        for i in range(6):
            x = 14 + i * 7
            c.line([(x, 32), (x - 3, 44), (x + 2, 52), (x - 2, 60)], 2)
        return
    if 'Octopus' in n or 'Squid' in n or 'Argonaut' in n:
        for i in range(6):
            x = 16 + i * 6
            c.line([(x, 34), (x - 6 + 2 * i, 48), (x - 10 + 4 * i, 58)], 4)
        c.ell(14, 6, 50, 38)
        c.eye(24, 26, big=True)
        c.eye(40, 26, big=True)
        return
    if g == 'Annelid' or 'Worm' in n or 'Nematode' in n:
        c.line([(6, 48), (16, 38), (28, 46), (40, 36), (54, 44), (58, 54)], 8)
        c.line([(16, 38), (28, 46)], 3, 'alt')
        return
    shell = 'Snail' in n or g == 'Mollusk' and ('Chiton' in n or 'Oyster' in n or 'Clam' in n or 'Nautilus' in n)
    c.ell(4, 40, 60, 54)                         # foot
    if shell:
        c.ell(16, 18, 52, 50, 'alt')
        c.line([(34, 34), (40, 30), (38, 40), (30, 38)], 2)
    c.line([(10, 44), (6, 30)], 2)
    c.line([(16, 42), (14, 28)], 2)
    c.eye(6, 30)
    c.eye(14, 28)


def serpentine(c, s, r):
    c.line([(52, 56), (36, 54), (20, 50), (16, 40), (26, 32), (44, 32), (50, 22), (40, 14), (26, 14)], 8)
    c.line([(20, 50), (16, 40), (26, 32)], 3, 'alt')
    c.ell(10, 8, 28, 20)
    c.poly([(10, 14), (4, 12), (4, 16)], 'acc')
    c.eye(16, 12)


def low_reptile(c, s, r):
    n, g = s['name'], s['group']
    if 'Turtle' in n or 'Tortoise' in n:
        c.ell(12, 22, 54, 50, 'alt')
        c.ell(4, 32, 18, 44)
        c.rect(14, 44, 20, 54)
        c.rect(44, 44, 50, 54)
        c.eye(9, 36)
        return
    if g == 'Amphibian' and ('Frog' in n or 'Toad' in n):
        c.ell(10, 28, 52, 54)
        c.ell(16, 40, 46, 54, 'alt')
        c.ell(12, 20, 26, 34)
        c.ell(32, 20, 46, 34)
        c.line([(14, 50), (6, 58)], 4)
        c.line([(48, 50), (56, 58)], 4)
        c.eye(19, 26, big=True)
        c.eye(39, 26, big=True)
        return
    c.ell(14, 30, 46, 44)
    c.poly([(44, 34), (62, 42), (44, 42)])
    c.ell(2, 28, 20, 40)
    c.ell(18, 36, 42, 44, 'alt')
    for x in (18, 40):
        c.line([(x, 40), (x - 4, 52)], 3)
        c.line([(x + 2, 40), (x + 6, 52)], 3)
    c.eye(8, 32)


def sessile(c, s, r):
    n, g = s['name'], s['group']
    if g == 'Fungus' or 'Mushroom' in n or 'Agaric' in n or 'Death Cap' in n:
        c.rect(26, 30, 38, 58)
        c.ell(8, 12, 56, 38)
        for _ in range(5):
            x, y = 14 + 34 * next(r), 16 + 12 * next(r)
            c.ell(x - 3, y - 2, x + 3, y + 2, 'alt')
        return
    if g == 'Lichen' or g == 'Alga' and 'Snow' in n:
        c.ell(4, 30, 60, 58, 'alt')
        for _ in range(9):
            x, y = 8 + 46 * next(r), 32 + 20 * next(r)
            c.ell(x - 5, y - 4, x + 5, y + 4)
        return
    if g == 'Alga' or 'Kelp' in n:
        for i in range(4):
            x = 14 + i * 12
            c.line([(x, 60), (x - 6, 44), (x + 4, 28), (x - 2, 8)], 5)
        c.ell(20, 10, 30, 20, 'alt')
        return
    tree = any(k in n for k in ('Tree', 'Redwood', 'Sequoia', 'Cycad', 'Pine', 'Mangrove', 'Ginkgo', 'Saguaro', 'Baobab'))
    if tree:
        c.rect(26, 30, 38, 60)
        c.ell(8, 2, 56, 40, 'alt')
        c.ell(4, 14, 30, 36, 'alt')
        c.ell(34, 14, 60, 36, 'alt')
        return
    c.line([(32, 60), (30, 40), (32, 22)], 3)
    c.poly([(30, 46), (8, 36), (14, 50)])
    c.poly([(32, 38), (56, 30), (50, 44)])
    c.ell(20, 6, 44, 28, 'alt')
    c.ell(27, 12, 37, 22, 'acc')


def microscope(c, s, r):
    g, n = s['group'], s['name']
    c.ell(2, 2, 62, 62, 'alt')
    inner = Image.new('L', (128, 128), 0)
    ImageDraw.Draw(inner).ellipse([12, 12, 116, 116], fill=255)
    c.alt.paste(0, mask=inner)
    if g == 'Virus':
        c.poly([(32, 12), (50, 22), (50, 42), (32, 52), (14, 42), (14, 22)])
        for (x, y) in ((32, 8), (54, 20), (54, 44), (32, 56), (10, 44), (10, 20)):
            c.ell(x - 3, y - 3, x + 3, y + 3, 'acc')
    elif g in ('Bacterium', 'Archaeon'):
        k = int(3 * next(r))
        if k == 0:
            c.line([(18, 40), (46, 24)], 14)
            c.line([(46, 24), (54, 14), (50, 6)], 1)
        elif k == 1:
            for (x, y) in ((22, 26), (36, 24), (28, 38), (42, 38)):
                c.ell(x - 7, y - 7, x + 7, y + 7)
        else:
            c.line([(14, 32), (22, 22), (30, 40), (38, 22), (46, 40), (52, 30)], 6)
    else:
        c.ell(14, 16, 50, 48)
        c.ell(26, 26, 36, 36, 'acc')
        for i in range(10):
            import math
            a = i * 0.628
            x, y = 32 + 19 * math.cos(a), 32 + 17 * math.sin(a)
            c.line([(x, y), (32 + 23 * math.cos(a), 32 + 21 * math.sin(a))], 1)


FAMILIES = {
    'quadruped': quadruped, 'primate': primate, 'dinosaur': dinosaur, 'flier': flier, 'insect': insect,
    'many_legged': many_legged, 'swimmer': swimmer, 'soft_bodied': soft_bodied, 'serpentine': serpentine,
    'low_reptile': low_reptile, 'sessile': sessile, 'microscope': microscope,
}


def draw(s, back=False):
    c = Canvas()
    FAMILIES.get(s['family'], microscope)(c, s, rnd(s['id']))
    im = c.render(back=back)
    if back:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    return im


def write_pal(path, pal):
    with open(path, 'w', newline='\r\n') as f:
        f.write('JASC-PAL\n0100\n16\n' + ''.join('%d %d %d\n' % c for c in pal))


def with_pal(im, pal):
    im = im.copy()
    im.putpalette([v for c in pal for v in c])
    return im


def bob(im, dy):
    """Second animation frame: the body shifted down a pixel."""
    out = Image.new('P', im.size, 0)
    out.paste(im, (0, dy))
    out.putpalette(im.getpalette())
    return out


# ---- icon palettes are shared; pick the closest of the three and remap to it.
def read_pal(path):
    lines = open(path).read().split()
    return [tuple(int(v) for v in lines[3 + i * 3:6 + i * 3]) for i in range(16)]


ICON_PALS = [read_pal(P('graphics', 'pokemon', 'icon_palettes', 'icon_palette_%d.pal' % i)) for i in range(3)]


def to_icon(front, pal):
    small = front.convert('RGB').resize((32, 32), Image.NEAREST)
    mask = front.resize((32, 32), Image.NEAREST)
    best = None
    for pi, ip in enumerate(ICON_PALS):
        err = 0
        idx = []
        for y in range(32):
            for x in range(32):
                if mask.getpixel((x, y)) == 0:
                    idx.append(0)
                    continue
                c = small.getpixel((x, y))
                k, e = min(((k, sum((a - b) ** 2 for a, b in zip(c, ip[k]))) for k in range(1, 16)), key=lambda t: t[1])
                idx.append(k)
                err += e
        if best is None or err < best[0]:
            best = (err, pi, idx)
    _, pi, idx = best
    frame = Image.new('P', (32, 32), 0)
    frame.putdata(idx)
    icon = Image.new('P', (32, 64), 0)
    icon.paste(frame, (0, 0))
    icon.paste(frame, (0, 33))  # second frame bobs down a pixel
    icon.putpalette([v for c in ICON_PALS[pi] for v in c])
    return icon, pi


def footprint():
    im = Image.new('P', (16, 16), 0)
    im.putpalette([255, 255, 255, 0, 0, 0] + [0, 0, 0] * 14)
    return im


def bbox_coords(im):
    box = im.getbbox() or (0, 0, 64, 64)
    w = min(64, ((box[2] - box[0]) + 7) // 8 * 8)
    h = min(64, ((box[3] - box[1]) + 7) // 8 * 8)
    return w, h, 64 - box[3]


def species_dirs():
    """Map species constant -> graphics directory, from the front pic table."""
    gfx = read('src/data/graphics/pokemon.h')
    table = read('src/data/pokemon_graphics/still_front_pic_table.h')
    out = {}
    for m in re.finditer(r'SPECIES_SPRITE\((\w+),\s*(\w+)\)', table):
        sym = m.group(2)
        p = re.search(r'%s\[\] = INCGFX_U32\("graphics/pokemon/([\w/]+)/front\.(?:png|4bpp)"' % sym, gfx)
        if p:
            out[m.group(1)] = p.group(1)
    return out


import sys
if '--preview' in sys.argv:
    out = sys.argv[sys.argv.index('--preview') + 1]
    picks = smap[:: max(1, len(smap) // 48)][:48]
    sheet = Image.new('RGB', (8 * 136, 6 * 72), (255, 255, 255))
    for i, o in enumerate(picks):
        sp = species[o['id']]
        f = with_pal(draw(sp), palette_for(sp)).convert('RGB')
        b = with_pal(draw(sp, back=True), palette_for(sp, True)).convert('RGB')
        sheet.paste(f, ((i % 8) * 136, (i // 8) * 72))
        sheet.paste(b, ((i % 8) * 136 + 66, (i // 8) * 72))
    sheet.resize((sheet.width * 2, sheet.height * 2), Image.NEAREST).save(out)
    raise SystemExit(0)

dirs = species_dirs()
front_coords = read('src/data/pokemon_graphics/front_pic_coordinates.h')
back_coords = read('src/data/pokemon_graphics/back_pic_coordinates.h')
icon_src = read('src/pokemon_icon.c')
done = 0
for o in smap:
    s = species[o['id']]
    slot = o['slot']
    d = dirs.get(slot)
    if not d:
        raise SystemExit('no graphics dir for ' + slot)
    pal, shiny = palette_for(s), palette_for(s, shiny=True)
    front = with_pal(draw(s), pal)
    back = with_pal(draw(s, back=True), pal)
    targets = [d]
    if slot == 'UNOWN':
        targets = [os.path.join('unown', x) for x in sorted(os.listdir(P('graphics', 'pokemon', 'unown')))
                   if os.path.isdir(P('graphics', 'pokemon', 'unown', x))]
    if slot == 'CASTFORM':
        targets = ['castform/' + f for f in ('normal', 'sunny', 'rainy', 'snowy')]
    pal_dirs = {'castform/' + f: True for f in ('normal', 'sunny', 'rainy', 'snowy')}
    for t in targets:
        base = P('graphics', 'pokemon', t)
        front.save(os.path.join(base, 'front.png'))
        anim = Image.new('P', (64, 128), 0)
        anim.paste(front, (0, 0))
        anim.paste(bob(front, 1), (0, 64))
        anim.putpalette(front.getpalette())
        anim.save(os.path.join(base, 'anim_front.png'))
        back.save(os.path.join(base, 'back.png'))
        icon, ipal = to_icon(front, pal)
        if os.path.exists(os.path.join(base, 'icon.png')) or t == d:
            icon.save(os.path.join(base, 'icon.png'))
        if os.path.exists(os.path.join(base, 'normal.pal')) or t in pal_dirs or t == d:
            write_pal(os.path.join(base, 'normal.pal'), pal)
            write_pal(os.path.join(base, 'shiny.pal'), shiny)
    root = P('graphics', 'pokemon', d.split('/')[0])
    if os.path.exists(os.path.join(root, 'normal.pal')) and slot == 'UNOWN':
        write_pal(os.path.join(root, 'normal.pal'), pal)
        write_pal(os.path.join(root, 'shiny.pal'), shiny)
    fp = os.path.join(root, 'footprint.png')
    footprint().save(fp)
    w, h, yo = bbox_coords(front)
    front_coords = re.sub(r'(\[SPECIES_%s\]\s*= \{ \.size = )MON_COORDS_SIZE\(\d+, \d+\), \.y_offset =\s*\d+' % slot,
                          r'\g<1>MON_COORDS_SIZE(%d, %d), .y_offset = %2d' % (w, h, yo), front_coords)
    bw, bh, byo = bbox_coords(back)
    back_coords = re.sub(r'(\[SPECIES_%s\]\s*= \{ \.size = )MON_COORDS_SIZE\(\d+, \d+\), \.y_offset =\s*\d+' % slot,
                         r'\g<1>MON_COORDS_SIZE(%d, %d), .y_offset = %2d' % (bw, bh, byo), back_coords)
    icon_src = re.sub(r'(\[SPECIES_%s\] = )\d(,)' % slot, r'\g<1>%d\g<2>' % ipal, icon_src)
    done += 1

write('src/data/pokemon_graphics/front_pic_coordinates.h', front_coords)
write('src/data/pokemon_graphics/back_pic_coordinates.h', back_coords)
write('src/pokemon_icon.c', icon_src)
print('sprites: %d species' % done)
