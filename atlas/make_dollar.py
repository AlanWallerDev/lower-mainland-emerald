#!/usr/bin/env python3
"""Canadian dollars: redraws the currency glyph (charmap ¥, 0xB7) in every Latin font as a $ sign,
made from that font's own S with a vertical stroke through it. Prices then read $300. The glyph
widths stay as they are (each ¥ cell is at least as wide as the S).

Starts from upstream (needs the pret `upstream` remote), so it is idempotent.
Run from the repo root: python3 atlas/make_dollar.py
"""
import io
import os
import re
import subprocess

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = {'latin_normal': 'Normal', 'latin_small': 'Small', 'latin_short': 'Short', 'latin_narrow': 'Narrow',
         'latin_small_narrow': 'SmallNarrow'}
YEN, S = 0xB7, 0xCD
BG, INK, SHADOW = 3, 1, 2   # palette indices: white cell, dark ink, grey shadow


SRC = open(os.path.join(ROOT, 'src', 'fonts.c')).read()


def s_width(font):
    """Drawn width of S in this font (pixels past it in the sheet are never shown)."""
    body = re.search(r'gFont%sLatinGlyphWidths\[\] = \{(.*?)\};' % font, SRC, re.S).group(1)
    return [int(x, 0) for x in re.findall(r'0x[0-9a-fA-F]+|\d+', body)][S]


def cell(c):
    return (c % 16) * 16, (c // 16) * 16


for name, font in FONTS.items():
    sw = s_width(font)
    rel = 'graphics/fonts/%s.png' % name
    data = subprocess.run(['git', 'show', 'upstream/master:' + rel], cwd=ROOT, capture_output=True, check=True).stdout
    im = Image.open(io.BytesIO(data))
    px = im.load()
    sx, sy = cell(S)
    yx, yy = cell(YEN)
    # Clear the yen glyph to the cell background, then copy the S's ink and shadow.
    for y in range(16):
        for x in range(16):
            if px[yx + x, yy + y] in (INK, SHADOW):
                px[yx + x, yy + y] = BG
    ink = [(x, y) for y in range(16) for x in range(sw) if px[sx + x, sy + y] == INK]
    for y in range(16):
        for x in range(sw + 1):
            if px[sx + x, sy + y] in (INK, SHADOW):
                px[yx + x, yy + y] = px[sx + x, sy + y]
    # Vertical stroke through the middle of the S, one pixel past its top and bottom.
    xs = [x for x, _ in ink]
    ys = [y for _, y in ink]
    mid = (min(xs) + max(xs)) // 2
    for y in range(max(0, min(ys) - 1), min(15, max(ys) + 1) + 1):
        px[yx + mid, yy + y] = INK
        if mid + 1 < 16 and px[yx + mid + 1, yy + y] == BG:
            px[yx + mid + 1, yy + y] = SHADOW
    if max(ys) + 2 < 16 and px[yx + mid, yy + max(ys) + 2] == BG:
        px[yx + mid, yy + max(ys) + 2] = SHADOW
    im.save(os.path.join(ROOT, rel))
print('dollar: currency glyph redrawn as $ in %d fonts' % len(FONTS))
