#!/usr/bin/env python3
"""Title logo: replaces the Pokémon wordmark with "LOWER MAINLAND", drawn in the original logo's palette.

Run from the repo root: python3 atlas/make_title.py
"""
import os
import subprocess

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(ROOT, 'graphics', 'title_screen', 'pokemon_logo.png')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

# Start from the upstream image so reruns are stable, and keep its palette.
orig = Image.open(subprocess.Popen(['git', 'show', 'upstream/master:graphics/title_screen/pokemon_logo.png'],
                                   cwd=ROOT, stdout=subprocess.PIPE).stdout)
orig.load()
pal = orig.getpalette()
used = sorted(set(orig.getdata()))

W, H = orig.size
YELLOW, GOLD, BLUE, NAVY = (255, 222, 41), (222, 164, 24), (49, 98, 205), (24, 41, 115)


# The title screen shows this image off-centre: the original wordmark spans x 3-168, centre ~86.
CENTER_X, MAX_W = 86, 160


def text_layer(text, size, y):
    font = ImageFont.truetype(FONT, size)
    d = ImageDraw.Draw(Image.new('L', (W, H)))
    while d.textlength(text, font=font) > MAX_W:
        size -= 1
        font = ImageFont.truetype(FONT, size)
    mask = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(mask)
    w = d.textlength(text, font=font)
    d.text((CENTER_X - w / 2, y), text, font=font, fill=255)
    return mask


mask = Image.new('L', (W, H), 0)
for layer in (text_layer('LOWER', 26, 0), text_layer('MAINLAND', 30, 28)):
    mask = Image.composite(Image.new('L', (W, H), 255), mask, layer)

rgb = Image.new('RGB', (W, H), (0, 0, 0))
outer = mask.filter(ImageFilter.MaxFilter(7))
inner = mask.filter(ImageFilter.MaxFilter(3))
rgb.paste(NAVY, mask=outer)
rgb.paste(BLUE, mask=inner)
# Vertical gold-to-yellow fill inside the letters.
grad = Image.new('RGB', (W, H))
for y in range(H):
    t = (y % 28) / 28
    grad.paste(tuple(int(YELLOW[i] * (1 - t) + GOLD[i] * t) for i in range(3)), (0, y, W, y + 1))
rgb.paste(grad, mask=mask)

# Map to the nearest color among the palette entries the original uses; black stays index 0.
cols = [(i, tuple(pal[i * 3:i * 3 + 3])) for i in used if i != 0]
out = Image.new('P', (W, H), 0)
out.putpalette(pal)
src = rgb.load()
dst = out.load()
cache = {}
outer_px = outer.load()
for y in range(H):
    for x in range(W):
        if not outer_px[x, y]:
            continue
        c = src[x, y]
        if c not in cache:
            cache[c] = min(cols, key=lambda e: sum((a - b) ** 2 for a, b in zip(c, e[1])))[0]
        dst[x, y] = cache[c]
out.save(LOGO)
print('title logo written')
