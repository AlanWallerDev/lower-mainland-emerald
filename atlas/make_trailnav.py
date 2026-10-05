#!/usr/bin/env python3
"""TrailNav branding in baked-in graphics: the device header reads "TRAILNAV" instead of
"POKeMON NAVIGATOR" (top title and bottom bar), and the main-menu button reads "BC MAP" instead of
"HOENN MAP". Letters are cut from the graphics' own fonts; missing ones are drawn to match.

Always starts from the upstream images (needs the pret `upstream` remote), so it is idempotent.
Run from the repo root: python3 atlas/make_trailnav.py
"""
import io
import os
import re
import struct
import subprocess

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)


def upstream(path, mode='rb'):
    data = subprocess.run(['git', 'show', 'upstream/master:' + path], cwd=ROOT, capture_output=True, check=True).stdout
    return data


def pixels(im):
    return im.get_flattened_data() if hasattr(im, 'get_flattened_data') else im.getdata()


def glyphs(px, x0, x1, y0, y1, text, ink=1, last=False):
    """Cut the letters of `text` (spaces skipped) from columns x0..x1 into sets of (dx, dy) ink pixels."""
    cols = [x for x in range(x0, x1) if any(px[x, y] == ink for y in range(y0, y1))]
    runs, start = [], cols[0]
    for a, b in zip(cols, cols[1:] + [None]):
        if b != a + 1:
            runs.append((start, a))
            start = b
    letters = [c for c in text if c != ' ']
    if last:  # only the last letters of the run of text
        runs = runs[-len(letters):]
    assert len(runs) == len(letters), 'expected %d letters, found %d runs' % (len(letters), len(runs))
    out = {}
    for ch, (a, b) in zip(letters, runs):
        out.setdefault(ch, {(x - a, y - y0) for x in range(a, b + 1) for y in range(y0, y1) if px[x, y] == ink})
    return out


def draw(px, font, text, x, y, ink, shadow=None, gap=1, space=4, bg=None):
    for ch in text:
        if ch == ' ':
            x += space
            continue
        g = font[ch]
        w = max(dx for dx, _ in g) + 1
        for dx, dy in g:
            px[x + dx, y + dy] = ink
        if shadow is not None:
            for dx, dy in g:
                for sx, sy in ((dx + 1, dy), (dx, dy + 1)):
                    if (sx, sy) not in g and px[x + sx, y + sy] == bg:
                        px[x + sx, y + sy] = shadow
        x += w + gap
    return x


def width(font, text, gap=1, space=4):
    return sum(space if c == ' ' else max(dx for dx, _ in font[c]) + 1 + gap for c in text) - gap


# ---- header: decode the tilemap into a canvas -------------------------------------------------
tiles_img = Image.open(io.BytesIO(upstream('graphics/pokenav/header.png')))
pal = tiles_img.getpalette()
entries = struct.unpack('<1024H', upstream('graphics/pokenav/header.bin'))
cv = Image.new('P', (256, 256), 0)
cv.putpalette(pal)
for i, v in enumerate(entries):
    t = v & 0x3ff
    tile = tiles_img.crop((t * 8, 0, t * 8 + 8, 8))
    if v >> 10 & 1:
        tile = tile.transpose(Image.FLIP_LEFT_RIGHT)
    if v >> 11 & 1:
        tile = tile.transpose(Image.FLIP_TOP_BOTTOM)
    cv.paste(tile, ((i % 32) * 8, (i // 32) * 8))
px = cv.load()
BG = 4

# Big title font (rows 3-15), white on green, from "POKeMON NAVIGATOR".
big = glyphs(px, 96, 170, 3, 16, 'NAVIGATOR')
big['L'] = {(x, y) for x in range(2) for y in range(13)} | {(x, y) for x in range(7) for y in (11, 12)}
for y in range(2, 16):
    for x in range(8, 176):
        px[x, y] = BG
draw(px, big, 'TRAILNAV', 24, 3, 1)

# Small bottom-bar font (rows 180-188), white with shadow 5, from the "NAVIGATOR" of the bottom bar.
small = glyphs(px, 140, 240, 180, 188, 'NAVIGATOR', last=True)
small['L'] = {(0, y) for y in range(7)} | {(x, 6) for x in range(4)}
for y in range(179, 189):
    for x in range(140, 240):
        px[x, y] = BG
w = width(small, 'TRAILNAV')
draw(px, small, 'TRAILNAV', 237 - w, 181, 1, shadow=5, bg=BG)

# Retile: tile 0 stays the upstream blank tile; identical tiles are shared.
tiles, index, out_entries = [], {}, []
blank = tuple(pixels(tiles_img.crop((0, 0, 8, 8))))
tiles.append(blank)
index[blank] = 0
for i, v in enumerate(entries):
    x, y = (i % 32) * 8, (i // 32) * 8
    key = tuple(pixels(cv.crop((x, y, x + 8, y + 8))))
    if key not in index:
        index[key] = len(tiles)
        tiles.append(key)
    out_entries.append((v & 0xf000) | index[key])
img = Image.new('P', (len(tiles) * 8, 8), 0)
img.putpalette(pal)
for i, t in enumerate(tiles):
    img.paste(Image.frombytes('P', (8, 8), bytes(t)), (i * 8, 0))
img.save(P('graphics', 'pokenav', 'header.png'))
open(P('graphics', 'pokenav', 'header.bin'), 'wb').write(struct.pack('<1024H', *out_entries))
g = open(P('src', 'graphics.c'), encoding='utf-8').read()
g = re.sub(r'(pokenav/header\.png", "\.4bpp\.lz", "-num_tiles )\d+', r'\g<1>%d' % len(tiles), g)
open(P('src', 'graphics.c'), 'w', encoding='utf-8').write(g)

# ---- main-menu button: "HOENN MAP" -> "BC MAP" -------------------------------------------------
opt = Image.open(io.BytesIO(upstream('graphics/pokenav/options/hoenn_map.png')))
strip = Image.new('P', (128, 16), 0)
strip.putpalette(opt.getpalette())
for i in range(4):
    strip.paste(opt.crop((0, i * 16, 32, i * 16 + 16)), (i * 32, 0))
sp = strip.load()
font = glyphs(sp, 16, 66, 4, 13, 'HOENN MAP')
font['B'] = {(x, y) for y, row in enumerate(['1111.', '1...1', '1...1', '1...1', '1111.', '1...1', '1...1', '1...1', '1111.'])
             for x, c in enumerate(row) if c == '1'}
font['C'] = {(x, y) for y, row in enumerate(['.111.', '1...1', '1....', '1....', '1....', '1....', '1....', '1...1', '.111.'])
             for x, c in enumerate(row) if c == '1'}
for y in range(4, 14):
    for x in range(16, 128):
        sp[x, y] = 4
draw(sp, font, 'BC MAP', 17, 4, 1, shadow=2, bg=4, space=5)
for i in range(4):
    opt.paste(strip.crop((i * 32, 0, i * 32 + 32, 16)), (0, i * 16))
opt.save(P('graphics', 'pokenav', 'options', 'hoenn_map.png'))
print('trailnav: header %d tiles, map button repainted' % len(tiles))
