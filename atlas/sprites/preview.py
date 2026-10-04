#!/usr/bin/env python3
"""Contact sheet of species art: python3 -m atlas.sprites.preview out.png [ids... | group:Mammal | bc | all]"""
import json
import os
import sys

from PIL import Image, ImageDraw

from . import registry

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
species = {s['id']: s for s in json.load(open(os.path.join(ROOT, 'atlas', 'data', 'species.json')))}
bc_file = os.path.join(ROOT, 'atlas', 'bc_species.json')
if os.path.exists(bc_file):
    species.update({s['id']: s for s in json.load(open(bc_file))['species']})
smap = json.load(open(os.path.join(ROOT, 'atlas', 'species_map.json')))

out, args = sys.argv[1], sys.argv[2:]
ids = []
for a in args:
    if a.startswith('group:'):
        g = a[6:]
        ids += [o['id'] for o in smap if species[o['id']]['group'] == g]
    elif a == 'bc':
        ids += sorted(k for k in species if k.startswith('bc-'))
    elif a == 'all':
        ids += [o['id'] for o in smap]
    else:
        ids.append(a)
ids = [i for i in ids if i in registry.SPECS]
cols = 8
cell_w, cell_h = 64 * 2 + 8, 64 * 2 + 22
rows = (len(ids) + cols - 1) // cols
sheet = Image.new('RGB', (cols * cell_w, max(1, rows) * cell_h), (255, 255, 255))
d = ImageDraw.Draw(sheet)
for i, sid in enumerate(ids):
    im = registry.draw(sid)
    pal, _ = registry.palettes(sid)
    im.putpalette([v for c in pal for v in c])
    x, y = (i % cols) * cell_w, (i // cols) * cell_h
    sheet.paste(im.convert('RGB').resize((128, 128), Image.NEAREST), (x + 4, y + 2))
    d.text((x + 4, y + 132), species[sid]['name'][:22], fill=(0, 0, 0))
sheet.save(out)
print(len(ids), 'drawn')
