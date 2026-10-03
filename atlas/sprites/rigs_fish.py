"""Fish rigs: shark, fish, seahorse, eel, angler, manta, armored."""


def _caudal(a, role, x, y, h=10, crescent=False, shark=False):
    p = a.part(role)
    if shark:
        p.poly([(x - 2, y - 2), (x + 10, y - h), (x + 6, y), (x + 9, y + h * .6), (x - 2, y + 3)])
    elif crescent:
        p.poly([(x - 2, y - 2), (x + 8, y - h), (x + 4, y), (x + 8, y + h), (x - 2, y + 2)])
    else:
        p.poly([(x - 2, y - 2), (x + 9, y - h * .8), (x + 9, y + h * .8), (x - 2, y + 2)])
    return p


def shark(a, sp, r):
    """Sharks. A back, C belly, D spots/stripes, W teeth. kind: plain, hammer, whale, goblin, frilled, basking, cookie, mega."""
    kind = sp.get('kind', 'plain')
    if kind == 'frilled':
        body = a.part('A').taper([(8, 30), (24, 32), (40, 36), (56, 34), (62, 30)], 9, 3)
        a.part('E').rect(14, 26, 16, 36).rect(18, 26, 20, 36)
        a.eye(8, 28, 1)
        return
    small = kind == 'cookie'
    _caudal(a, 'A', 52, 30, 12 if not small else 8, shark=True)
    body = a.part('A').blob([(4, 32), (14, 24), (36, 23), (54, 29), (54, 33), (36, 40), (12, 40)])
    a.part('C', clip=body, line=False).blob([(0, 34), (30, 35), (56, 33), (40, 44), (4, 44)])
    if not small:
        a.part('A').poly([(26, 25), (32, 10), (38, 25)])  # dorsal
        a.part('A').poly([(20, 37), (26, 48), (30, 38)])  # pectoral
    if kind == 'whale':
        s = a.part('D', clip=body, line=False)
        for _ in range(18):
            x, y = 10 + 42 * next(r), 25 + 11 * next(r)
            s.circle(x, y, .9)
    elif kind == 'tiger':
        s = a.part('D', clip=body, line=False)
        for x in range(18, 52, 5):
            s.rect(x, 22, x + 1.5, 31)
    elif kind == 'cookie':
        a.part('D', clip=body, line=False).rect(10, 20, 14, 46)
    if kind == 'hammer':
        a.part('A').blob([(4, 22), (10, 22), (12, 40), (4, 40)])
        a.eye(6, 23, 1)
    elif kind == 'goblin':
        a.part('A').poly([(10, 26), (-4, 26), (8, 32)])
        a.part('W').rect(6, 34, 12, 36)
        a.eye(12, 30, 1)
    elif kind == 'basking':
        a.part('K').blob([(2, 32), (12, 30), (12, 42), (2, 40)])
        g = a.part('D', clip=body, line=False)
        for x in (14, 17, 20, 23):
            g.rect(x, 26, x + 1, 40)
        a.eye(9, 29, 1)
    else:
        if kind in ('mega', 'plain', 'whale', 'tiger'):
            a.part('W').poly([(6, 36), (14, 37), (12, 39), (8, 39)])
        for x in (16, 18, 20):
            a.part('D' if kind != 'whale' else 'C', clip=body, line=False).rect(x, 30, x + .8, 36)
        a.eye(10, 30, 1)


def fish(a, sp, r):
    """Bony fish. A body, B fins, C belly, D spots/marks, E eye/glow. shape: torpedo, round, small, snail, deep.
    finlets, spots, crest (oarfish), fangs, dome (barreleye), tripod."""
    shape = sp.get('shape', 'small')
    if sp.get('tripod'):
        a.part('B').line([(20, 40), (14, 58)], 1.2).line([(30, 40), (32, 58)], 1.2).line([(50, 36), (58, 58)], 1.2)
    if shape == 'round':
        _caudal(a, 'B', 50, 32, 8)
        body = a.part('A').blob([(8, 32), (20, 18), (40, 18), (52, 30), (40, 46), (20, 46)])
        a.part('B').poly([(28, 20), (36, 8), (40, 20)]).poly([(26, 40), (30, 50), (36, 42)])
    elif shape == 'torpedo':
        _caudal(a, 'B', 52, 31, 12, crescent=True)
        body = a.part('A').blob([(4, 32), (16, 24), (40, 24), (54, 31), (40, 38), (16, 40)])
        a.part('B').poly([(24, 25), (28, 16), (32, 25)])
    elif shape == 'snail':
        body = a.part('A').blob([(6, 30), (18, 20), (30, 24), (58, 32), (30, 42), (16, 44)])
    elif shape == 'deep':
        _caudal(a, 'B', 50, 32, 7)
        body = a.part('A').blob([(4, 26), (16, 18), (32, 22), (52, 30), (32, 40), (14, 44), (4, 38)])
    else:
        _caudal(a, 'B', 46, 32, 8)
        body = a.part('A').blob([(10, 32), (20, 24), (36, 24), (48, 32), (36, 40), (20, 40)])
        a.part('B').poly([(26, 25), (32, 18), (36, 25)])
    a.part('C', clip=body, line=False).ell(0, 34, 60, 52)
    if sp.get('spots'):
        s = a.part('D', clip=body, line=False)
        for _ in range(12):
            x, y = 10 + 40 * next(r), 20 + 22 * next(r)
            s.circle(x, y, 1)
    if sp.get('finlets'):
        f = a.part('D')
        for x in (36, 40, 44, 48):
            f.poly([(x, 25), (x + 2, 22), (x + 3, 26)]).poly([(x, 37), (x + 2, 40), (x + 3, 36)])
    if sp.get('crest'):
        a.part('D').taper([(4, 20), (6, 8), (10, 2)], 3, 2)
        a.part('D').rect(10, 22, 56, 24)
    if sp.get('dome'):
        a.part('E', line=False).ell(10, 10, 30, 28)
        a.part('B').circle(18, 22, 2.5)
        a.eye(18, 21, 1)
        return
    if sp.get('fangs'):
        f = a.part('W')
        for x in (3, 7, 11):
            f.poly([(x, 33), (x + 1.2, 43), (x + 2.4, 33)])
    big = shape == 'deep' or sp.get('bigeye')
    a.eye(12, 28 if shape != 'round' else 27, 2 if big else 1, 'big' if big else 'dot')
    if sp.get('glow'):
        g = a.part('E')
        for x in range(14, 44, 6):
            g.circle(x, 38, .8)


def seahorse(a, sp, r):
    """Seahorse. A body, D spots, B fin."""
    body = a.part('A')
    body.taper([(34, 18), (38, 30), (34, 42), (40, 52), (46, 56), (48, 50), (44, 48)], 10, 3)
    head = a.part('A').circle(30, 14, 7)
    a.part('A').line([(26, 16), (14, 20)], 3.5)
    a.part('A').poly([(30, 8), (33, 2), (36, 8)])
    a.part('B').ell(40, 26, 46, 36)
    s = a.part('D', clip=body, line=False)
    for _ in range(8):
        x, y = 30 + 14 * next(r), 18 + 34 * next(r)
        s.circle(x, y, .8)
    a.eye(28, 12, 1)


def eel(a, sp, r):
    """Eel-like fish. A body, B fin, E tail light. bigmouth (gulper), fleshy (hagfish)."""
    body = a.part('A').taper([(10, 34), (22, 30), (34, 36), (46, 30), (58, 36), (62, 40)], 8 if sp.get('fleshy') else 6, 2)
    if sp.get('bigmouth'):
        a.part('A').blob([(0, 16), (18, 24), (20, 38), (0, 54), (6, 34)])
        a.part('C').blob([(2, 22), (15, 28), (3, 48), (8, 34)])
        a.part('E').circle(62, 40, 2)
        a.eye(14, 28, 1)
    else:
        a.part('A').ell(4, 30, 16, 38)
        if sp.get('fleshy'):
            a.part('C').line([(4, 36), (2, 39)], 1).line([(6, 37), (5, 40)], 1)
        a.eye(9, 32, 1)


def angler(a, sp, r):
    """Deep-sea anglerfish. A body, E lure glow, W teeth."""
    _caudal(a, 'A', 48, 36, 6)
    body = a.part('A').blob([(6, 28), (20, 18), (40, 22), (50, 34), (38, 48), (16, 50), (4, 42)])
    a.part('A').curve((22, 20), (18, 4), (6, 8), 1.4, 1)
    a.part('E').circle(6, 9, 3)
    a.part('K').blob([(2, 34), (14, 34), (16, 44), (4, 46)])
    t = a.part('W')
    for x in (4, 7, 10, 13):
        t.poly([(x, 34), (x + 1, 39), (x + 2, 34)])
    a.eye(18, 30, 1, 'pale')


def manta(a, sp, r):
    """Manta ray seen from above-front. A back, C belly edge, cephalic fins."""
    a.part('A').line([(32, 40), (32, 62)], 1.5)
    body = a.part('A').blob([(32, 18), (60, 30), (62, 36), (40, 38), (32, 46), (24, 38), (2, 36), (4, 30)])
    a.part('C', clip=body, line=False).ell(20, 34, 44, 50)
    a.part('A').blob([(26, 18), (24, 10), (28, 16)]).blob([(38, 18), (40, 10), (36, 16)])
    a.eye(27, 22, 1)
    a.eye(37, 22, 1)


def armored(a, sp, r):
    """Dunkleosteus: armoured head plates (B) over a sharkish body (A), bony blades (W)."""
    _caudal(a, 'A', 52, 32, 12, shark=True)
    body = a.part('A').blob([(10, 32), (24, 24), (44, 26), (56, 32), (44, 40), (22, 42)])
    a.part('B').blob([(2, 30), (12, 16), (30, 18), (32, 40), (14, 46), (2, 42)])
    a.part('W').poly([(2, 34), (12, 36), (4, 40)])
    a.part('B', line=True).rect(20, 18, 22, 44)
    a.eye(14, 26, 2, 'big')
