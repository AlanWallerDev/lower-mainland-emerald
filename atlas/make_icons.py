#!/usr/bin/env python3
"""Menu icons (party, PC boxes, Field Journal lists): every species' icon.png and the three shared
icon palettes (graphics/pokemon/icon_palettes/icon_palette_0-2.pal).

Upstream's three palettes hold Hoenn's colours, so many organisms' browns, greens and greys fell to
near-black and their icons read as silhouettes. This builds three palettes from the organisms' own
front sprites instead: species are grouped by colour, each group gets the 15 colours that best fit
its sprites (k-means), and each species then uses whichever palette draws it with the least error.
The egg and question-mark icons are remapped from their old palette to the new one.

Run after atlas/make_sprites.py (it reads front.png and normal.pal): python3 atlas/make_icons.py
"""
import io
import json
import os
import re
import subprocess

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
PALDIR = P('graphics', 'pokemon', 'icon_palettes')
KEY = (98, 156, 131)  # icon palette index 0 (transparent), as upstream


def read_pal(path):
    v = open(path).read().split()[3:]
    return [tuple(map(int, v[i * 3:i * 3 + 3])) for i in range(16)]


def write_pal(path, cols):
    with open(path, 'w', newline='\r\n') as f:
        f.write('JASC-PAL\n0100\n16\n' + ''.join('%d %d %d\n' % c for c in cols))


def dist(a, b):
    # Weighted RGB distance (green counts most, as the eye sees it).
    return 2 * (a[0] - b[0]) ** 2 + 4 * (a[1] - b[1]) ** 2 + 3 * (a[2] - b[2]) ** 2


def small_icon(base):
    """The front sprite shrunk to 32x32: list of (x, y, rgb) for opaque pixels."""
    front = Image.open(os.path.join(base, 'front.png'))
    pal = read_pal(os.path.join(base, 'normal.pal'))
    rgb = Image.new('RGB', front.size)
    rgb.putdata([pal[v] for v in front.tobytes()])
    small = rgb.resize((32, 32), Image.BOX)
    mask = Image.frombytes('L', front.size, bytes(255 if v else 0 for v in front.tobytes())).resize((32, 32), Image.BOX)
    return [(x, y, small.getpixel((x, y))) for y in range(32) for x in range(32) if mask.getpixel((x, y)) >= 100]


def kmeans(colors, k, iters=12):
    """k colours fitting a list of rgb tuples (deterministic: seeded by spread-out picks)."""
    uniq = sorted(set(colors))
    if len(uniq) <= k:
        return uniq + [uniq[-1]] * (k - len(uniq))
    lum = sorted(uniq, key=sum)
    cent = [lum[int(i * (len(lum) - 1) / (k - 1))] for i in range(k)]
    counts = {}
    for c in colors:
        counts[c] = counts.get(c, 0) + 1
    for _ in range(iters):
        sums = [[0, 0, 0, 0] for _ in cent]
        for c, n in counts.items():
            j = min(range(k), key=lambda i: dist(c, cent[i]))
            s = sums[j]
            s[0] += c[0] * n; s[1] += c[1] * n; s[2] += c[2] * n; s[3] += n
        cent = [(s[0] // s[3], s[1] // s[3], s[2] // s[3]) if s[3] else cent[i] for i, s in enumerate(sums)]
    return cent


def fit_error(pixels, pal):
    return sum(min(dist(c, p) for p in pal) for _, _, c in pixels)


def snap(c):
    return tuple(v // 8 * 8 for v in c)  # GBA colours are 5 bits per channel


def main():
    smap = json.load(open(P('atlas', 'species_map.json')))
    src = open(P('src', 'pokemon_icon.c')).read()
    icons = {}
    for e in smap:
        slot = e['slot']
        d = 'unown/a' if slot == 'UNOWN' else 'castform/normal' if slot == 'CASTFORM' else slot.lower()
        icons[slot] = (d, small_icon(P('graphics', 'pokemon', d)))

    # Start from a split by mean hue (greens/blues, warm, neutral), then alternate fitting and assigning.
    def group0(px):
        r = sum(c[0] for _, _, c in px) / len(px)
        g = sum(c[1] for _, _, c in px) / len(px)
        b = sum(c[2] for _, _, c in px) / len(px)
        if max(r, g, b) - min(r, g, b) < 25:
            return 2
        return 0 if g >= r or b >= r else 1
    assign = {s: group0(px) for s, (_, px) in icons.items()}
    pals = None
    for _ in range(4):
        pals = []
        for gi in range(3):
            cols = [c for s, (_, px) in icons.items() if assign[s] == gi for _, _, c in px]
            pals.append([KEY] + [snap(c) for c in kmeans(cols, 15)])
        assign = {s: min(range(3), key=lambda gi: fit_error(px, pals[gi][1:])) for s, (_, px) in icons.items()}

    old = [read_pal(os.path.join(PALDIR, 'icon_palette_%d.pal' % i)) for i in range(3)]
    for i, pal in enumerate(pals):
        write_pal(os.path.join(PALDIR, 'icon_palette_%d.pal' % i), pal)

    for slot, (d, px) in icons.items():
        pal = pals[assign[slot]]
        frame = Image.new('P', (32, 32), 0)
        for x, y, c in px:
            frame.putpixel((x, y), min(range(1, 16), key=lambda k: dist(c, pal[k])))
        icon = Image.new('P', (32, 64), 0)
        icon.paste(frame, (0, 0))
        icon.paste(frame, (0, 33))  # second frame bobs down a pixel
        icon.putpalette([v for c in pal for v in c])
        targets = [d]
        if slot == 'UNOWN':
            targets = ['unown/' + x for x in sorted(os.listdir(P('graphics', 'pokemon', 'unown')))
                       if os.path.isdir(P('graphics', 'pokemon', 'unown', x))]
        for t in targets:
            if os.path.exists(P('graphics', 'pokemon', t, 'icon.png')) or t == d:
                icon.save(P('graphics', 'pokemon', t, 'icon.png'))
        src = re.sub(r'(\[SPECIES_%s\] = )\d(,)' % slot, r'\g<1>%d\g<2>' % assign[slot], src)
    # Unown's letter forms share the slot's palette.
    src = re.sub(r'(\[SPECIES_UNOWN_\w+\] = )\d(,)', r'\g<1>%d\g<2>' % assign.get('UNOWN', 0), src)

    # Fixed icons (egg, question mark): remap from the upstream palette they were drawn for.
    for name, sym in (('egg', 'EGG'), ('question_mark', None)):
        rel = 'graphics/pokemon/%s/icon.png' % name
        data = subprocess.run(['git', 'show', 'upstream/master:' + rel], cwd=ROOT, capture_output=True).stdout
        if not data:
            continue
        im = Image.open(io.BytesIO(data))
        m = re.search(r'\[SPECIES_%s\] = (\d),' % sym, src) if sym else None
        pi = int(m.group(1)) if m else 0
        upal = old[pi]
        up = subprocess.run(['git', 'show', 'upstream/master:graphics/pokemon/icon_palettes/icon_palette_%d.pal' % pi],
                            cwd=ROOT, capture_output=True).stdout.decode().split()[3:]
        if up:
            upal = [tuple(map(int, up[i * 3:i * 3 + 3])) for i in range(16)]
        out = Image.new('P', im.size, 0)
        out.putdata([0 if v == 0 else min(range(1, 16), key=lambda k: dist(upal[v], pals[pi][k])) for v in im.tobytes()])
        out.putpalette([v for c in pals[pi] for v in c])
        out.save(P(rel))

    open(P('src', 'pokemon_icon.c'), 'w').write(src)
    print('icons: %d species on 3 fitted palettes (%s)' % (len(icons), ', '.join(
        str(sum(1 for v in assign.values() if v == i)) for i in range(3))))


main()
