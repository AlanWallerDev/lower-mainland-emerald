#!/usr/bin/env python3
"""TrailNav close-up legend: the ticker under a zoomed-in town map (graphics/pokenav/region_map/
city_zoom_text.png). It is one 512px ribbon cut into 64 tiles (8 per sheet row) that three 32x8
sprites scroll through, pausing on each 96px page. Upstream's pages read POKéMON CENTER, POKé MART,
POKéMON GYM, BATTLE TENT and POKéMON CONTEST; this redraws them in the same tiny 6px font and
colours as FIELD STATION, MART, GYM, BATTLE TENT and CONTEST HALL.

Idempotent (keeps the PNG's palette). Run from the repo root: python3 atlas/make_zoom_text.py
"""
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'graphics/pokenav/region_map/city_zoom_text.png')

FONT = {
    'A': ['.##.', '#..#', '#..#', '####', '#..#', '#..#'],
    'B': ['###.', '#..#', '###.', '#..#', '#..#', '###.'],
    'C': ['.##.', '#..#', '#...', '#...', '#..#', '.##.'],
    'D': ['###.', '#..#', '#..#', '#..#', '#..#', '###.'],
    'E': ['####', '#...', '###.', '#...', '#...', '####'],
    'F': ['####', '#...', '###.', '#...', '#...', '#...'],
    'G': ['.##.', '#..#', '#...', '#.##', '#..#', '.###'],
    'H': ['#..#', '#..#', '####', '#..#', '#..#', '#..#'],
    'I': ['###', '.#.', '.#.', '.#.', '.#.', '###'],
    'L': ['#...', '#...', '#...', '#...', '#...', '####'],
    'M': ['#...#', '##.##', '#.#.#', '#...#', '#...#', '#...#'],
    'N': ['#..#', '##.#', '#.##', '#..#', '#..#', '#..#'],
    'O': ['.##.', '#..#', '#..#', '#..#', '#..#', '.##.'],
    'R': ['###.', '#..#', '#..#', '###.', '#..#', '#..#'],
    'S': ['.###', '#...', '.##.', '...#', '...#', '###.'],
    'T': ['#####', '..#..', '..#..', '..#..', '..#..', '..#..'],
    'Y': ['#...#', '.#.#.', '..#..', '..#..', '..#..', '..#..'],
    ' ': ['..', '..', '..', '..', '..', '..'],
}
# (label, palette index) per 96px page, in upstream's order and colours.
PAGES = [('FIELD STATION', 3), ('MART', 5), ('GYM', 15), ('BATTLE TENT', 2), ('CONTEST HALL', 4)]

old = Image.open(PATH)
ribbon = [[0] * 512 for _ in range(8)]
for page, (label, colour) in enumerate(PAGES):
    x0 = page * 96
    for y in range(1, 7):
        for x in range(7, 13):
            ribbon[y][x0 + x] = colour
    x = x0 + 14
    for ch in label:
        glyph = FONT[ch]
        for y, row in enumerate(glyph):
            for dx, c in enumerate(row):
                if c == '#':
                    ribbon[1 + y][x + dx] = colour
        x += len(glyph[0]) + 1
    assert x <= x0 + 96, label + ' is too wide for its page'

sheet = Image.new('P', (64, 64))
sheet.putpalette(old.getpalette())
sp = sheet.load()
for t in range(64):
    for y in range(8):
        for x in range(8):
            v = ribbon[y][t * 8 + x]
            sp[(t % 8) * 8 + x, (t // 8) * 8 + y] = v  # 0 is the black background
sheet.save(PATH)
print('zoom text: TrailNav legend redrawn')
