#!/usr/bin/env python3
"""ECHO BAY float homes: the round thatched huts on Pacifidlog's log rafts become BC float homes, a
plank cabin with a slate standing-seam metal roof, a stovepipe, two windows and a centre door.

Redraws the hut's layer-1 tiles (palette 9) in data/tilesets/secondary/pacifidlog in place, so no
map changes: the hut is metatiles 0x202 (top) and 0x209-0x21b (3x3), and its deck, water and cast
shadow (layer 0) are kept. The upstream hut mirrors tiles about its centre, so the cabin is drawn
symmetric except in the tiles used once (door). Uses palette 9's existing colours.
Starts from upstream (needs the pret `upstream` remote), so it is idempotent.
Run from the repo root: python3 atlas/float_homes.py [--preview out.png]
"""
import io
import os
import struct
import subprocess
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REL = 'data/tilesets/secondary/pacifidlog/'
PAL = 9
GRID = [[None, 0x202, None], [0x209, 0x20a, 0x20b], [0x211, 0x212, 0x213], [0x219, 0x21a, 0x21b]]
# Palette 9: 8/7/6 slate blues, 14 grey, 13/12/11/10/9 cedar browns to cream, 15 blue.
OUT, SLATE, SEAM, RIDGE = 8, 7, 6, 14
DARKWOOD, PLANK_LINE, PLANK, PLANK_HI, CREAM, GLASS = 13, 12, 11, 10, 9, 15


def git_show(path):
    return subprocess.run(['git', 'show', 'upstream/master:' + path], cwd=ROOT, capture_output=True, check=True).stdout


def draw():
    """The cabin as a 48x64 grid of palette indices (0 = see-through), symmetric about x = 23.5."""
    c = [[0] * 48 for _ in range(64)]

    def put(x, y, v):
        c[y][x] = v
        c[y][47 - x] = v

    # Stovepipe on the ridge, with a cap.
    for y in range(9, 17):
        for x in (22, 23):
            put(x, y, RIDGE if x == 23 else OUT)
    for x in (21, 22, 23):
        put(x, 8, OUT)
    # Roof: ridge at y 16, eaves at y 37, widening down to the overhang.
    for y in range(15, 38):
        half = 15 + (y - 15) * 8 // 22          # 15 at the ridge, 23 at the eaves
        for x in range(24 - half, 24):
            edge = x == 24 - half
            if y == 15 or edge:
                v = OUT
            elif y in (16, 17):
                v = RIDGE                        # ridge cap
            elif y >= 35:
                v = OUT if y == 37 else SEAM     # eave trim
            else:
                v = SEAM if (23 - x) % 4 == 1 else SLATE
            put(x, y, v)
    # Walls below the eaves: cedar planks, darker under the eave.
    for y in range(38, 63):
        for x in range(4, 24):
            if x == 4:
                v = DARKWOOD
            elif y == 38:
                v = DARKWOOD
            elif y % 3 == 0:
                v = PLANK_LINE
            elif y % 3 == 1:
                v = PLANK_HI
            else:
                v = PLANK
            put(x, y, v)
    for x in range(3, 24):  # sill log on the raft
        put(x, 62, DARKWOOD)
        put(x, 63, OUT)
    put(3, 61, DARKWOOD)
    # Windows: cream frame, blue glass with a pale glint, mullion.
    for y in range(42, 52):
        for x in range(8, 16):
            frame = y in (42, 51) or x in (8, 15)
            v = CREAM if frame else GLASS
            if not frame and x == 11:
                v = CREAM
            if not frame and y == 43 and x in (9, 12):
                v = CREAM
            put(x, y, v)
    for x in range(7, 17):
        put(x, 52, DARKWOOD)  # sill shadow
    # Door: cream trim, dark wood with a lighter panel and a handle.
    for y in range(43, 62):
        for x in range(19, 24):
            if y == 43 or x == 19:
                v = CREAM
            elif x == 20 or y == 44:
                v = DARKWOOD
            elif 47 <= y <= 57 and 21 <= x:
                v = PLANK_LINE
            else:
                v = DARKWOOD
            put(x, y, v)
    c[52][26] = CREAM  # handle, right of centre (the door tiles are used once)
    return c


def main():
    tiles = Image.open(io.BytesIO(git_show(REL + 'tiles.png')))
    tp = tiles.load()
    tw = tiles.width // 8
    meta = git_show(REL + 'metatiles.bin')
    art = draw()
    seen = {}
    for r, row in enumerate(GRID):
        for col, mid in enumerate(row):
            if mid is None:
                continue
            e = struct.unpack('<8H', meta[(mid - 0x200) * 16:(mid - 0x200) * 16 + 16])
            for k in range(4):
                v = e[4 + k]
                if v >> 12 != PAL:
                    continue
                tid, hf, vf = (v & 0x3ff) - 0x200, v >> 10 & 1, v >> 11 & 1
                x0, y0 = col * 16 + (k % 2) * 8, r * 16 + (k // 2) * 8
                cell = [[art[y0 + (7 - y if vf else y)][x0 + (7 - x if hf else x)] for x in range(8)] for y in range(8)]
                if tid in seen:
                    assert seen[tid] == cell, 'tile %x is shared but the drawing differs' % tid
                    continue
                seen[tid] = cell
                for y in range(8):
                    for x in range(8):
                        tp[(tid % tw) * 8 + x, (tid // tw) * 8 + y] = cell[y][x]
    tiles.save(os.path.join(ROOT, REL, 'tiles.png'))
    if '--preview' in sys.argv:
        pal = [tuple(map(int, l.split())) for l in open(os.path.join(ROOT, REL, 'palettes/%02d.pal' % PAL)).read().split('\n')[3:19]]
        im = Image.new('RGB', (48, 64), (64, 128, 200))
        for y in range(64):
            for x in range(48):
                if art[y][x]:
                    im.putpixel((x, y), pal[art[y][x]])
        im.resize((192, 256), Image.NEAREST).save(sys.argv[sys.argv.index('--preview') + 1])
    print('float homes: %d hut tiles redrawn' % len(seen))


main()
