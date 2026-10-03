#!/usr/bin/env python3
"""Stand-in sprites for every organism: front, animated front, back, icon, footprint and palettes.

Each organism is drawn from its own art spec (atlas/sprites/specs_*.py): a body rig with real colours
and markings, rendered by atlas/sprites/engine.py. Run from the repo root: python3 atlas/make_sprites.py
Preview a contact sheet: python3 -m atlas.sprites.preview out.png all
"""
import json
import os
import re
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from atlas.sprites import registry  # noqa: E402

P = lambda *a: os.path.join(ROOT, *a)


def read(p):
    with open(P(p), encoding='utf-8') as f:
        return f.read()


def write(p, s):
    with open(P(p), 'w', encoding='utf-8') as f:
        f.write(s)


species = {s['id']: s for s in json.load(open(P('atlas', 'data', 'species.json'), encoding='utf-8'))}
smap = json.load(open(P('atlas', 'species_map.json'), encoding='utf-8'))


def draw(s, back=False):
    im = registry.draw(s['id'], back=back)
    if im is None:
        raise SystemExit('no art spec for %s (%s)' % (s['id'], s['name']))
    return im


def palette_for(s, shiny=False):
    normal, sh = registry.palettes(s['id'])
    return sh if shiny else normal


def write_pal(path, pal):
    with open(path, 'w', newline='\r\n') as f:
        f.write('JASC-PAL\n0100\n16\n' + ''.join('%d %d %d\n' % c for c in pal))


def with_pal(im, pal):
    im = im.copy()
    im.putpalette([v for c in pal for v in c])
    return im


def bob(im, dy):
    """Second animation frame: the body shifted down a pixel."""
    out = Image.new('P', im.size, 0)
    out.paste(im, (0, dy))
    out.putpalette(im.getpalette())
    return out


# ---- icon palettes are shared; pick the closest of the three and remap to it.
def read_pal(path):
    lines = open(path).read().split()
    return [tuple(int(v) for v in lines[3 + i * 3:6 + i * 3]) for i in range(16)]


ICON_PALS = [read_pal(P('graphics', 'pokemon', 'icon_palettes', 'icon_palette_%d.pal' % i)) for i in range(3)]


def to_icon(front, pal):
    small = front.convert('RGB').resize((32, 32), Image.BOX)
    # Opacity from the palette indices themselves (index 0 is transparent). Going through the
    # palette here would turn index 0 into its colour and invert the mask.
    opaque = Image.frombytes('L', front.size, bytes(255 if v else 0 for v in front.tobytes())).resize((32, 32), Image.BOX)
    mask = opaque.point(lambda v: 1 if v >= 100 else 0)
    best = None
    for pi, ip in enumerate(ICON_PALS):
        err = 0
        idx = []
        for y in range(32):
            for x in range(32):
                if mask.getpixel((x, y)) == 0:
                    idx.append(0)
                    continue
                c = small.getpixel((x, y))
                k, e = min(((k, sum((a - b) ** 2 for a, b in zip(c, ip[k]))) for k in range(1, 16)), key=lambda t: t[1])
                idx.append(k)
                err += e
        if best is None or err < best[0]:
            best = (err, pi, idx)
    _, pi, idx = best
    frame = Image.new('P', (32, 32), 0)
    frame.putdata(idx)
    icon = Image.new('P', (32, 64), 0)
    icon.paste(frame, (0, 0))
    icon.paste(frame, (0, 33))  # second frame bobs down a pixel
    icon.putpalette([v for c in ICON_PALS[pi] for v in c])
    return icon, pi


def footprint():
    im = Image.new('P', (16, 16), 0)
    im.putpalette([255, 255, 255, 0, 0, 0] + [0, 0, 0] * 14)
    return im


def bbox_coords(im):
    box = im.getbbox() or (0, 0, 64, 64)
    w = min(64, ((box[2] - box[0]) + 7) // 8 * 8)
    h = min(64, ((box[3] - box[1]) + 7) // 8 * 8)
    return w, h, 64 - box[3]


def species_dirs():
    """Map species constant -> graphics directory, from the front pic table."""
    gfx = read('src/data/graphics/pokemon.h')
    table = read('src/data/pokemon_graphics/still_front_pic_table.h')
    out = {}
    for m in re.finditer(r'SPECIES_SPRITE\((\w+),\s*(\w+)\)', table):
        sym = m.group(2)
        p = re.search(r'%s\[\] = INCGFX_U32\("graphics/pokemon/([\w/]+)/front\.(?:png|4bpp)"' % sym, gfx)
        if p:
            out[m.group(1)] = p.group(1)
    return out


import sys
if '--preview' in sys.argv:
    out = sys.argv[sys.argv.index('--preview') + 1]
    picks = smap[:: max(1, len(smap) // 48)][:48]
    sheet = Image.new('RGB', (8 * 136, 6 * 72), (255, 255, 255))
    for i, o in enumerate(picks):
        sp = species[o['id']]
        f = with_pal(draw(sp), palette_for(sp)).convert('RGB')
        b = with_pal(draw(sp, back=True), palette_for(sp, True)).convert('RGB')
        sheet.paste(f, ((i % 8) * 136, (i // 8) * 72))
        sheet.paste(b, ((i % 8) * 136 + 66, (i // 8) * 72))
    sheet.resize((sheet.width * 2, sheet.height * 2), Image.NEAREST).save(out)
    raise SystemExit(0)

dirs = species_dirs()
front_coords = read('src/data/pokemon_graphics/front_pic_coordinates.h')
back_coords = read('src/data/pokemon_graphics/back_pic_coordinates.h')
icon_src = read('src/pokemon_icon.c')
done = 0
for o in smap:
    s = species[o['id']]
    slot = o['slot']
    d = dirs.get(slot)
    if not d:
        raise SystemExit('no graphics dir for ' + slot)
    pal, shiny = palette_for(s), palette_for(s, shiny=True)
    front = with_pal(draw(s), pal)
    back = with_pal(draw(s, back=True), pal)
    targets = [d]
    if slot == 'UNOWN':
        targets = [os.path.join('unown', x) for x in sorted(os.listdir(P('graphics', 'pokemon', 'unown')))
                   if os.path.isdir(P('graphics', 'pokemon', 'unown', x))]
    if slot == 'CASTFORM':
        targets = ['castform/' + f for f in ('normal', 'sunny', 'rainy', 'snowy')]
    pal_dirs = {'castform/' + f: True for f in ('normal', 'sunny', 'rainy', 'snowy')}
    for t in targets:
        base = P('graphics', 'pokemon', t)
        front.save(os.path.join(base, 'front.png'))
        anim = Image.new('P', (64, 128), 0)
        anim.paste(front, (0, 0))
        anim.paste(bob(front, 1), (0, 64))
        anim.putpalette(front.getpalette())
        anim.save(os.path.join(base, 'anim_front.png'))
        back.save(os.path.join(base, 'back.png'))
        icon, ipal = to_icon(front, pal)
        if os.path.exists(os.path.join(base, 'icon.png')) or t == d:
            icon.save(os.path.join(base, 'icon.png'))
        if os.path.exists(os.path.join(base, 'normal.pal')) or t in pal_dirs or t == d:
            write_pal(os.path.join(base, 'normal.pal'), pal)
            write_pal(os.path.join(base, 'shiny.pal'), shiny)
    root = P('graphics', 'pokemon', d.split('/')[0])
    if os.path.exists(os.path.join(root, 'normal.pal')) and slot == 'UNOWN':
        write_pal(os.path.join(root, 'normal.pal'), pal)
        write_pal(os.path.join(root, 'shiny.pal'), shiny)
    fp = os.path.join(root, 'footprint.png')
    footprint().save(fp)
    w, h, yo = bbox_coords(front)
    front_coords = re.sub(r'(\[SPECIES_%s\]\s*= \{ \.size = )MON_COORDS_SIZE\(\d+, \d+\), \.y_offset =\s*\d+' % slot,
                          r'\g<1>MON_COORDS_SIZE(%d, %d), .y_offset = %2d' % (w, h, yo), front_coords)
    bw, bh, byo = bbox_coords(back)
    back_coords = re.sub(r'(\[SPECIES_%s\]\s*= \{ \.size = )MON_COORDS_SIZE\(\d+, \d+\), \.y_offset =\s*\d+' % slot,
                         r'\g<1>MON_COORDS_SIZE(%d, %d), .y_offset = %2d' % (bw, bh, byo), back_coords)
    icon_src = re.sub(r'(\[SPECIES_%s\] = )\d(,)' % slot, r'\g<1>%d\g<2>' % ipal, icon_src)
    done += 1

write('src/data/pokemon_graphics/front_pic_coordinates.h', front_coords)
write('src/data/pokemon_graphics/back_pic_coordinates.h', back_coords)
write('src/pokemon_icon.c', icon_src)
print('sprites: %d species' % done)
