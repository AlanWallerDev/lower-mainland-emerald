#!/usr/bin/env python3
"""PC storage menu (graphics/pokemon_storage/menu.png): the header PKMN DATA becomes DATA (the PKMN
plate is dropped and DATA's plate centred) and the button PARTY POKéMON becomes PARTY.

Starts from upstream (needs the pret `upstream` remote), so it is idempotent.
Run from the repo root: python3 atlas/make_pc_menu.py
"""
import io
import os
import subprocess

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REL = 'graphics/pokemon_storage/menu.png'
data = subprocess.run(['git', 'show', 'upstream/master:' + REL], cwd=ROOT, capture_output=True, check=True).stdout
img = Image.open(io.BytesIO(data))
px = img.load()

# Header plates on rows 4-12: PKMN at x 14-40, DATA at x 41-66, on the header grey.
block = [[px[x, y] for x in range(41, 67)] for y in range(4, 13)]
for y in range(4, 13):
    bg = px[13, y]  # header grey just left of the plates (keeps its palette bank)
    for x in range(14, 67):
        px[x, y] = bg
left = 14 + (53 - 26) // 2
for dy, row in enumerate(block):
    for dx, v in enumerate(row):
        px[left + dx, 4 + dy] = v

# Button text on rows 20-27: PARTY ends at x 92, POKéMON fills x 96-127; on the button face.
for y in range(20, 28):
    for x in range(94, 128):
        px[x, y] = px[x, 18]  # the button face above the text, same column and palette bank
img.save(os.path.join(ROOT, REL))
print('pc menu: DATA header, PARTY button')
