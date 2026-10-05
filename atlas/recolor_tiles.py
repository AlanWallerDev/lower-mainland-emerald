#!/usr/bin/env python3
"""Recolour the overworld tilesets for BC (atlas/recolor.json): every tileset palette is rebuilt
from upstream with exact colours swapped, so neighbouring tilesets keep matching edges.

Run from the repo root: python3 atlas/recolor_tiles.py (idempotent; needs the pret `upstream` remote).
"""
import glob
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg = json.load(open(os.path.join(ROOT, 'atlas', 'recolor.json'), encoding='utf-8'))['colors']
cmap = {tuple(map(int, k.split(','))): tuple(map(int, v.split(','))) for k, v in cfg.items() if not k.startswith('_')}

files = sorted(glob.glob(os.path.join(ROOT, 'data', 'tilesets', '**', 'palettes', '*.pal'), recursive=True))
changed = 0
for f in files:
    rel = os.path.relpath(f, ROOT)
    src = subprocess.run(['git', 'show', 'upstream/master:' + rel], cwd=ROOT, capture_output=True).stdout.decode()
    if not src:
        continue
    lines = src.replace('\r\n', '\n').split('\n')
    out = lines[:3]
    for line in lines[3:]:
        parts = line.split()
        if len(parts) == 3:
            c = tuple(map(int, parts))
            if c in cmap:
                c = cmap[c]
                changed += 1
            out.append('%d %d %d' % c)
        elif line:
            out.append(line)
    with open(f, 'w', newline='\r\n') as fh:
        fh.write('\n'.join(out) + '\n')
print('recolor: %d palette files, %d colours swapped' % (len(files), changed))
