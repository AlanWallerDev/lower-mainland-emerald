#!/usr/bin/env python3
"""FIELD JOURNAL screens: text baked into the Journal's graphics.

- graphics/pokedex/menu.png: the POKéDEX title becomes JOURNAL (copied from the search screen's
  title, already JOURNAL) and the menu rows BACK TO POKéDEX / CLOSE POKéDEX are redrawn in the
  game's normal font as BACK TO JOURNAL / CLOSE JOURNAL.
- graphics/pokedex/interface.png: the HOENN list label becomes BC (tiny 7px font, ink with a
  shadow to the right and below).

Starts from upstream's menu.png and interface.png (needs the pret `upstream` remote), so it is
idempotent. Run from the repo root: python3 atlas/make_journal_ui.py
"""
import io
import os
import re
import subprocess

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)


def upstream(rel):
    data = subprocess.run(['git', 'show', 'upstream/master:' + rel], cwd=ROOT, capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(data))


# ---- menu.png -----------------------------------------------------------------------------------
menu = upstream('graphics/pokedex/menu.png')
mp = menu.load()
search = Image.open(P('graphics/pokedex/search_menu.png')).load()
for y in range(8, 16):  # title row: search screen white (3) is menu white (1); black and edges match
    for x in range(0, 118):
        v = search[x, y]
        mp[x, y] = {3: 1}.get(v, v)

charmap = {}
for line in open(P('charmap.txt'), encoding='utf-8'):
    m = re.match(r"^'(.)'\s*=\s*([0-9A-F]{2})\s*$", line)
    if m:
        charmap[m.group(1)] = int(m.group(2), 16)
src = open(P('src/fonts.c')).read()
widths = [int(v, 0) for v in re.findall(r'0x[0-9a-fA-F]+|\d+',
          re.search(r'gFontNormalLatinGlyphWidths\[\] = \{(.*?)\};', src, re.S).group(1))]
font = Image.open(P('graphics/fonts/latin_normal.png')).load()
INK = {1: 9, 2: 5}  # font ink / shadow -> menu text colours; the rest is the menu's green (d)


def write(text, x, top):
    """Draw text with the normal font; glyph rows 3-12 land on rows top..top+9."""
    for ch in text:
        c = charmap[ch]
        gx, gy = (c % 16) * 16, (c // 16) * 16
        for y in range(3, 13):
            for dx in range(widths[c]):
                v = font[gx + dx, gy + y]
                mp[x + dx, top + y - 3] = INK.get(v, 0xd)
        x += widths[c]


for top, x0, text in ((99, 0, 'BACK TO JOURNAL'), (115, 1, 'CLOSE JOURNAL')):
    for y in range(top, top + 10):
        for x in range(0, 88):
            mp[x, y] = 0xd
    write(text, x0, top)
menu.save(P('graphics/pokedex/menu.png'))

# ---- interface.png ------------------------------------------------------------------------------
iface = upstream('graphics/pokedex/interface.png')
ip = iface.load()
GLYPHS = {'B': ['11.', '1.1', '1.1', '11.', '1.1', '1.1', '11.'],
          'C': ['.11', '1..', '1..', '1..', '1..', '1..', '.11']}
for y in range(324, 332):
    for x in range(0, 27):
        ip[x, y] = 0
x = 0
for ch in 'BC':
    for gy, row in enumerate(GLYPHS[ch]):
        for gx, c in enumerate(row):
            if c == '1':
                ip[x + gx, 324 + gy] = 1
    x += 4
for y in range(331, 323, -1):  # shadow to the right and below each ink pixel
    for x in range(26, -1, -1):
        if ip[x, y] == 1:
            for sx, sy in ((x + 1, y), (x, y + 1)):
                if ip[sx, sy] == 0:
                    ip[sx, sy] = 0xf
iface.save(P('graphics/pokedex/interface.png'))
print('journal ui: menu title and rows, BC list label')
