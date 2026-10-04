#!/usr/bin/env python3
"""Title logo for Pokémon BC: keeps the original Pokémon wordmark and replaces the
"EMERALD VERSION" banner with "BC", drawn in the banner's own palette.

Run from the repo root: python3 atlas/make_title.py
Needs the pret remote: git remote add upstream https://github.com/pret/pokeemerald && git fetch upstream master
"""
import os
import subprocess

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TITLE_DIR = os.path.join(ROOT, 'graphics', 'title_screen')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
TEXT = 'BC'


def upstream(name):
    """Load a title-screen image from upstream so reruns are stable."""
    img = Image.open(subprocess.Popen(['git', 'show', 'upstream/master:graphics/title_screen/' + name],
                                      cwd=ROOT, stdout=subprocess.PIPE).stdout)
    img.load()
    return img


# The wordmark is the original one.
upstream('pokemon_logo.png').save(os.path.join(TITLE_DIR, 'pokemon_logo.png'))

# The banner: white letters with grey shading and a dark outline, like "EMERALD VERSION".
orig = upstream('emerald_version.png')
pal = orig.getpalette()
W, H = orig.size
WHITE, LIGHT, SHADE, OUTLINE = 15, 6, 12, 4  # palette indices in emerald_version.png

font = ImageFont.truetype(FONT, 30)
mask = Image.new('L', (W, H), 0)
d = ImageDraw.Draw(mask)
left, top, right, bottom = d.textbbox((0, 0), TEXT, font=font)
d.text(((W - (right - left)) / 2 - left, (H - (bottom - top)) / 2 - top), TEXT, font=font, fill=255)
mask = mask.point(lambda v: 255 if v >= 128 else 0)
outline = mask.filter(ImageFilter.MaxFilter(5))

out = Image.new('P', (W, H), 0)
out.putpalette(pal)
m, o, px = mask.load(), outline.load(), out.load()
ys = [y for y in range(H) for x in range(W) if m[x, y]]
top_y, bot_y = min(ys), max(ys)
for y in range(H):
    t = (y - top_y) / max(1, bot_y - top_y)
    fill = WHITE if t < 0.45 else LIGHT if t < 0.75 else SHADE
    for x in range(W):
        if m[x, y]:
            px[x, y] = fill
        elif o[x, y]:
            px[x, y] = OUTLINE
out.save(os.path.join(TITLE_DIR, 'emerald_version.png'))
print('title logo written')
