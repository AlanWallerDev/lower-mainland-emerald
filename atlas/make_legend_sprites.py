#!/usr/bin/env python3
"""Overworld sprites for the three story legendaries, drawn from their battle sprites (written by
make_sprites.py), so the DEEP COVE clash, the hideouts and the STAWAMUS CHIEF show the organisms the
dialogue names:

- GROUDON slot (spirit bear) and KYOGRE slot (glass sponge reef): four 32x32 frames each
  (graphics/object_events/pics/pokemon/groudon.png, kyogre.png) with their own palettes and
  water-reflection palettes. Frames 1 and 3 bob a pixel so the idle animation stays alive.
- RAYQUAZA slot (marbled murrelet): five 64x64 frames plus the still frame. Its palette (NPC_3)
  is shared with townsfolk, so the murrelet is mapped onto that palette's existing colours.
  The last frame (Rayquaza rising) is the bird lifted 8 pixels.

Run after atlas/make_sprites.py: python3 atlas/make_legend_sprites.py [--preview out.png]
"""
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
OW = 'graphics/object_events/'


def read_pal(path):
    v = open(P(path)).read().split()[3:]
    return [tuple(map(int, v[i * 3:i * 3 + 3])) for i in range(16)]


def write_pal(path, cols):
    with open(P(path), 'w', newline='\r\n') as f:
        f.write('JASC-PAL\n0100\n16\n' + ''.join('%d %d %d\n' % c for c in cols))


def battle_rgba(slot):
    """First frame of the slot's battle sprite as RGBA, background (index 0) transparent."""
    im = Image.open(P('graphics/pokemon', slot, 'anim_front.png'))
    im = im.crop((0, 0, 64, 64))
    pal = im.getpalette()
    out = Image.new('RGBA', (64, 64))
    src, dst = im.load(), out.load()
    for y in range(64):
        for x in range(64):
            i = src[x, y]
            if i:
                dst[x, y] = tuple(pal[i * 3:i * 3 + 3]) + (255,)
    return out


def fit(rgba, size, pad):
    """Crop to the sprite and scale it to fit size x size (keeping pad pixels clear), bottom-aligned."""
    box = rgba.getbbox()
    spr = rgba.crop(box)
    k = min((size - pad) / spr.width, (size - pad) / spr.height, 1.0)
    w, h = max(1, round(spr.width * k)), max(1, round(spr.height * k))
    spr = spr.resize((w, h), Image.LANCZOS)
    out = Image.new('RGBA', (size, size))
    out.alpha_composite(spr, ((size - w) // 2, size - h - pad // 2))
    return out


def nearest(c, cols, allowed=None):
    pool = allowed or range(1, len(cols))
    return min(pool, key=lambda i: sum((a - b) ** 2 for a, b in zip(c, cols[i])))


def to_indexed(rgba, cols, allowed=None):
    out = Image.new('P', rgba.size)
    out.putpalette([v for c in cols for v in c])
    s, d = rgba.load(), out.load()
    for y in range(rgba.height):
        for x in range(rgba.width):
            r, g, b, a = s[x, y]
            d[x, y] = nearest((r, g, b), cols, allowed) if a >= 128 else 0
    return out


def own_palette(rgba, key):
    """A 15-colour palette for the sprite, with the transparent key colour in index 0."""
    q = rgba.convert('RGB').quantize(colors=16)
    alpha = rgba.getchannel('A').load()
    used = {}
    qp, qpal = q.load(), q.getpalette()
    for y in range(rgba.height):
        for x in range(rgba.width):
            if alpha[x, y] >= 128:
                used[qp[x, y]] = used.get(qp[x, y], 0) + 1
    cols = [tuple(qpal[i * 3:i * 3 + 3]) for i, _ in sorted(used.items(), key=lambda kv: -kv[1])][:15]
    cols = [key] + cols
    while len(cols) < 16:
        cols.append((0, 0, 0))
    return cols


def shifted(im, dy):
    out = Image.new('P', im.size)
    out.putpalette(im.getpalette())
    out.paste(im.crop((0, max(0, -dy), im.width, im.height - max(0, dy))), (0, max(0, dy)))
    return out


def strip(frames):
    out = Image.new('P', (sum(f.width for f in frames), frames[0].height))
    out.putpalette(frames[0].getpalette())
    x = 0
    for f in frames:
        out.paste(f, (x, 0))
        x += f.width
    return out


made = []
for slot in ('groudon', 'kyogre'):
    key = read_pal(OW + 'palettes/%s.pal' % slot)[0]
    spr = fit(battle_rgba(slot), 32, 2)
    cols = own_palette(spr, key)
    frame = to_indexed(spr, cols)
    strip([frame, shifted(frame, 1), frame, shifted(frame, 1)]).save(P(OW, 'pics/pokemon/%s.png' % slot))
    write_pal(OW + 'palettes/%s.pal' % slot, cols)
    # Reflections are drawn darker and bluer, like upstream's.
    refl = [cols[0]] + [(int(r * 0.6), int(g * 0.6), min(255, int(b * 0.6) + 40)) for r, g, b in cols[1:]]
    write_pal(OW + 'palettes/%s_reflection.pal' % slot, refl)
    made.append(frame)

npc3 = read_pal(OW + 'palettes/npc_3.pal')
# Leave out NPC_3's greens (a dark-brown seabird would otherwise turn green).
earthy = [i for i in range(1, 16) if not (npc3[i][1] > npc3[i][0] + 30 and npc3[i][1] > npc3[i][2] + 30)]
bird = to_indexed(fit(battle_rgba('rayquaza'), 64, 8), npc3, earthy)
strip([bird, bird, bird, shifted(bird, -2), shifted(bird, -8)]).save(P(OW, 'pics/pokemon/rayquaza.png'))
bird.save(P(OW, 'pics/pokemon/rayquaza_still.png'))
made.append(bird)

if '--preview' in sys.argv:
    prev = Image.new('RGB', (160, 64), (115, 197, 164))
    x = 0
    for m in made:
        prev.paste(m.convert('RGB'), (x, 0))
        x += m.width + 8
    prev.resize((640, 256), Image.NEAREST).save(sys.argv[sys.argv.index('--preview') + 1])
print('legend sprites: bear, reef and murrelet overworld sprites written')
