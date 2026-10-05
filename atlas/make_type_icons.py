#!/usr/bin/env python3
"""Type icons (graphics/interface/menu_info.png): the coloured 32x12 type labels on the summary,
Journal and shop screens still read NORMAL, FIRE, WATER... This relabels them with the hack's
type names (COMMON, EMBER, AQUA, VERDANT, CHARM, STONE, SOIL, FROST, SKY, BRAWN, CHITIN, TOXIN,
MIND, ARMOR, NIGHT; the unused Ghost and Dragon slots read -----) in a narrow 7px font so the long
names fit: white ink (f) with a dark shadow (e) to the right and below, on each cell's own colours.

Starts from upstream (needs the pret `upstream` remote), so it is idempotent.
Run from the repo root: python3 atlas/make_type_icons.py [--preview out.png]
"""
import io
import os
import subprocess
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REL = 'graphics/interface/menu_info.png'
INK, SHADOW = 0xf, 0xe

# Upstream's grid: (row, column) of each 32x12 type cell, cells 16 px apart from y = 16.
NAMES = {
    (0, 0): 'COMMON', (0, 1): 'EMBER', (0, 2): 'AQUA', (0, 3): 'VERDANT',
    (1, 0): 'CHARM', (1, 1): 'STONE', (1, 2): 'SOIL', (1, 3): 'FROST',
    (2, 0): 'SKY', (2, 1): 'BRAWN', (2, 2): '-----', (2, 3): 'CHITIN',
    (3, 0): 'TOXIN', (3, 1): 'MIND', (3, 2): 'ARMOR', (3, 3): 'NIGHT',
    (4, 0): '-----',
}
FONT = {
    'A': ['.#.', '#.#', '#.#', '###', '#.#', '#.#', '#.#'],
    'B': ['##.', '#.#', '#.#', '##.', '#.#', '#.#', '##.'],
    'C': ['.##', '#..', '#..', '#..', '#..', '#..', '.##'],
    'D': ['##.', '#.#', '#.#', '#.#', '#.#', '#.#', '##.'],
    'E': ['###', '#..', '#..', '##.', '#..', '#..', '###'],
    'F': ['###', '#..', '#..', '##.', '#..', '#..', '#..'],
    'G': ['.##', '#..', '#..', '#.#', '#.#', '#.#', '.##'],
    'H': ['#.#', '#.#', '#.#', '###', '#.#', '#.#', '#.#'],
    'I': ['###', '.#.', '.#.', '.#.', '.#.', '.#.', '###'],
    'K': ['#.#', '#.#', '##.', '#..', '##.', '#.#', '#.#'],
    'L': ['#..', '#..', '#..', '#..', '#..', '#..', '###'],
    'M': ['#...#', '##.##', '#.#.#', '#...#', '#...#', '#...#', '#...#'],
    'N': ['#..#', '##.#', '##.#', '#.##', '#.##', '#..#', '#..#'],
    'O': ['.#.', '#.#', '#.#', '#.#', '#.#', '#.#', '.#.'],
    'Q': ['.#.', '#.#', '#.#', '#.#', '#.#', '##.', '.##'],
    'R': ['##.', '#.#', '#.#', '##.', '#.#', '#.#', '#.#'],
    'S': ['.##', '#..', '#..', '.#.', '..#', '..#', '##.'],
    'T': ['###', '.#.', '.#.', '.#.', '.#.', '.#.', '.#.'],
    'U': ['#.#', '#.#', '#.#', '#.#', '#.#', '#.#', '.#.'],
    'V': ['#.#', '#.#', '#.#', '#.#', '#.#', '.#.', '.#.'],
    'W': ['#...#', '#...#', '#...#', '#.#.#', '#.#.#', '##.##', '#...#'],
    'X': ['#.#', '#.#', '.#.', '.#.', '.#.', '#.#', '#.#'],
    'Y': ['#.#', '#.#', '.#.', '.#.', '.#.', '.#.', '.#.'],
    '-': ['...', '...', '...', '###', '...', '...', '...'],
}

data = subprocess.run(['git', 'show', 'upstream/master:' + REL], cwd=ROOT, capture_output=True, check=True).stdout
img = Image.open(io.BytesIO(data))
px = img.load()

for (row, col), name in NAMES.items():
    x0, y0 = col * 32, 16 + row * 16
    # Each text row's background is the cell's own colour on that row (some cells are two-tone);
    # the cell's left edge column carries it even where a label fills the whole row.
    for y in range(y0 + 2, y0 + 10):
        bg = px[x0, y]
        for x in range(x0 + 1, x0 + 31):
            px[x, y] = bg
    width = sum(len(FONT[c][0]) + 1 for c in name)
    assert width <= 31, name
    x = x0 + 1 + (31 - width) // 2
    ink = []
    for c in name:
        for gy, line in enumerate(FONT[c]):
            for gx, v in enumerate(line):
                if v == '#':
                    ink.append((x + gx, y0 + 2 + gy))
        x += len(FONT[c][0]) + 1
    base = px[x0 + 16, y0 + 1] - px[x0 + 16, y0 + 1] % 16  # palette bank of this cell (multiples of 16)
    for p in ink:
        px[p] = base + INK
    for (ix, iy) in ink:
        for p in ((ix + 1, iy), (ix, iy + 1)):
            if p not in ink and px[p] % 16 not in (INK,):
                px[p] = base + SHADOW

img.save(os.path.join(ROOT, REL))
if '--preview' in sys.argv:
    img.convert('RGB').crop((0, 16, 128, 92)).resize((512, 304), Image.NEAREST).save(sys.argv[sys.argv.index('--preview') + 1])
print('type icons: %d labels redrawn' % len(NAMES))
