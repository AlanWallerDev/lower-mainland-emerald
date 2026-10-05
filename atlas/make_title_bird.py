#!/usr/bin/env python3
"""Title screen silhouette: a marbled murrelet in flight in place of Rayquaza.

The title background is a 32x32 tilemap (graphics/title_screen/rayquaza.bin) over a 256-tile sheet
(rayquaza.png). This composites the upstream picture, repaints the sky gradient over the old
silhouette (the leftmost 16 columns hold clean sky), draws the murrelet in the silhouette colour
(index 11) with its eye in the pulsing 'legendary marking' colour (index 15), then re-tiles: tiles
are de-duplicated with flips, and every cell keeps its palette bits.

Starts from upstream (needs the pret `upstream` remote), so it is idempotent.
Run from the repo root: python3 atlas/make_title_bird.py [--preview out.png]
"""
import io
import os
import struct
import subprocess
import sys

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REL = 'graphics/title_screen/'
SILHOUETTE, GLOW, WHITE = 11, 15, 2
SS = 4  # supersampling for smooth edges


def git_show(path):
    return subprocess.run(['git', 'show', 'upstream/master:' + path], cwd=ROOT, capture_output=True, check=True).stdout


sheet = Image.open(io.BytesIO(git_show(REL + 'rayquaza.png')))
palette = sheet.getpalette()
sp = sheet.load()
cells = [struct.unpack('<H', git_show(REL + 'rayquaza.bin')[i * 2:i * 2 + 2])[0] for i in range(1024)]

# Composite the upstream picture (256x256, palette indices).
img = Image.new('P', (256, 256))
img.putpalette(palette)
px = img.load()
for i, v in enumerate(cells):
    t, hf, vf = v & 0x3ff, v >> 10 & 1, v >> 11 & 1
    for y in range(8):
        for x in range(8):
            px[(i % 32) * 8 + x, (i // 32) * 8 + y] = sp[(t % 16) * 8 + (7 - x if hf else x), (t // 16) * 8 + (7 - y if vf else y)]

# Repaint the sky over the visible screen from the clean left strip (keeps the gradient's dither).
for y in range(160):
    for x in range(16, 240):
        px[x, y] = px[x % 16, y]

# The murrelet, drawn at SS x scale: chunky alcid body, short slender bill, narrow pointed wings
# raised in a V on the upstroke, short tail. Flying left to right, low over the water.
W, H = 240 * SS, 160 * SS
mask = Image.new('L', (W, H), 0)
d = ImageDraw.Draw(mask)
s = lambda pts: [(x * SS, y * SS) for x, y in pts]
d.ellipse(s([(78, 96), (172, 136)]), fill=255)                          # plump body
d.ellipse(s([(148, 86), (188, 124)]), fill=255)                         # round head
d.polygon(s([(184, 100), (199, 105), (184, 110)]), fill=255)            # short bill
d.polygon(s([(88, 110), (70, 112), (64, 119), (70, 126), (90, 128)]), fill=255)  # stubby tail
d.polygon(s([(140, 104), (122, 84), (98, 66), (70, 54), (54, 50),       # near wing, raised back
             (64, 62), (78, 80), (94, 98), (104, 116)]), fill=255)
d.polygon(s([(132, 100), (150, 78), (170, 60), (192, 48), (206, 44),    # far wing, raised forward
             (198, 58), (182, 76), (162, 96), (150, 108)]), fill=255)
mask = mask.resize((240, 160), Image.LANCZOS)
mp = mask.load()
for y in range(160):
    for x in range(240):
        if mp[x, y] >= 128:
            px[x, y] = SILHOUETTE
# Eye: a pulsing glow pixel with a white glint, like Rayquaza's markings.
px[175, 101] = GLOW
px[176, 101] = GLOW
px[175, 102] = GLOW
px[176, 100] = WHITE

# Re-tile with flip-aware de-duplication.
def tile_at(i):
    cx, cy = (i % 32) * 8, (i // 32) * 8
    return tuple(px[cx + x, cy + y] for y in range(8) for x in range(8))


def flips(t):
    rows = [t[r * 8:r * 8 + 8] for r in range(8)]
    h = tuple(p for r in rows for p in reversed(r))
    v = tuple(p for r in reversed(rows) for p in r)
    hv = tuple(p for r in reversed(rows) for p in reversed(r))
    return [(t, 0, 0), (h, 1, 0), (v, 0, 1), (hv, 1, 1)]


tiles, index, out = [], {}, []
for i, v in enumerate(cells):
    t = tile_at(i)
    hit = next(((index[f], hf, vf) for f, hf, vf in flips(t) if f in index), None)
    if hit is None:
        index[t] = len(tiles)
        tiles.append(t)
        hit = (index[t], 0, 0)
    tid, hf, vf = hit
    out.append(tid | hf << 10 | vf << 11 | (v & 0xf000))
if len(tiles) > 256:
    sys.exit('make_title_bird: %d tiles, the sheet holds 256' % len(tiles))

new = Image.new('P', (128, 128))
new.putpalette(palette)
np_ = new.load()
for n, t in enumerate(tiles):
    for k, p in enumerate(t):
        np_[(n % 16) * 8 + k % 8, (n // 16) * 8 + k // 8] = p
new.save(os.path.join(ROOT, REL, 'rayquaza.png'))
with open(os.path.join(ROOT, REL, 'rayquaza.bin'), 'wb') as f:
    f.write(b''.join(struct.pack('<H', v) for v in out))

if '--preview' in sys.argv:
    img.crop((0, 0, 240, 160)).convert('RGB').resize((480, 320), Image.NEAREST).save(sys.argv[sys.argv.index('--preview') + 1])
print('title bird: murrelet silhouette in %d tiles' % len(tiles))
