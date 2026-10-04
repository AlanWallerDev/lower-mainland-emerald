"""Invertebrate rigs: insects, arachnids, myriapods, crustaceans, molluscs, cnidarians, worms, oddities."""
import math


def _sixlegs(a, role, xs, y, length=12, w=1.2):
    p = a.part(role)
    for i, x in enumerate(xs):
        p.line([(x, y), (x - 4 + i * 2, y + length * .5), (x - 6 + i * 4, y + length)], w)
    return p


def butterfly(a, sp, r):
    """Butterfly or moth, wings open, seen from above. A wing, B wing border/veins, C spots, D band, E body.
    tails (swallowtail), veins (monarch), moth (feathery antennae, fat body), eyespots."""
    moth = sp.get('moth', False)
    fw = a.part('A')
    fw.blob([(32, 26), (8, 6), (2, 14), (6, 30), (30, 34)]).blob([(32, 26), (56, 6), (62, 14), (58, 30), (34, 34)])
    hw = a.part(sp.get('hind', 'A'))
    hw.blob([(30, 32), (8, 34), (10, 50), (24, 52), (31, 40)]).blob([(34, 32), (56, 34), (54, 50), (40, 52), (33, 40)])
    if sp.get('tails'):
        hw.taper([(16, 50), (14, 60)], 3, 1.5).taper([(48, 50), (50, 60)], 3, 1.5)
    wings = [fw, hw]
    for w in wings:
        a.part('B', clip=w, line=False).blob([(0, 4), (64, 4), (64, 10), (40, 20), (24, 20), (0, 10)]) if sp.get('tips') else None
    if sp.get('border'):
        for w in wings:
            b = a.part('B', clip=w, line=False)
            b.blob([(-4, 0), (68, 0), (68, 64), (-4, 64), (-4, 60), (60, 60), (60, 4), (4, 4), (4, 60), (-4, 60)])
            b.poly([(0, 0), (10, 0), (0, 40)]).poly([(64, 0), (54, 0), (64, 40)])
    if sp.get('veins'):
        for w in wings:
            v = a.part('B', clip=w, line=False)
            for t in (-50, -25, 0, 25):
                for side in (-1, 1):
                    ang = math.radians(t)
                    v.line([(32, 30), (32 + side * 30 * math.cos(ang), 30 + 30 * math.sin(ang) - 6)], 1)
    if sp.get('band'):
        a.part('D', clip=fw, line=False).blob([(14, 10), (24, 24), (40, 24), (50, 10), (54, 18), (40, 30), (24, 30), (10, 18)])
        a.part('D', clip=hw, line=False).rect(16, 36, 48, 41)
    if sp.get('stripes'):
        s = a.part('D', clip=fw, line=False)
        for x in (12, 20, 44, 52):
            s.line([(x, 4), (x + (32 - x) * .3, 30)], 2.4)
    if sp.get('spots'):
        s = a.part('C', clip=hw, line=False)
        for x in (14, 20, 26, 38, 44, 50):
            s.circle(x, 47, 1.2)
    if sp.get('eyespots'):
        e = a.part('C')
        for (x, y) in ((16, 42), (48, 42), (14, 18), (50, 18)):
            e.circle(x, y, 3)
        k = a.part('K')
        for (x, y) in ((16, 42), (48, 42), (14, 18), (50, 18)):
            k.circle(x, y, 1.2)
    body = a.part('E')
    body.ell(29, 18, 35, 50 if not moth else 46)
    if moth:
        body.ell(27, 22, 37, 46)
        a.part('E').line([(30, 18), (24, 8)], 2.5).line([(34, 18), (40, 8)], 2.5)
    else:
        a.part('K').line([(31, 19), (26, 6)], .8).line([(33, 19), (38, 6)], .8)
        a.part('K').circle(26, 6, 1).circle(38, 6, 1)


def caterpillar(a, sp, r):
    """Caterpillar. A body, B bands, C spots/belly, D horn/eyespot. pattern: bands, spots, eyespot, fuzzy."""
    pat = sp.get('pattern', 'bands')
    segs = []
    for i in range(7):
        x = 12 + i * 7
        y = 40 - 4 * math.sin(i * .8)
        segs.append((x, y))
    body = a.part('A')
    for (x, y) in segs:
        body.circle(x, y, 6.5 if pat != 'fuzzy' else 8)
    a.part('A').circle(6, 40, 7)
    if pat == 'bands':
        b = a.part('B', clip=body, line=False)
        for (x, y) in segs[::2]:
            b.rect(x - 1.5, 20, x + 1.5, 60)
    if pat in ('spots', 'bands'):
        c = a.part('C', clip=body, line=False)
        for (x, y) in segs:
            c.circle(x, y - 2, 1.2)
    if pat == 'eyespot':
        a.part('C').circle(12, 34, 3.2)
        a.part('K').circle(11, 34, 1.4)
    if pat == 'fuzzy':
        h = a.part('B')
        for (x, y) in segs:
            for k in range(-2, 3):
                h.line([(x + k * 2, y - 6), (x + k * 3, y - 12)], 1)
        a.part('D', clip=body, line=False).rect(20, 20, 40, 60)
    if sp.get('horn'):
        a.part('D').line([(54, 36), (60, 26)], 2)
    a.part('C').rect(4, 46, 60, 48)
    a.eye(4, 38, 1)


def beetle(a, sp, r):
    """Beetle from above-side. A elytra, B pronotum/head, C spots, D horns/mandibles, legs K.
    spots, stripes, horn (rhino/goliath), mandibles (stag), neck (giraffe weevil), ridges, bands."""
    _sixlegs(a, 'K', [24, 32, 40], 44, 12)
    el = a.part('A').blob([(18, 30), (36, 22), (56, 26), (60, 38), (50, 50), (28, 50), (18, 44)])
    a.part('A', clip=el).line([(20, 37), (58, 37)], .8)
    if sp.get('spots'):
        s = a.part('C', clip=el, line=False)
        for (x, y) in [(28, 30), (40, 28), (52, 32), (30, 44), (42, 44), (54, 42)]:
            s.circle(x, y, 2.2)
    if sp.get('bands'):
        s = a.part('C', clip=el, line=False)
        s.rect(28, 20, 33, 54).rect(44, 20, 49, 54)
    if sp.get('stripes'):
        s = a.part('C', clip=el, line=False)
        for y in (28, 34, 40, 46):
            s.rect(18, y, 62, y + 1.2)
    if sp.get('ridges'):
        s = a.part('B', clip=el, line=False)
        for _ in range(14):
            x, y = 22 + 36 * next(r), 26 + 22 * next(r)
            s.circle(x, y, 1)
    pro = a.part('B').blob([(8, 34), (14, 26), (22, 28), (24, 42), (14, 44)])
    if sp.get('neck'):
        a.part('B').line([(14, 34), (4, 18)], 3)
        head = a.part('B').circle(4, 16, 3)
        a.eye(3, 15, 1)
        return
    head = a.part('B').ell(2, 32, 12, 40)
    if sp.get('mandibles'):
        a.part('D').curve((4, 32), (-2, 22), (6, 18), 2.5, 1.5).curve((4, 40), (-4, 36), (0, 28), 2.5, 1.5)
    if sp.get('horn'):
        a.part('D').curve((6, 32), (2, 22), (8, 16), 2.5, 1.5)
    a.part('K').line([(4, 33), (0, 26)], .8)
    a.eye(5, 35, 1)


def bee(a, sp, r):
    """Bee, wasp, hornet, ant-like velvet ant. A body, B stripes, C face/markings, wings W. fuzzy, wingless."""
    if not sp.get('wingless'):
        w = a.part('W')
        w.blob([(30, 28), (40, 8), (50, 10), (38, 30)]).blob([(26, 28), (24, 10), (32, 10), (32, 28)])
    _sixlegs(a, 'K', [22, 28, 34], 40, 12)
    abd = a.part('A').blob([(32, 34), (42, 26), (56, 30), (60, 40), (50, 48), (36, 46)])
    s = a.part('B', clip=abd, line=False)
    for x in (40, 47, 54):
        s.rect(x, 20, x + 3, 56)
    th = a.part(sp.get('thorax', 'A')).circle(26, 36, 7.5)
    if sp.get('fuzzy'):
        a.part(sp.get('thorax', 'A')).circle(26, 32, 6)
    head = a.part(sp.get('headrole', 'B')).circle(14, 36, 6.5)
    if sp.get('face'):
        a.part('C', clip=head, line=False).ell(6, 36, 16, 44)
    a.part('K').line([(12, 31), (8, 22)], 1).line([(15, 31), (14, 22)], 1)
    a.eye(12, 34, 2, 'big')


def ant(a, sp, r):
    """Ant or termite. A body, B head, E honeypot abdomen."""
    term = sp.get('termite', False)
    _sixlegs(a, 'A', [24, 30, 36], 40, 12)
    if sp.get('repletes'):
        a.part('E').circle(48, 36, 11)
    else:
        a.part('A').ell(38, 30, 58, 46) if not term else a.part('A').ell(36, 30, 60, 46)
    a.part('A').ell(22, 33, 36, 43)
    head = a.part('B').circle(14, 36, 7 if not sp.get('bighead') else 9)
    if not term:
        a.part('B').curve((10, 30), (4, 22), (0, 24), 1.2, 1)
        a.part('D').poly([(6, 40), (0, 42), (6, 43)])
    a.eye(12, 34, 1)


def dragonfly(a, sp, r):
    """Dragonfly / mayfly. A body, B wing tint, C spots. mayfly: upright wings, tail filaments."""
    may = sp.get('mayfly', False)
    w = a.part('W')
    if may:
        w.blob([(26, 30), (22, 4), (34, 2), (32, 30)])
        a.part('A').line([(54, 34), (63, 22)], .8).line([(54, 34), (64, 30)], .8)
    else:
        w.blob([(24, 30), (6, 12), (2, 18), (24, 34)]).blob([(30, 30), (48, 12), (54, 18), (30, 34)])
        w.blob([(24, 34), (6, 44), (8, 50), (26, 38)]).blob([(30, 34), (50, 44), (48, 50), (30, 38)])
        if sp.get('wingspots'):
            s = a.part('B', clip=w, line=False)
            s.ell(8, 10, 24, 22).ell(34, 10, 50, 22).ell(6, 40, 22, 52).ell(36, 40, 52, 52)
    a.part('A').line([(28, 34), (60, 34) if not may else (54, 34)], 3)
    a.part('A').ell(20, 29, 32, 39)
    a.part('A').circle(17, 34, 4.5)
    a.eye(16, 32, 2, 'big')


def mantis(a, sp, r):
    """Praying mantis, upright on a twig. A body, B wings, C flower lobes (devil's flower mantis), D twig."""
    a.part('D' if not sp.get('flower') else 'B').rect(4, 56, 60, 59)
    legs = a.part('A')
    legs.line([(34, 42), (28, 56)], 1.6).line([(40, 42), (46, 56)], 1.6).line([(44, 40), (54, 56)], 1.6)
    abd = a.part('A').blob([(30, 40), (40, 34), (60, 40), (58, 46), (40, 48)])
    a.part('B', clip=None).blob([(32, 36), (44, 30), (62, 38), (44, 40)])
    if sp.get('flower'):
        a.part('C').blob([(24, 34), (30, 20), (40, 26), (36, 38)]).blob([(14, 30), (18, 22), (24, 30)])
    a.part('A').line([(32, 40), (22, 18)], 4)
    a.part('A').line([(24, 24), (12, 30), (10, 22)], 2.6).line([(25, 26), (16, 36), (14, 28)], 2.6)
    head = a.part('A').poly([(16, 14), (22, 10), (28, 14), (22, 20)])
    a.part('A').line([(19, 11), (12, 2)], .8).line([(23, 10), (22, 0)], .8)
    a.eye(18, 13, 1, 'big')
    a.eye(26, 13, 1, 'big')


def orthopteran(a, sp, r):
    """Cricket / locust / Jerusalem cricket / cockroach. A body, B bands/pattern, C belly. kind: locust, jerusalem, roach, katydid."""
    kind = sp.get('kind', 'locust')
    if kind == 'jerusalem':
        _sixlegs(a, 'A', [22, 30, 38], 42, 12, 2)
        abd = a.part('A').blob([(26, 36), (40, 30), (58, 34), (60, 46), (40, 50), (26, 46)])
        s = a.part('B', clip=abd, line=False)
        for x in range(30, 60, 5):
            s.rect(x, 20, x + 2, 60)
        head = a.part('C').circle(14, 38, 10)
        a.eye(9, 35, 1)
        return
    if kind == 'roach':
        _sixlegs(a, 'K', [22, 30, 38], 44, 12)
        body = a.part('A').blob([(8, 38), (20, 28), (50, 28), (60, 40), (50, 50), (20, 50)])
        s = a.part('B', clip=body, line=False)
        for x in range(22, 58, 6):
            s.rect(x, 20, x + 1.2, 60)
        a.part('C').ell(4, 34, 18, 46)
        a.part('K').curve((6, 36), (0, 20), (8, 12), .9, .7)
        a.eye(8, 38, 1)
        return
    a.part('A').line([(36, 40), (50, 26), (60, 46)], 2.5)
    _sixlegs(a, 'A', [20, 26], 44, 10)
    body = a.part('A').blob([(10, 38), (18, 30), (54, 32), (60, 38), (50, 44), (18, 46)])
    a.part('B', clip=body).blob([(20, 30), (60, 34), (56, 40), (22, 38)])
    if sp.get('spots'):
        s = a.part('D', clip=body, line=False)
        for x in range(24, 56, 6):
            s.circle(x, 35, 1.2)
    a.part('A').line([(14, 44), (8, 54)], 2)
    head = a.part('A').circle(10, 38, 6)
    a.part('A').curve((8, 33), (0, 20), (6, 8), .8, .6)
    a.eye(8, 37, 1, 'big')


def truebug(a, sp, r):
    """True bugs: giant water bug, sharpshooter, flatid leaf bug. A body, B wing/pattern, C spots. kind: waterbug, hopper, flatid."""
    kind = sp.get('kind', 'hopper')
    if kind == 'flatid':
        a.part('A').blob([(10, 50), (26, 18), (50, 18), (58, 50)])
        a.part('B').circle(14, 46, 4)
        a.part('K').line([(14, 40), (10, 32)], .8)
        a.eye(12, 45, 1)
        return
    if kind == 'waterbug':
        _sixlegs(a, 'A', [30, 38], 44, 10, 2)
        a.part('A').curve((20, 38), (6, 34), (4, 26), 3.5, 2)
        body = a.part('A').blob([(10, 38), (20, 26), (48, 26), (60, 38), (48, 50), (20, 50)])
        a.part('B', clip=body, line=False).blob([(24, 26), (60, 30), (60, 46), (28, 44)])
        a.part('A').poly([(10, 36), (2, 38), (10, 42)])
        a.eye(10, 34, 1)
        return
    _sixlegs(a, 'K', [24, 30, 36], 40, 10)
    body = a.part('A').blob([(8, 36), (16, 28), (46, 30), (60, 38), (46, 44), (16, 44)])
    a.part('B', clip=body, line=False).blob([(22, 30), (60, 34), (58, 42), (24, 42)])
    s = a.part('C', clip=body, line=False)
    for _ in range(12):
        x, y = 18 + 40 * next(r), 28 + 14 * next(r)
        s.circle(x, y, .8)
    a.part('A').ell(4, 32, 16, 42)
    a.eye(8, 35, 2, 'big')


def fly(a, sp, r):
    """Fly / mosquito / fairyfly. A body, B stripes, wings W. kind: tsetse, mosquito, fairyfly."""
    kind = sp.get('kind', 'tsetse')
    w = a.part('W')
    if kind == 'fairyfly':
        w.line([(30, 30), (54, 10)], 3).line([(28, 30), (40, 6)], 3)
        f = a.part('W')
        for i in range(8):
            f.line([(30 + i * 3, 30 - i * 2.5), (36 + i * 3, 34 - i * 2.5)], .6)
    else:
        w.blob([(30, 30), (54, 18), (58, 24), (34, 34)]).blob([(28, 30), (48, 26), (50, 32), (30, 34)])
    legs = 18 if kind == 'mosquito' else 10
    _sixlegs(a, 'A', [22, 28, 34], 40, legs, 1 if kind == 'mosquito' else 1.2)
    abd = a.part('A').blob([(30, 34), (42, 30), (56, 34), (44, 42)] if kind != 'mosquito' else [(30, 34), (46, 32), (60, 30), (46, 38)])
    if sp.get('stripes'):
        s = a.part('B', clip=abd, line=False)
        for x in (36, 42, 48):
            s.rect(x, 20, x + 2, 50)
    a.part('A').ell(18, 30, 32, 42)
    head = a.part('A').circle(14, 36, 5)
    if kind == 'mosquito':
        a.part('A').line([(10, 38), (0, 46)], 1)
    elif kind == 'tsetse':
        a.part('A').line([(10, 36), (2, 36)], 1.2)
    a.eye(13, 35, 2, 'red' if kind == 'tsetse' else 'big')


def springtail(a, sp, r):
    """Springtail (snow flea). A body, small and round, furcula."""
    a.part('A').line([(40, 48), (52, 54)], 1.5)
    _sixlegs(a, 'A', [24, 30, 36], 46, 8)
    body = a.part('A').blob([(14, 40), (22, 30), (44, 30), (52, 42), (40, 50), (20, 50)])
    a.part('A').curve((16, 34), (8, 22), (4, 22), 1.2, 1)
    a.eye(16, 38, 1)


def spider(a, sp, r):
    """Spider. A body, B abdomen, C marks (hourglass, stripes), D hair/knee bands. kind: widow, tarantula, jumper, recluse."""
    kind = sp.get('kind', 'widow')
    thick = 2.8 if kind == 'tarantula' else 1.4
    legs = a.part('A')
    for i, (ang) in enumerate((-60, -25, 15, 50)):
        t = math.radians(ang)
        legs.line([(26, 36), (26 - 12 * math.cos(t), 36 + 12 * math.sin(t) - 6), (24 - 22 * math.cos(t), 56)], thick)
        legs.line([(30, 36), (34 + 12 * math.cos(t), 36 + 12 * math.sin(t) - 6), (38 + 18 * math.cos(t), 56)], thick)
    if kind == 'tarantula':
        k = a.part('D', clip=legs, line=False)
        for y in (44, 52):
            k.rect(0, y, 64, y + 2)
    abd = a.part('B').circle(44, 30, 13 if kind == 'widow' else 11)
    if kind == 'widow':
        a.part('C', clip=abd, line=False).poly([(42, 34), (48, 34), (45, 38), (48, 42), (42, 42), (45, 38)])
    if kind == 'jumper':
        a.part('C', clip=abd, line=False).circle(44, 26, 2.5).circle(40, 32, 1.5).circle(48, 32, 1.5)
    ceph = a.part('A').circle(24, 36, 8)
    if kind == 'recluse':
        a.part('D', clip=ceph, line=False).poly([(22, 30), (28, 30), (25, 38)])
    if kind == 'jumper':
        a.part('E').ell(14, 32, 22, 42)
        a.eye(18, 35, 2, 'big')
        a.eye(23, 33, 1)
    else:
        a.eye(18, 34, 1)
        a.eye(21, 33, 1)


def scorpion(a, sp, r):
    """Scorpion. A body, B claws, C stinger."""
    a.part('A').curve((40, 40), (62, 40), (52, 16), 4, 2.5)
    a.part('C').poly([(50, 16), (44, 14), (48, 20)])
    legs = a.part('A')
    for x in (22, 28, 34, 40):
        legs.line([(x, 42), (x - 4, 54)], 1.4)
    a.part('A').blob([(14, 38), (22, 32), (44, 34), (46, 42), (22, 46)])
    a.part('B').line([(16, 38), (8, 30)], 3).line([(16, 42), (8, 48)], 3)
    a.part('B').blob([(2, 24), (10, 26), (10, 34), (0, 30)]).blob([(2, 44), (10, 44), (10, 52), (0, 50)])
    a.eye(16, 37, 1)


def tick(a, sp, r):
    """Tick or mite. A body, B shield, C spot (lone star), D hairs. kind: tick, mite (rounder), facemite (worm-like)."""
    kind = sp.get('kind', 'tick')
    if kind == 'facemite':
        a.part('A').blob([(10, 28), (30, 24), (60, 30), (30, 36), (10, 36)])
        legs = a.part('A')
        for x in (12, 16, 20, 24):
            legs.line([(x, 34), (x - 2, 40)], 1.2)
        a.eye(9, 30, 1)
        return
    legs = a.part(sp.get('legrole', 'A'))
    for i, ang in enumerate((-50, -15, 20, 55)):
        t = math.radians(ang)
        legs.line([(30, 36), (30 - 22 * math.cos(t), 36 + 16 * math.sin(t))], 1.6)
        legs.line([(34, 36), (34 + 22 * math.cos(t), 36 + 16 * math.sin(t))], 1.6)
    body = a.part('A').ell(18, 22, 46, 52) if kind == 'tick' else a.part('A').circle(32, 36, 13)
    if kind == 'tick':
        a.part('B', clip=body).ell(18, 20, 46, 34)
    if sp.get('star'):
        a.part('C').circle(32, 28, 2)
    if sp.get('hairs'):
        h = a.part('D')
        for k in range(8):
            t = k * math.pi / 4
            h.line([(32 + 13 * math.cos(t), 36 + 13 * math.sin(t)), (32 + 19 * math.cos(t), 36 + 19 * math.sin(t))], .8)
    a.part('A').poly([(28, 22), (32, 14), (36, 22)])


def myriapod(a, sp, r):
    """Centipede / millipede / velvet worm. A body, B segment bands, C legs/spots. kind: house (long legs), desert, millipede, velvet."""
    kind = sp.get('kind', 'desert')
    pts = [(8 + i * 6, 34 + 4 * math.sin(i * .9)) for i in range(9)]
    legs = a.part('C' if kind != 'house' else 'A')
    L = 14 if kind == 'house' else (6 if kind in ('millipede', 'velvet') else 8)
    for (x, y) in pts[1:]:
        legs.line([(x, y), (x - 3, y + L)], 1 if kind != 'velvet' else 2)
        if kind == 'house':
            legs.line([(x, y), (x - 4, y - L)], 1)
    body = a.part('A')
    for (x, y) in pts:
        body.circle(x, y, 4 if kind != 'millipede' else 4.5)
    if kind != 'velvet':
        b = a.part('B', clip=body, line=False)
        for (x, y) in pts[1::2]:
            b.rect(x - 1.5, y - 8, x + 1.5, y + 8)
    a.part('A').curve(pts[0], (0, 22), (6, 14), 1, .8)
    a.eye(pts[0][0] - 1, pts[0][1] - 1, 1)


def crab(a, sp, r):
    """Crab. A shell, B claws, C hair/spots. kind: crab, yeti (hairy white claws), horseshoe."""
    kind = sp.get('kind', 'crab')
    if kind == 'horseshoe':
        a.part('A').line([(32, 44), (32, 62)], 2)
        sh = a.part('A').blob([(4, 40), (12, 20), (32, 14), (52, 20), (60, 40), (32, 46)])
        a.part('B', clip=sh).blob([(14, 40), (20, 22), (44, 22), (50, 40)])
        a.eye(22, 26, 1)
        a.eye(42, 26, 1)
        return
    legs = a.part('A')
    for i in range(3):
        y = 38 + i * 4
        legs.line([(20, y), (8, y + 6), (4, y + 14)], 2).line([(44, y), (56, y + 6), (60, y + 14)], 2)
    claw_role = 'B'
    a.part(claw_role).line([(18, 34), (8, 24)], 3.5).line([(46, 34), (56, 24)], 3.5)
    a.part(claw_role).blob([(2, 14), (12, 16), (12, 26), (2, 24)]).blob([(52, 16), (62, 14), (62, 24), (52, 26)])
    if kind == 'yeti':
        h = a.part('C')
        for x in (2, 6, 10, 54, 58, 62):
            h.line([(x, 24), (x, 32)], 1.2)
    a.part('A').blob([(12, 38), (20, 28), (44, 28), (52, 38), (44, 48), (20, 48)])
    a.part('A').line([(28, 30), (26, 22)], 1).line([(36, 30), (38, 22)], 1)
    a.eye(26, 22, 1)
    a.eye(38, 22, 1)


def lobster(a, sp, r):
    """Lobster / spiny lobster. A shell, B claws/legs, C spots. spiny=True: no big claws, long antennae."""
    spiny = sp.get('spiny', False)
    a.part('A').poly([(54, 34), (63, 26), (63, 42)])
    body = a.part('A').taper([(14, 34), (28, 34), (42, 35), (54, 34)], 10, 7)
    s = a.part('A', clip=body)
    for x in (38, 44, 50):
        s.rect(x, 20, x + .8, 50)
    legs = a.part('B')
    for x in (22, 28, 34):
        legs.line([(x, 38), (x - 4, 50)], 1.4)
    if spiny:
        a.part('B').curve((10, 30), (0, 14), (10, 2), 2, 1).curve((10, 32), (2, 22), (0, 8), 2, 1)
        sp_ = a.part('C', clip=body, line=False)
        for _ in range(8):
            x, y = 16 + 34 * next(r), 30 + 8 * next(r)
            sp_.circle(x, y, 1)
    else:
        a.part('B').line([(14, 36), (6, 46)], 3).blob([(0, 44), (10, 44), (8, 56), (0, 54)])
        a.part('B').line([(14, 30), (6, 22)], 3).blob([(0, 12), (10, 16), (8, 24), (0, 22)])
        a.part('A').curve((8, 32), (0, 26), (2, 6), 1, .8)
    a.part('A').ell(6, 28, 20, 40)
    a.eye(10, 31, 1)


def barnacle(a, sp, r):
    """Acorn barnacles on rock. A shell plates, B rock, C opening/feathery cirri."""
    a.part('B').rect(0, 48, 64, 64)
    for (x, y, s) in [(18, 44, 10), (38, 42, 12), (52, 48, 7), (8, 50, 6)]:
        a.part('A').poly([(x - s, y + 6), (x - s * .5, y - s * .6), (x + s * .5, y - s * .6), (x + s, y + 6)])
        a.part('C').ell(x - s * .4, y - s * .8, x + s * .4, y - s * .3)
    a.part('C').curve((38, 34), (44, 24), (50, 26), 1, .8).curve((38, 34), (40, 22), (46, 18), 1, .8)


def isopod(a, sp, r):
    """Giant isopod. A segmented shell, B legs."""
    legs = a.part('B')
    for x in range(14, 52, 6):
        legs.line([(x, 44), (x - 2, 54)], 1.6)
    body = a.part('A').blob([(6, 40), (12, 26), (32, 22), (54, 26), (60, 40), (32, 48)])
    s = a.part('A', clip=body)
    for x in range(14, 56, 6):
        s.rect(x, 16, x + 1, 50)
    a.part('A').curve((8, 32), (0, 26), (2, 16), 1.2, .8)
    a.eye(10, 32, 2, 'pale')


def microcrust(a, sp, r):
    """Tiny crustaceans: water flea, sea-monkey, sea sapphire, phyllosoma. A body, B appendages, C gut/shine, E eye."""
    kind = sp.get('kind', 'flea')
    if kind == 'flea':
        body = a.part('A').blob([(14, 30), (30, 18), (50, 26), (50, 46), (30, 54), (16, 44)])
        a.part('C', clip=body, line=False).curve((26, 28), (40, 36), (34, 48), 3, 2)
        a.part('B').curve((20, 26), (8, 16), (4, 10), 2, 1.5).curve((20, 26), (10, 8), (14, 2), 2, 1.5)
        a.part('K').circle(18, 28, 3)
    elif kind == 'monkey':
        a.part('A').taper([(12, 34), (30, 34), (46, 38), (60, 34)], 6, 2)
        legs = a.part('B')
        for x in range(16, 40, 4):
            legs.line([(x, 36), (x - 2, 44)], 1.2)
        a.part('K').circle(10, 30, 2).circle(14, 28, 2)
    elif kind == 'sapphire':
        body = a.part('A').ell(10, 26, 54, 42)
        a.part('C', clip=body, line=False).ell(14, 28, 40, 34)
        a.part('B').line([(54, 34), (62, 30)], 1.5).line([(54, 34), (62, 38)], 1.5)
        a.part('K').circle(14, 32, 1.5)
    else:  # phyllosoma: flat glassy leaf larva
        body = a.part('A').ell(14, 20, 50, 50)
        legs = a.part('B')
        for ang in range(0, 360, 45):
            t = math.radians(ang)
            legs.line([(32 + 16 * math.cos(t), 35 + 14 * math.sin(t)), (32 + 28 * math.cos(t), 35 + 26 * math.sin(t))], 1)
        a.part('K').circle(28, 22, 1.5).circle(36, 22, 1.5)


def slug(a, sp, r):
    """Slug (banana slug). A body, D spots, C foot rim."""
    body = a.part('A').blob([(4, 44), (12, 34), (26, 30), (44, 32), (62, 44), (56, 50), (8, 50)])
    a.part('A', clip=body).ell(14, 28, 34, 44)
    a.part('C', clip=body, line=False).rect(0, 48, 64, 52)
    if sp.get('spots'):
        s = a.part('D', clip=body, line=False)
        for _ in range(9):
            x, y = 14 + 44 * next(r), 34 + 12 * next(r)
            s.ell(x - 1.6, y - 1.2, x + 1.6, y + 1.2)
    a.part('A').line([(10, 36), (4, 24)], 2).line([(14, 34), (12, 22)], 2)
    a.part('K').circle(4, 24, 1.2).circle(12, 22, 1.2)
    a.part('A').line([(6, 44), (2, 48)], 1.2)


def snail(a, sp, r):
    """Snail. A body, B shell, D shell bands, C sclerites (scaly-foot)."""
    body = a.part('A').blob([(2, 50), (10, 40), (40, 42), (62, 50), (54, 54), (6, 54)])
    a.part('A').line([(10, 42), (4, 30)], 2).line([(14, 42), (12, 30)], 2)
    a.part('K').circle(4, 30, 1.2).circle(12, 30, 1.2)
    shell = a.part('B').circle(38, 32, 15)
    d = a.part('D', clip=shell, line=False)
    pts = [(38 + (12 - k * .9) * math.cos(k * .6), 32 + (12 - k * .9) * math.sin(k * .6)) for k in range(14)]
    d.taper(pts, 2, 1)
    if sp.get('scales'):
        c = a.part('C', clip=body, line=False)
        for x in range(10, 60, 4):
            c.rect(x, 48, x + 2, 54)


def octopus(a, sp, r):
    """Octopus / squid. A body, B suckers/arm web, C spots/glow, E eye. kind: octopus, dumbo, glass, blanket, telescope, vampire, squid, bigfin."""
    kind = sp.get('kind', 'octopus')
    if kind in ('squid', 'bigfin'):
        if kind == 'bigfin':
            arms = a.part('A')
            for k in range(6):
                arms.curve((32, 40), (20 + k * 5, 52), (14 + k * 7, 64), 1.2, .8)
            mantle = a.part('A').blob([(26, 40), (24, 14), (32, 6), (40, 14), (38, 40)])
            a.part('A').ell(10, 6, 54, 20)
            a.eye(30, 34, 1)
            a.eye(35, 34, 1)
            return
        arms = a.part('A')
        for k in range(6):
            arms.curve((18, 34), (6, 26 + k * 3), (0, 20 + k * 5), 2, 1)
        mantle = a.part('A').blob([(16, 30), (32, 26), (54, 28), (62, 34), (54, 40), (32, 42), (16, 38)])
        a.part('A').poly([(52, 26), (60, 18), (62, 34)]).poly([(52, 42), (60, 50), (62, 34)])
        a.part('C', clip=mantle, line=False).ell(20, 36, 60, 48)
        a.eye(20, 32, 2, 'big')
        return
    web = kind in ('vampire', 'blanket')
    arms = a.part('A')
    for k in range(8):
        x0 = 18 + k * 4
        arms.curve((x0, 38), (x0 - 10 + k * 2, 52), (x0 - 16 + k * 5, 60 - (k % 2) * 4), 3, 1.2)
    if web:
        a.part('B').blob([(8, 40), (56, 40), (60, 56), (32, 50), (4, 56)])
    mantle = a.part('A').blob([(14, 34), (18, 12), (32, 4), (46, 12), (50, 34), (32, 42)])
    if kind == 'dumbo':
        a.part('A').ell(4, 10, 16, 20).ell(48, 10, 60, 20)
    if sp.get('spots'):
        s = a.part('C', clip=mantle, line=False)
        for _ in range(8):
            x, y = 18 + 28 * next(r), 8 + 26 * next(r)
            s.circle(x, y, 1.1)
    if kind == 'telescope':
        a.part('E').ell(20, 28, 26, 38).ell(38, 28, 44, 38)
        a.eye(23, 30, 1)
        a.eye(41, 30, 1)
        return
    style = 'red' if kind == 'vampire' else 'big'
    a.eye(24, 30, 2, style)
    a.eye(40, 30, 2, style)


def chiton(a, sp, r):
    """Chiton from above: eight plates. A plates, B girdle, C plate highlights."""
    a.part('B').ell(6, 18, 58, 48)
    pl = a.part('A')
    for i in range(8):
        x = 10 + i * 6
        pl.ell(x, 22, x + 6, 44)
    h = a.part('C', line=False)
    for i in range(8):
        h.rect(12 + i * 6, 32, 14 + i * 6, 34)


def bivalve(a, sp, r):
    """Oyster / clam. A shell, B ridges, C pearly interior."""
    sh = a.part('A').blob([(6, 44), (12, 22), (32, 12), (54, 22), (60, 44), (32, 52)])
    b = a.part('B', clip=sh, line=False)
    for k in range(-3, 4):
        b.line([(32, 50), (32 + k * 9, 10)], 1.2)
    a.part('C').blob([(10, 46), (32, 42), (56, 46), (32, 54)])


def spiral(a, sp, r):
    """Ammonite / argonaut: spiral shell with tentacles. A shell, B ribs, C body/arms."""
    shell = a.part('A').circle(36, 32, 20)
    b = a.part('B', clip=shell, line=False)
    pts = [(36 + (17 - k * 1.1) * math.cos(k * .55), 32 + (17 - k * 1.1) * math.sin(k * .55)) for k in range(16)]
    b.taper(pts, 2.5, 1)
    for k in range(0, 360, 30):
        t = math.radians(k)
        b.line([(36 + 12 * math.cos(t), 32 + 12 * math.sin(t)), (36 + 20 * math.cos(t), 32 + 20 * math.sin(t))], .8)
    arms = a.part('C')
    for k in range(5):
        arms.curve((18, 40), (8, 42 + k * 2), (2, 46 + k * 3), 1.6, 1)
    a.part('C').ell(12, 34, 24, 46)
    a.eye(16, 38, 1)


def jelly(a, sp, r):
    """Jellyfish. A bell, B oral arms, C gonad rings/rim, E glow. kind: moon, lionsmane, atolla, phantom, deepstaria, ephyra."""
    kind = sp.get('kind', 'moon')
    if kind == 'ephyra':
        e = a.part('A')
        for k in range(8):
            t = math.radians(k * 45)
            e.line([(32, 32), (32 + 18 * math.cos(t), 32 + 18 * math.sin(t))], 6)
        a.part('C').circle(32, 32, 5)
        return
    if kind == 'deepstaria':
        a.part('A').blob([(4, 50), (10, 14), (32, 6), (54, 14), (60, 50), (32, 58)])
        n = a.part('C', line=False)
        for k in range(6):
            n.line([(10 + k * 9, 16), (6 + k * 10, 54)], .7)
        return
    arms = a.part('B')
    long = kind in ('lionsmane', 'phantom')
    for k in range(5):
        x = 20 + k * 6
        arms.curve((x, 30), (x - 6 + (k % 2) * 12, 44), (x - 4, 62 if long else 52), 3 if kind == 'phantom' else 1.5, 1)
    if kind == 'lionsmane':
        t = a.part('B')
        for k in range(9):
            x = 10 + k * 5
            t.line([(x, 30), (x + (k % 3) - 1, 62)], .7)
    bell = a.part('A').blob([(6, 32), (12, 14), (32, 6), (52, 14), (58, 32), (32, 36)])
    if kind == 'moon':
        c = a.part('C', clip=bell, line=False)
        for (x, y) in ((22, 20), (32, 16), (42, 20), (32, 26)):
            c.circle(x, y, 3.5)
    if kind == 'atolla':
        a.part('C', clip=bell, line=False).ell(16, 10, 48, 28)
        g = a.part('E')
        for k in range(9):
            g.circle(8 + k * 6, 33, 1.2)


def polyp(a, sp, r):
    """Polyp on a stalk (moon jelly polyp). A stalk, B tentacles."""
    a.part('C').rect(16, 56, 48, 64)
    a.part('A').taper([(32, 58), (32, 40), (32, 28)], 4, 7)
    t = a.part('B')
    for k in range(9):
        ang = math.radians(200 + k * 17.5)
        t.curve((32, 26), (32 + 12 * math.cos(ang), 26 + 12 * math.sin(ang)), (32 + 20 * math.cos(ang), 24 + 14 * math.sin(ang)), 1.2, .8)
    a.part('A').ell(25, 22, 39, 30)


def floatjelly(a, sp, r):
    """Portuguese man o' war (float + tentacles) or giant siphonophore (chain). A float, B tentacles, C crest."""
    if sp.get('chain'):
        ch = a.part('A')
        for k in range(10):
            ch.circle(6 + k * 6, 30 + 6 * math.sin(k * .7), 3.5)
        t = a.part('B')
        for k in range(10):
            x, y = 6 + k * 6, 30 + 6 * math.sin(k * .7)
            t.line([(x, y), (x + 1, y + 16)], .7)
        return
    t = a.part('B')
    for k in range(7):
        x = 20 + k * 4
        t.curve((x, 36), (x - 4, 48), (x + 2, 64), 1.2, .8)
    a.part('A').blob([(8, 36), (14, 22), (40, 18), (56, 26), (50, 38), (20, 40)])
    a.part('C').blob([(16, 22), (24, 12), (44, 12), (52, 24)])


def worm(a, sp, r):
    """Worms. A body, B plume/bands, C tube. kind: earth, tube (Riftia), pompeii, xmas, boneeater."""
    kind = sp.get('kind', 'earth')
    if kind == 'earth':
        body = a.part('A').taper([(6, 44), (16, 36), (30, 42), (44, 34), (58, 40)], 6, 5)
        a.part('B', clip=body, line=False).rect(18, 30, 24, 50)
        return
    if kind == 'xmas':
        a.part('C').rect(0, 52, 64, 64)
        for cx in (22, 42):
            sp_ = a.part('A')
            for k in range(6):
                w = 3 + k * 2
                sp_.ell(cx - w, 14 + k * 6, cx + w, 18 + k * 6)
            a.part('B', clip=sp_, line=False).rect(0, 0, 64, 64) if False else None
        return
    if kind == 'boneeater':
        a.part('C').blob([(4, 56), (20, 44), (60, 46), (62, 60), (2, 62)])
        p = a.part('A')
        for x in (20, 30, 40, 48):
            p.line([(x, 46), (x + 2, 30)], 1.6)
            p.circle(x + 2, 28, 2.2)
        return
    if kind == 'pompeii':
        a.part('C').rect(18, 20, 46, 64)
        a.part('A').ell(20, 10, 44, 26)
        h = a.part('B')
        for k in range(10):
            h.line([(22 + k * 2.4, 22), (20 + k * 2.6, 34)], .7)
        return
    # tube worm
    tubes = a.part('C')
    for x in (16, 32, 46):
        tubes.rect(x - 4, 26, x + 4, 64)
    pl = a.part('A')
    for x in (16, 32, 46):
        pl.ell(x - 7, 14, x + 7, 30)


def seacuc(a, sp, r):
    """Swimming sea cucumber (headless chicken monster). A body, B veil, C gut."""
    a.part('B').blob([(4, 28), (14, 14), (24, 22), (14, 34)])
    body = a.part('A').blob([(14, 24), (32, 18), (56, 28), (52, 44), (30, 46), (16, 38)])
    a.part('C', clip=body, line=False).curve((20, 32), (36, 40), (52, 34), 3, 2)
    a.part('B').blob([(50, 36), (62, 40), (58, 52), (46, 46)])


def sponge(a, sp, r):
    """Harp sponge: vertical branches on a base. A branches, C tips."""
    a.part('A').rect(8, 50, 56, 54).rect(10, 44, 54, 50)
    v = a.part('A')
    for x in range(12, 56, 6):
        v.line([(x, 48), (x, 12)], 2)
    a.part('C').rect(10, 9, 54, 11)


def pyrosome(a, sp, r):
    """Pyrosome: a glowing tube colony. A tube, E zooid glow."""
    tube = a.part('A').blob([(4, 28), (20, 22), (56, 24), (62, 32), (56, 40), (20, 42), (4, 36)])
    g = a.part('E', clip=tube, line=False)
    for _ in range(26):
        x, y = 8 + 52 * next(r), 24 + 16 * next(r)
        g.circle(x, y, .9)
    a.part('K').ell(2, 28, 8, 36)


def burgess(a, sp, r):
    """Burgess Shale and other Cambrian/odd fossils. kind: anomalocaris, opabinia, hallucigenia, pikaia, tully."""
    kind = sp.get('kind', 'anomalocaris')
    if kind == 'anomalocaris':
        a.part('A').poly([(52, 34), (63, 24), (60, 34), (63, 44)])
        body = a.part('A').blob([(10, 34), (20, 24), (50, 26), (56, 34), (50, 42), (20, 44)])
        fl = a.part('B', clip=None)
        for x in range(18, 52, 6):
            fl.ell(x - 3, 20, x + 3, 28).ell(x - 3, 40, x + 3, 48)
        a.part('A').curve((10, 36), (0, 40), (4, 52), 2.5, 1.5)
        a.part('A').curve((10, 32), (0, 28), (4, 16), 2.5, 1.5)
        a.part('E').line([(14, 28), (12, 22)], 1.2).circle(12, 20, 2.2)
        return
    if kind == 'opabinia':
        a.part('A').poly([(52, 34), (62, 26), (60, 34), (62, 42)])
        body = a.part('A').blob([(14, 34), (22, 28), (52, 30), (56, 34), (52, 38), (22, 40)])
        fl = a.part('B')
        for x in range(22, 52, 5):
            fl.ell(x - 2.5, 26, x + 2.5, 31).ell(x - 2.5, 37, x + 2.5, 42)
        a.part('A').curve((14, 36), (4, 44), (2, 54), 1.2, 1)
        a.part('A').poly([(0, 52), (6, 54), (2, 58)])
        e = a.part('E')
        for x in (14, 17, 20, 23, 26):
            e.circle(x, 27, 1.6)
        return
    if kind == 'hallucigenia':
        body = a.part('A').taper([(8, 40), (30, 38), (58, 40)], 4, 3)
        sp_ = a.part('B')
        for x in range(16, 56, 6):
            sp_.line([(x, 38), (x + 1, 22)], 1.6)
        legs = a.part('A')
        for x in range(16, 56, 6):
            legs.line([(x, 41), (x - 1, 54)], 1.4)
        a.part('A').circle(6, 40, 3)
        return
    if kind == 'pikaia':
        body = a.part('A').blob([(4, 34), (16, 28), (50, 30), (62, 34), (50, 38), (16, 40)])
        b = a.part('B', clip=body, line=False)
        for x in range(12, 60, 4):
            b.line([(x, 28), (x - 2, 40)], .7)
        a.part('A').line([(6, 32), (2, 28)], .8).line([(6, 32), (4, 26)], .8)
        return
    # tully monster
    a.part('A').poly([(52, 34), (62, 24), (60, 34), (62, 44)])
    body = a.part('A').blob([(18, 34), (26, 28), (52, 30), (56, 34), (52, 38), (26, 40)])
    s = a.part('B', clip=body, line=False)
    for x in range(26, 54, 4):
        s.rect(x, 26, x + 1, 42)
    a.part('A').line([(28, 32), (28, 18)], 1.2).line([(18, 34), (4, 34)], 2)
    a.part('A').ell(24, 14, 32, 20)
    a.part('B').poly([(0, 32), (6, 34), (0, 37)])
    a.eye(24, 17, 1)
    a.eye(32, 17, 1)


def seastar(a, sp, r):
    """Sea star seen from above. arms: count (5 ochre, 20 sunflower). A arms, B centre, C spots."""
    import math
    n = sp.get('arms', 5)
    cx, cy = 32, 34
    long_r = 27 if n <= 6 else 25
    w = 7 if n <= 6 else 3.2
    arms = a.part('A')
    for i in range(n):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        arms.taper([(cx, cy), (cx + long_r * math.cos(ang), cy + long_r * math.sin(ang))], w, 1.5)
    a.part('B').circle(cx, cy, 8 if n <= 6 else 10)
    if sp.get('spots'):
        sp_ = a.part('C', line=False)
        for _ in range(14):
            ang, d = 2 * math.pi * next(r), 4 + 18 * next(r)
            sp_.circle(cx + d * math.cos(ang), cy + d * math.sin(ang), 1)


def urchin(a, sp, r):
    """Sea urchin: a round test bristling with spines. A spines, B body."""
    import math
    cx, cy = 32, 38
    sp_ = a.part('A')
    for i in range(28):
        ang = math.pi + math.pi * i / 27 + 0.05 * (next(r) - .5)
        sp_.line([(cx, cy), (cx + 26 * math.cos(ang), cy + 22 * math.sin(ang))], 1.6)
    for i in range(6):
        ang = 0.2 + 2.7 * i / 5
        sp_.line([(cx, cy), (cx + 24 * math.cos(ang), cy + 10 * math.sin(ang))], 1.6)
    a.part('B').ell(cx - 15, cy - 11, cx + 15, cy + 11)
