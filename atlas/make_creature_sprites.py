#!/usr/bin/env python3
"""Overworld creature sprites (graphics/object_events/pics/pokemon/*) drawn from each slot's battle
sprite (written by make_sprites.py), so the creatures people walk with, the professor's chaser,
the movers and the legendaries all show the organisms the game now holds.

Each sprite keeps its upstream frame layout. The battle sprite is a side view facing left, so it
serves every facing (the game mirrors it for east); walk frames bob one pixel.

Palettes: most sprites share an NPC palette with townsfolk, so they are mapped onto that palette's
colours. Sprites with a palette of their own get one made from the organism. GROUDON and KYOGRE
draw their front and side views with NPC_3 / NPC_4 and their sleeping view with their own palette,
which (as upstream) is a grey version of the shared one.

Run after atlas/make_sprites.py: python3 atlas/make_creature_sprites.py [--preview out.png]
"""
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
OW = 'graphics/object_events/'

# pic: (species slot, frame width, frame height, palette file, own palette?)
SPRITES = {
    'azumarill': ('azumarill', 16, 16, 'npc_1', False),
    'azurill': ('azurill', 16, 16, 'npc_1', False),
    'kecleon': ('kecleon', 16, 16, 'npc_3', False),
    'pikachu': ('pikachu', 16, 16, 'npc_2', False),
    'skitty': ('skitty', 16, 16, 'npc_1', False),
    'zigzagoon': ('zigzagoon', 16, 16, 'npc_1', False),
    'wingull': ('wingull', 16, 16, 'npc_1', False),
    'kirlia': ('kirlia', 16, 32, 'npc_3', False),
    'dusclops': ('dusclops', 16, 32, 'npc_4', False),
    'mew': ('mew', 16, 32, 'npc_1', False),
    'sudowoodo': ('sudowoodo', 16, 32, 'npc_3', False),
    'regi': ('regirock', 32, 32, 'npc_2', False),
    'latias_latios': ('latias', 32, 32, 'npc_2', False),
    'groudon': ('groudon', 32, 32, 'npc_3', False),
    'kyogre': ('kyogre', 32, 32, 'npc_4', False),
    'rayquaza': ('rayquaza', 64, 64, 'npc_3', False),
    'rayquaza_still': ('rayquaza', 64, 64, 'npc_3', False),
    'enemy_zigzagoon': ('zigzagoon', 32, 32, 'enemy_zigzagoon', True),
    'poochyena': ('poochyena', 32, 32, 'poochyena', True),
    'vigoroth': ('vigoroth', 32, 32, 'vigoroth', True),
    'deoxys': ('deoxys', 32, 32, 'deoxys', True),
    'lugia': ('lugia', 32, 32, 'lugia', True),
    'ho_oh': ('ho_oh', 32, 32, 'ho_oh', True),
}
# Dolls and cushions' doll objects (graphics/object_events/pics/dolls): single frames on an NPC palette.
# The slot comes from the file name (big_wailmer_doll -> wailmer).
DOLL_PALETTES = {
    'npc_1': 'azurill baltoy big_blastoise big_lapras big_regirock clefairy jigglypuff marill mudkip skitty '
             'swablu totodile wynaut unused_porygon2 unused_squirtle',
    'npc_2': 'big_charizard meowth pichu pikachu torchic unused_pikachu',
    'npc_3': 'big_regice big_venusaur chikorita gulpin kecleon lotad seedot togepi treecko unused_magnemite '
             'unused_natu unused_wooper',
    'npc_4': 'big_registeel big_rhydon big_snorlax big_wailmer cyndaquil ditto duskull smoochum',
}
# Decoration menu icons for the big dolls (graphics/decorations/*_doll.png, 24x24, own palette).
ICONS = 'blastoise charizard lapras regice regirock registeel rhydon snorlax venusaur wailmer'

# Sleeping views with their own palette: a grey version of the shared palette the pic is drawn for.
ASLEEP = {'groudon': 'npc_3', 'kyogre': 'npc_4'}


def read_pal(name):
    v = open(P(OW, 'palettes', name + '.pal')).read().split()[3:]
    return [tuple(map(int, v[i * 3:i * 3 + 3])) for i in range(16)]


def write_pal(name, cols):
    with open(P(OW, 'palettes', name + '.pal'), 'w', newline='\r\n') as f:
        f.write('JASC-PAL\n0100\n16\n' + ''.join('%d %d %d\n' % c for c in cols))


def battle_rgba(slot):
    """First frame of the slot's battle sprite as RGBA, background (index 0) transparent."""
    im = Image.open(P('graphics/pokemon', slot, 'anim_front.png')).crop((0, 0, 64, 64))
    pal = im.getpalette()
    out = Image.new('RGBA', (64, 64))
    src, dst = im.load(), out.load()
    for y in range(64):
        for x in range(64):
            if src[x, y]:
                dst[x, y] = tuple(pal[src[x, y] * 3:src[x, y] * 3 + 3]) + (255,)
    return out


def fit(rgba, w, h, pad):
    """Crop to the sprite and scale it into w x h (pad pixels clear), centred and standing on the bottom."""
    spr = rgba.crop(rgba.getbbox())
    k = min((w - pad) / spr.width, (h - pad) / spr.height, 1.0)
    sw, sh = max(1, round(spr.width * k)), max(1, round(spr.height * k))
    spr = spr.resize((sw, sh), Image.LANCZOS)
    out = Image.new('RGBA', (w, h))
    out.alpha_composite(spr, ((w - sw) // 2, h - sh - pad // 2))
    return out


def nearest(c, cols, pool):
    return min(pool, key=lambda i: sum((a - b) ** 2 for a, b in zip(c, cols[i])))


def to_indexed(rgba, cols, pool):
    out = Image.new('P', rgba.size)
    out.putpalette([v for c in cols for v in c])
    s, d = rgba.load(), out.load()
    for y in range(rgba.height):
        for x in range(rgba.width):
            r, g, b, a = s[x, y]
            d[x, y] = nearest((r, g, b), cols, pool) if a >= 128 else 0
    return out


def own_palette(rgba, key):
    """Up to 15 colours of the sprite, with the transparent key colour in index 0."""
    q = rgba.convert('RGB').quantize(colors=15)
    qpal = q.getpalette()
    cols = [key] + [tuple(qpal[i * 3:i * 3 + 3]) for i in range(15)]
    return cols


def shifted(im, dy):
    out = Image.new('P', im.size)
    out.putpalette(im.getpalette())
    out.paste(im.crop((0, max(0, -dy), im.width, im.height - max(0, dy))), (0, max(0, dy)))
    return out


made = []
for pic, (slot, fw, fh, palname, own) in SPRITES.items():
    path = P(OW, 'pics/pokemon', pic + '.png')
    n = Image.open(path).width // fw
    spr = fit(battle_rgba(slot), fw, fh, 2 if fw <= 32 else 8)
    cols = read_pal(palname)
    if own:
        cols = own_palette(spr, cols[0])
        write_pal(palname, cols)
    pool = list(range(1, 16))
    # Shared palettes hold townsfolk greens that dark browns and greys snap to (the black bear
    # turned green); unless the organism is itself mostly green, leave those colours out.
    greenish = lambda c: c[1] > c[0] + 30 and c[1] > c[2] + 30
    sp = spr.load()
    px = [sp[x, y][:3] for y in range(spr.height) for x in range(spr.width) if sp[x, y][3] >= 128]
    if not own and sum(map(greenish, px)) < 0.25 * max(1, len(px)):
        pool = [i for i in pool if not greenish(cols[i])]
    frame = to_indexed(spr, cols, pool)
    # Standard 9-frame sets walk on frames 3-8; shorter sets bob on every other frame.
    frames = []
    for i in range(n):
        walking = i >= 3 if n == 9 else i % 2 == 1
        frames.append(shifted(frame, 1 if walking and i % 2 else 0) if pic != 'rayquaza' else frame)
    if pic == 'rayquaza':  # last frames: the bird lifting off
        frames[-2], frames[-1] = shifted(frame, -2), shifted(frame, -8)
    strip = Image.new('P', (fw * n, fh))
    strip.putpalette(frame.getpalette())
    for i, f in enumerate(frames):
        strip.paste(f, (i * fw, 0))
    strip.save(path)
    made.append(frame)

def doll_slot(name):
    return name.replace('unused_', '').replace('big_', '')


def map_frame(slot, w, h, cols, pad=2):
    spr = fit(battle_rgba(slot), w, h, pad)
    greenish = lambda c: c[1] > c[0] + 30 and c[1] > c[2] + 30
    sp = spr.load()
    px = [sp[x, y][:3] for y in range(spr.height) for x in range(spr.width) if sp[x, y][3] >= 128]
    pool = list(range(1, 16))
    if sum(map(greenish, px)) < 0.25 * max(1, len(px)):
        pool = [i for i in pool if not greenish(cols[i])]
    return to_indexed(spr, cols, pool)


dolls = 0
for palname, names in DOLL_PALETTES.items():
    cols = read_pal(palname)
    for name in names.split():
        path = P(OW, 'pics/dolls', name + '_doll.png')
        w, h = Image.open(path).size
        map_frame(doll_slot(name), w, h, cols, 1).save(path)
        dolls += 1
for name in ICONS.split():
    path = P('graphics/decorations', name + '_doll.png')
    old = Image.open(path)
    key = tuple(old.getpalette()[:3])
    spr = fit(battle_rgba(name), 24, 24, 1)
    cols = own_palette(spr, key)
    to_indexed(spr, cols, list(range(1, 16))).save(path)
    dolls += 1

for name, shared in ASLEEP.items():
    cols = read_pal(shared)
    grey = [cols[0]] + [(g, g, g) for g in (int(0.3 * r + 0.59 * gg + 0.11 * b) for r, gg, b in cols[1:])]
    write_pal(name, grey)
    write_pal(name + '_reflection', [cols[0]] + [(int(g * 0.6), int(g * 0.6), min(255, int(g * 0.6) + 40)) for g, _, _ in grey[1:]])

if '--preview' in sys.argv:
    prev = Image.new('RGB', (64 * 8, 64 * 3), (115, 197, 164))
    for i, m in enumerate(made):
        prev.paste(m.convert('RGB').resize((m.width * 2, m.height * 2), Image.NEAREST) if m.width <= 32 else m.convert('RGB'),
                   ((i % 8) * 64, (i // 8) * 64))
    prev.resize((prev.width * 2, prev.height * 2), Image.NEAREST).save(sys.argv[sys.argv.index('--preview') + 1])
print('creature sprites: %d overworld sprites, %d dolls and doll icons written' % (len(made), dolls))
