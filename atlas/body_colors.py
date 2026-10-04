#!/usr/bin/env python3
"""Sets each species' bodyColor (used by the Field Journal colour search) from its front sprite:
the most common non-transparent colour, matched to the nearest of the ten body colours.

Run from the repo root after atlas/make_sprites.py: python3 atlas/body_colors.py (idempotent).
"""
import json
import os
import re

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)

COLORS = {
    'RED': (200, 50, 40), 'BLUE': (50, 90, 200), 'YELLOW': (230, 200, 50), 'GREEN': (60, 150, 60),
    'BLACK': (35, 35, 40), 'BROWN': (130, 85, 45), 'PURPLE': (130, 70, 160), 'GRAY': (140, 140, 140),
    'WHITE': (235, 235, 235), 'PINK': (235, 140, 170),
}


def body_color(png):
    img = Image.open(png)
    pal = img.getpalette()
    counts = {}
    for i in img.get_flattened_data() if hasattr(img, 'get_flattened_data') else img.getdata():
        if i:
            counts[i] = counts.get(i, 0) + 1
    if not counts:
        return 'GRAY'
    # The darkest colour is usually the outline: skip it unless it is most of the sprite.
    lum = lambda i: sum(pal[i * 3:i * 3 + 3])
    darkest = min(counts, key=lum)
    if len(counts) > 1 and counts[darkest] < 0.5 * sum(counts.values()):
        del counts[darkest]
    top = max(counts, key=counts.get)
    rgb = tuple(pal[top * 3:top * 3 + 3])
    return min(COLORS, key=lambda c: sum((a - b) ** 2 for a, b in zip(rgb, COLORS[c])))


smap = json.load(open(P('atlas', 'species_map.json'), encoding='utf-8'))
path = P('src', 'data', 'pokemon', 'species_info.h')
src = open(path, encoding='utf-8').read()
for e in smap:
    png = P('graphics', 'pokemon', e['slot'].lower(), 'front.png')
    if not os.path.exists(png):
        continue
    color = body_color(png)
    src = re.sub(r'(\[SPECIES_%s\] =\s*\{[^\[]*?\.bodyColor = )BODY_COLOR_\w+' % e['slot'],
                 lambda m: m.group(1) + 'BODY_COLOR_' + color, src, count=1)
open(path, 'w', encoding='utf-8').write(src)
print('body colours set')
