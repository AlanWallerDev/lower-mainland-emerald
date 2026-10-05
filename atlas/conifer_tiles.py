#!/usr/bin/env python3
"""Conifer trees for the overworld: re-shades the crowns of the general tileset's trees (the 32x32
tree and its forest variants, metatiles 0x1d4-0x1ff) into drooping conifer tiers, and narrows the
tops of standalone trees into points.

Works on tile pixels, so every variant that shares a tile changes together. The tier pattern is
symmetric about the tree's centre, so mirrored tiles still line up. Starts from upstream (needs the
pret `upstream` remote), so it is idempotent.
Run from the repo root: python3 atlas/conifer_tiles.py [--preview out.png]
"""
import io
import os
import struct
import subprocess
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
REL = 'data/tilesets/primary/general/'
TREE_PAL = 2
CROWN = {1, 2, 3, 4}          # palette-2 crown shades, light to dark
GRASS = (13, 14)              # palette-2 grass shades used to fill cut-away corners
FAMILY = range(0x1d4, 0x200)  # tree metatiles
TOPS = {0x1d4: 0, 0x1d5: 16}  # standalone tree tops (left and right halves): sharpen these


def git_show(path):
    return subprocess.run(['git', 'show', 'upstream/master:' + path], cwd=ROOT, capture_output=True, check=True).stdout


tiles = Image.open(io.BytesIO(git_show(REL + 'tiles.png')))
tp = tiles.load()
TW = tiles.width // 8
meta = git_show(REL + 'metatiles.bin')


def entries(m):
    return struct.unpack('<8H', meta[m * 16:m * 16 + 16])


# Where each tree tile sits across the tree: x of its first column (0-31) and whether it is mirrored.
place = {}
for m in FAMILY:
    for k, v in enumerate(entries(m)):
        tid, hf, pal = v & 0x3ff, v >> 10 & 1, v >> 12
        if pal != TREE_PAL or tid == 0 or tid >= 512:
            continue
        x0 = (m % 2) * 16 + (k % 4 % 2) * 8
        place.setdefault(tid, (x0, hf))


def shade(x, y):
    """Conifer tier shade at tree column x (0-31) and tile row y: bands that droop from the centre."""
    d = abs(x - 15.5)
    phase = (y + int(d * 0.75)) % 8
    s = (2, 1, 2, 3, 3, 3, 4, 4)[phase]
    if s == 1 and (int(d) + y) % 3 == 0:   # break up the highlight so tiers look like needles
        s = 2
    if s == 3 and (int(d) * 7 + y * 3) % 5 == 0:
        s = 4
    return s


def get(tid):
    tx, ty = tid % TW, tid // TW
    return [[tp[tx * 8 + x, ty * 8 + y] for x in range(8)] for y in range(8)]


def put(tid, px):
    tx, ty = tid % TW, tid // TW
    for y in range(8):
        for x in range(8):
            tp[tx * 8 + x, ty * 8 + y] = px[y][x]


for tid, (x0, hf) in place.items():
    px = get(tid)
    out = [row[:] for row in px]
    for y in range(8):
        for x in range(8):
            if px[y][x] not in CROWN:
                continue
            # keep the dark outline: crown pixels next to a non-crown pixel stay as they are
            edge = any(not (0 <= x + dx < 8 and 0 <= y + dy < 8) or px[y + dy][x + dx] not in CROWN
                       for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                       if 0 <= x + dx < 8 and 0 <= y + dy < 8)
            if edge and px[y][x] == 4:
                continue
            col = x0 + (7 - x if hf else x)
            out[y][x] = shade(col, y)
    put(tid, out)

# Sharpen standalone tops: cut the rounded shoulders into a pointed crown (16 rows of the top half).
for m, xoff in TOPS.items():
    e = entries(m)
    for k in range(4):
        v = e[k]
        tid, hf = v & 0x3ff, v >> 10 & 1
        if v >> 12 != TREE_PAL:
            continue
        px = get(tid)
        for y in range(8):
            for x in range(8):
                col = xoff + (k % 2) * 8 + (7 - x if hf else x)
                row = (k // 2) * 8 + y
                half = 3 + row * 0.85          # crown half-width at this row
                d = abs(col - 15.5)
                if px[y][x] in CROWN and d > half:
                    px[y][x] = GRASS[(col + row) % 2]
                elif px[y][x] in CROWN and d > half - 1.2:
                    px[y][x] = 4
        put(tid, px)

# Tips of the tree below, drawn on the top layer of a tree's bottom metatile (0x1dc/0x1dd) so the
# nearer, lower tree stands in front. Redraw them as the point of the conifer below (rows -8..-1
# above that tree's crown); everything else is transparent so the upper tree's base shows through.
for m, k in ((0x1dc, 7), (0x1dd, 6)):
    v = entries(m)[k]
    tid, hf = v & 0x3ff, v >> 10 & 1
    x0 = (m % 2) * 16 + (k % 4 % 2) * 8
    px = [[0] * 8 for _ in range(8)]
    for y in range(8):
        for x in range(8):
            col = x0 + (7 - x if hf else x)
            row = y - 8
            half = 3 + row * 0.5         # rises ~6 px over the upper tree's base and trunk
            d = abs(col - 15.5)
            if d <= half:
                px[y][x] = 4 if d > half - 1.2 else shade(col, row % 8)
    put(tid, px)

tiles.save(P(REL, 'tiles.png'))

if '--preview' in sys.argv:
    out = sys.argv[sys.argv.index('--preview') + 1]
    pal = open(P(REL, 'palettes', '%02d.pal' % TREE_PAL)).read().split()[3:]
    colors = [tuple(map(int, pal[i * 3:i * 3 + 3])) for i in range(16)]
    img = Image.new('RGB', (96, 64))
    grid = [[0x1d4, 0x1d5] * 3, [0x1dc, 0x1dd] * 3] * 2
    for gy, row in enumerate(grid):
        for gx, m in enumerate(row):
            for k, v in enumerate(entries(m)[:4]):
                tid, hf, vf = v & 0x3ff, v >> 10 & 1, v >> 11 & 1
                for y in range(8):
                    for x in range(8):
                        c = tp[(tid % TW) * 8 + (7 - x if hf else x), (tid // TW) * 8 + (7 - y if vf else y)]
                        img.putpixel((gx * 16 + (k % 2) * 8 + x, gy * 16 + (k // 2) * 8 + y), colors[c])
    img.resize((384, 256), Image.NEAREST).save(out)
print('conifer: %d tree tiles re-shaded' % len(place))
