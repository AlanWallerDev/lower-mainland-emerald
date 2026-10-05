#!/usr/bin/env python3
"""BC region map for the TrailNav and Fly screens, drawn from atlas/region_map.json.

Writes graphics/pokenav/region_map/map.png (tiles) and map.bin (64x64 affine tilemap),
src/data/region_map/region_map_layout.h (which section each grid cell belongs to), the x/y/size of
each section in region_map_sections.json, and the tile count in src/region_map.c.

Run from the repo root: python3 atlas/make_region_map.py [--preview out.png] (idempotent).
"""
import json
import os
import re
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
W, H = 28, 15          # section grid
OX, OY = 1, 2          # grid origin in the 64x64 tilemap (MAPCURSOR_X_MIN / Y_MIN)
BASE = 112             # palette slot: map.pal entry i is pixel index BASE + i

# Palette entries of map.pal (see the file); names for readability.
C = {
    'sea': 1, 'sea2': 2, 'lake': 3, 'searoute': 5, 'searoute2': 4, 'deep': 6,
    'green1': 10, 'green2': 11, 'green3': 12, 'green4': 13, 'green5': 14, 'khaki': 15,
    'white': 17, 'sand': 18, 'yellow': 19, 'orange': 20, 'gold': 21, 'amber': 22,
    'red': 25, 'darkred': 26, 'grey': 27, 'darkgrey': 28,
}

layout = json.load(open(P('atlas', 'region_map.json'), encoding='utf-8'))
terrain = layout['terrain']
assert len(terrain) == H and all(len(r) == W for r in terrain), 'terrain must be 28x15'
cell_sec = {}
for sec, cells in layout['sections'].items():
    for x, y in cells:
        assert (x, y) not in cell_sec, 'cell %d,%d used twice (%s, %s)' % (x, y, sec, cell_sec.get((x, y)))
        cell_sec[(x, y)] = sec


def kind(sec):
    if re.search(r'_(TOWN|CITY)$', sec):
        return 'city' if sec.endswith('_CITY') or len(layout['sections'][sec]) > 1 else 'town'
    return 'route' if 'ROUTE' in sec else 'place'


WATER = set('~l')
for (x, y), sec in cell_sec.items():
    t = terrain[y][x]
    if kind(sec) == 'route' and sec in ('MAPSEC_ROUTE_%d' % n for n in (103, 105, 106, 107, 108, 109, 122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134)):
        assert t in WATER, '%s at %d,%d should be sea, is %r' % (sec, x, y, t)
    elif kind(sec) in ('route', 'town', 'city') and sec != 'MAPSEC_SOUTHERN_ISLAND':
        assert t not in WATER, '%s at %d,%d should be land, is %r' % (sec, x, y, t)


def is_water(x, y):
    if 0 <= x < W and 0 <= y < H:
        return terrain[y][x] in WATER
    return True


# ---- one 8x8 cell of art -----------------------------------------------------------------
TEX = {
    'g': ('green2', 'green1'), 'f': ('green4', 'green3'), 'm': ('green5', 'darkgrey'),
    's': ('white', 'grey'), 'd': ('sand', 'yellow'), 'o': ('khaki', 'sand'),
}


def land_cell(t, x, y):
    a, b = TEX[t]
    px = [[C[a]] * 8 for _ in range(8)]
    if t == 'm' and (x + y) % 2:   # mountains: a peak on every other cell
        for r in range(8):
            for c in range(8):
                if (r * 3 + c * 5 + x) % 6 == 0:
                    px[r][c] = C['green4']
    elif t == 'm':
        for r in range(2, 7):
            for c in range(4 - (r - 1) // 2 - 1, 4 + (r - 1) // 2 + 1):
                px[r][c] = C['darkgrey'] if r > 3 else C['white']
    elif t == 's':
        for r in range(1, 7):
            for c in range(4 - r // 2, 4 + r // 2):
                px[r][c] = C['grey'] if r > 2 else C['white']
    else:
        for r in range(8):
            for c in range(8):
                if (r * 3 + c * 5 + x + y) % 7 == 0:
                    px[r][c] = C[b]
    return px


def water_cell(t, route=False):
    a, b = ('searoute', 'searoute2') if route else (('lake', 'sea') if t == 'l' else ('sea', 'sea2'))
    return [[C[a] if r % 2 == 0 else C[b]] * 8 for r in range(8)]


def coast(px, x, y):
    """Dark edge on land sides that face water."""
    edge = C['green5']
    if is_water(x, y - 1):
        px[0] = [edge] * 8
    if is_water(x, y + 1):
        px[7] = [edge] * 8
    for r in range(8):
        if is_water(x - 1, y):
            px[r][0] = edge
        if is_water(x + 1, y):
            px[r][7] = edge


def route_band(px, x, y, sec):
    same = lambda a, b: cell_sec.get((a, b)) == sec or (cell_sec.get((a, b)) and kind(cell_sec[(a, b)]) != 'route')
    col, rim = C['gold'], C['amber']
    for r in range(1, 7):
        for c in range(1, 7):
            px[r][c] = col if (r + c) % 4 else C['yellow']
    if same(x, y - 1):
        for r in range(0, 1):
            for c in range(1, 7):
                px[r][c] = col
    if same(x, y + 1):
        for c in range(1, 7):
            px[7][c] = col
    if same(x - 1, y):
        for r in range(1, 7):
            px[r][0] = col
    if same(x + 1, y):
        for r in range(1, 7):
            px[r][7] = col


def marker(px, shape, color, part=None):
    """Town dot, or one half of a city capsule (part: 'l','r','t','b')."""
    fill, dark = (C['red'], C['darkred']) if color == 'red' else (C['searoute'], C['deep'])
    for r in range(8):
        for c in range(8):
            if shape == 'dot':
                d = (r - 3.5) ** 2 + (c - 3.5) ** 2
                inside, rim = d <= 7.5, 7.5 < d <= 13
            else:
                rr, cc = (r, c) if part in ('l', 'r') else (c, r)
                end = part in ('l', 't')
                cc2 = cc if end else 7 - cc
                d = (rr - 3.5) ** 2 + max(0, 3.5 - cc2) ** 2
                inside, rim = d <= 7.5 and 1 <= rr <= 6, d <= 13 and not (d <= 7.5 and 1 <= rr <= 6)
            if inside:
                px[r][c] = fill
            elif rim:
                px[r][c] = dark
    hl = (2, 2) if shape == 'dot' or part in ('l', 't') else None
    if hl:
        px[hl[0]][hl[1]] = C['white']
        px[hl[0]][hl[1] + 1] = C['white']


def cell_art(x, y):
    t = terrain[y][x]
    sec = cell_sec.get((x, y))
    k = kind(sec) if sec else None
    if t in WATER:
        px = water_cell(t, route=(k == 'route'))
        if sec == 'MAPSEC_SOUTHERN_ISLAND':
            for r in range(3, 6):
                for c in range(2, 6):
                    px[r][c] = C['green3']
        return px
    px = land_cell(t, x, y)
    coast(px, x, y)
    if k == 'route':
        route_band(px, x, y, sec)
    elif k == 'town':
        marker(px, 'dot', 'blue')
    elif k == 'city':
        cells = layout['sections'][sec]
        if len(cells) == 1:
            marker(px, 'dot', 'red')
        else:
            (x0, y0), (x1, y1) = cells[0], cells[1]
            horiz = y0 == y1
            first = (x, y) == (min(x0, x1), y) if horiz else (x, y) == (x, min(y0, y1))
            marker(px, 'capsule', 'red', ('l' if first else 'r') if horiz else ('t' if first else 'b'))
    return px


# ---- compose the 64x64 tilemap, dedupe tiles ---------------------------------------------------
tiles, index, tilemap = [], {}, []
sea_px = water_cell('~')
for ty in range(64):
    for tx in range(64):
        gx, gy = tx - OX, ty - OY
        if 0 <= gx < W and 0 <= gy < H:
            px = cell_art(gx, gy)
        else:   # beyond BC: land next to the grid continues as Yukon, Alberta and the US
            ex, ey = min(max(gx, 0), W - 1), min(max(gy, 0), H - 1)
            near = abs(gx - ex) + abs(gy - ey) <= 3 and gx >= 0  # open Pacific to the west
            px = land_cell('o', gx, gy) if near and terrain[ey][ex] not in WATER else sea_px
        key = tuple(v for row in px for v in row)
        if key not in index:
            index[key] = len(tiles)
            tiles.append(key)
        tilemap.append(index[key])
assert len(tiles) <= 256, 'too many tiles: %d' % len(tiles)

orig = Image.open(P('graphics', 'pokenav', 'region_map', 'map.png'))
pal = orig.getpalette()
cols = 16
img = Image.new('P', (cols * 8, ((len(tiles) + cols - 1) // cols) * 8), 0)
img.putpalette(pal)
pix = img.load()
for i, t in enumerate(tiles):
    ox, oy = (i % cols) * 8, (i // cols) * 8
    for j, v in enumerate(t):
        pix[ox + j % 8, oy + j // 8] = BASE + v

if '--preview' in sys.argv:
    out = sys.argv[sys.argv.index('--preview') + 1]
    prev = Image.new('P', (240, 160))
    prev.putpalette(pal)
    pp = prev.load()
    for ty in range(20):
        for tx in range(30):
            t = tiles[tilemap[ty * 64 + tx]]
            for j, v in enumerate(t):
                pp[tx * 8 + j % 8, ty * 8 + j // 8] = BASE + v
    prev.convert('RGB').resize((720, 480), Image.NEAREST).save(out)
    print('preview written, %d tiles' % len(tiles))
    raise SystemExit(0)

img.save(P('graphics', 'pokenav', 'region_map', 'map.png'))
open(P('graphics', 'pokenav', 'region_map', 'map.bin'), 'wb').write(bytes(tilemap))

src = open(P('src', 'region_map.c'), encoding='utf-8').read()
src = re.sub(r'-num_tiles \d+ -Wnum_tiles', '-num_tiles %d -Wnum_tiles' % len(tiles), src)
open(P('src', 'region_map.c'), 'w', encoding='utf-8').write(src)

# ---- section grid and section positions ------------------------------------------------------------
rows = []
for y in range(H):
    rows.append('    {' + ', '.join(cell_sec.get((x, y), 'MAPSEC_NONE') for x in range(W)) + '},')
open(P('src', 'data', 'region_map', 'region_map_layout.h'), 'w', encoding='utf-8').write(
    '// Generated by atlas/make_region_map.py from atlas/region_map.json.\n'
    'static const mapsec_u8_t sRegionMap_MapSectionLayout[MAP_HEIGHT][MAP_WIDTH] = {\n' + '\n'.join(rows) + '\n};\n')

secs_path = P('src', 'data', 'region_map', 'region_map_sections.json')
secs = json.load(open(secs_path, encoding='utf-8'))
for e in secs['map_sections']:
    cells = layout['sections'].get(e['id'])
    if cells:
        xs, ys = [c[0] for c in cells], [c[1] for c in cells]
        if kind(e['id']) == 'route':  # routes: their first cell (fly and area markers use the box)
            e.update(x=min(xs), y=min(ys), width=max(xs) - min(xs) + 1, height=max(ys) - min(ys) + 1)
        else:
            e.update(x=min(xs), y=min(ys), width=max(xs) - min(xs) + 1, height=max(ys) - min(ys) + 1)
    elif e['id'] in layout['places']:
        x, y = layout['places'][e['id']]
        e.update(x=x, y=y, width=1, height=1)
with open(secs_path, 'w', encoding='utf-8') as f:
    json.dump(secs, f, indent=2, ensure_ascii=False)
    f.write('\n')
print('region map: %d tiles, %d sections' % (len(tiles), len(layout['sections'])))
