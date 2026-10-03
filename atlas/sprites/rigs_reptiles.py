"""Reptile, amphibian and fossil-vertebrate rigs."""


def turtle(a, sp, r):
    """Turtle. A shell, B skin, C plastron/shell rim, D scute lines. sea=True: flippers; hatchling smaller."""
    sea = sp.get('sea', True)
    sc = .7 if sp.get('hatchling') else 1.0
    ox, oy = (12, 12) if sc < 1 else (0, 0)
    S = lambda x, y: (ox + x * sc, oy + y * sc)
    if sea:
        a.part('B').poly([S(20, 38), S(4, 50), S(10, 54), S(28, 44)]).poly([S(44, 40), S(58, 50), S(54, 54), S(40, 44)])
    else:
        a.part('B').line([S(20, 42), S(18, 52)], 5 * sc).line([S(44, 42), S(46, 52)], 5 * sc)
        a.part('B').poly([S(50, 38), S(60, 40), S(50, 42)])
    shell = a.part('A').blob([S(12, 40), S(18, 24), S(32, 18), S(48, 24), S(54, 40), S(32, 46)])
    if sp.get('ridges'):
        for x in (24, 32, 40):
            a.part('D', clip=shell, line=False).rect(*S(x, 16), *S(x + 1.5, 46))
    else:
        sc_part = a.part('D', clip=shell, line=False)
        for (x, y) in [(24, 28), (32, 25), (40, 28), (28, 36), (38, 36)]:
            px, py = S(x, y)
            sc_part.ell(px - 3 * sc, py - 3 * sc, px + 3 * sc, py + 3 * sc)
    a.part('C', clip=shell, line=False).rect(*S(0, 41), *S(64, 48))
    head = a.part('B').blob([S(2, 34), S(6, 28), S(14, 30), S(16, 38), S(8, 40)])
    if sp.get('beak'):
        a.part('B').poly([S(2, 34), S(0, 39), S(5, 37)])
    ex, ey = S(7, 32)
    a.eye(ex, ey, 1)


def snake(a, sp, r):
    """Coiled snake. A body, B bands/diamonds, C belly, D third band colour, E tongue. pattern: bands, diamonds, rings, blotch, none."""
    pat = sp.get('pattern', 'none')
    body = a.part('A')
    body.taper([(56, 56), (40, 56), (22, 54), (14, 46), (22, 38), (42, 38), (50, 30), (44, 22), (28, 20)], 7, 5)
    if pat != 'none':
        b = a.part('B', clip=body, line=False)
        if pat == 'diamonds':
            for (x, y) in [(46, 56), (30, 55), (17, 47), (28, 38), (44, 37), (48, 26), (36, 20)]:
                b.poly([(x - 3, y), (x, y - 3), (x + 3, y), (x, y + 3)])
        elif pat in ('bands', 'rings', 'coral'):
            for x in range(10, 60, 6):
                b.rect(x, 0, x + 3, 64)
            if pat == 'coral':
                d = a.part('D', clip=body, line=False)
                for x in range(13, 60, 12):
                    d.rect(x, 0, x + 2, 64)
        else:
            for (x, y) in [(48, 56), (32, 55), (18, 46), (34, 38), (48, 30)]:
                b.circle(x, y, 2.4)
    if sp.get('rattle'):
        a.part('C').line([(56, 56), (62, 54)], 3.5)
    if sp.get('horns'):
        a.part('A').poly([(24, 14), (26, 10), (28, 15)])
    head = a.part('A').blob([(14, 16), (26, 14), (30, 20), (24, 24), (14, 22)])
    a.part('E').line([(14, 20), (8, 21)], .8)
    a.eye(20, 17, 1)


def lizard(a, sp, r):
    """Lizard. A body, B pattern, C belly, D crest/spikes. kind: iguana, horned, gila, basilisk."""
    kind = sp.get('kind', 'iguana')
    stout = kind in ('horned', 'gila')
    a.part('A').taper([(46, 40), (56, 44), (62, 52), (64, 58)], 5 if stout else 4, 1.5)
    a.part('A').line([(18, 42), (14, 52)], 3.5).line([(40, 42), (44, 52)], 3.5)
    body = a.part('A').blob([(12, 38), (20, 30), (40, 30), (50, 38), (40, 46), (20, 46)] if stout else
                            [(14, 38), (22, 32), (40, 32), (48, 38), (40, 44), (20, 44)])
    a.part('C', clip=body, line=False).rect(0, 43, 64, 50)
    if kind == 'gila':
        b = a.part('B', clip=body, line=False)
        for x in range(16, 50, 7):
            b.blob([(x, 30), (x + 4, 32), (x + 3, 40), (x - 1, 38)], 1)
    if kind == 'horned':
        sp_ = a.part('D')
        for x in range(18, 46, 5):
            sp_.poly([(x, 32), (x + 1.5, 27), (x + 3, 32)])
    if kind in ('iguana', 'basilisk'):
        cr = a.part('D')
        for x in range(16, 46, 4):
            cr.poly([(x, 33), (x + 2, 25 if kind == 'basilisk' else 28), (x + 4, 33)])
    a.part('A').line([(22, 44), (18, 54)], 3.5).line([(44, 42), (48, 52)], 3.5)
    head = a.part('A').blob([(2, 36), (6, 30), (16, 30), (18, 38), (8, 42)])
    if kind == 'iguana':
        a.part('C').ell(8, 38, 16, 46)
    if kind == 'horned':
        a.part('D').poly([(10, 30), (14, 22), (16, 31)]).poly([(14, 30), (20, 24), (19, 33)])
    if kind == 'basilisk':
        a.part('D').poly([(10, 31), (18, 20), (18, 32)])
    a.eye(9, 34, 1)


def crocodilian(a, sp, r):
    """Alligator. A hide, B scutes, C belly."""
    a.part('A').taper([(44, 40), (54, 42), (62, 46)], 7, 2)
    a.part('A').line([(20, 44), (16, 52)], 4).line([(38, 44), (42, 52)], 4)
    body = a.part('A').blob([(10, 40), (16, 32), (44, 32), (50, 40), (44, 48), (16, 48)])
    sc = a.part('B', clip=body, line=False)
    for x in range(16, 46, 4):
        sc.rect(x, 31, x + 2, 34)
    a.part('C', clip=body, line=False).rect(0, 45, 64, 50)
    a.part('A').blob([(0, 38), (10, 34), (16, 36), (16, 42), (0, 42)])
    a.part('W').rect(2, 41, 12, 42)
    a.part('A').line([(24, 46), (20, 54)], 4).line([(44, 44), (48, 52)], 4)
    a.eye(12, 34, 1)


def frog(a, sp, r):
    """Frog or toad. A skin, B legs/pattern, C belly, D spots, E eye colour. kind: tree, dart, toad, glass, harlequin."""
    kind = sp.get('kind', 'tree')
    a.part('A').blob([(36, 44), (54, 40), (60, 52), (44, 56)])
    body = a.part('A').blob([(10, 40), (18, 26), (36, 24), (48, 34), (44, 50), (16, 52)])
    a.part('C', clip=body, line=False).ell(8, 42, 40, 58)
    if sp.get('spots'):
        s = a.part('D', clip=body, line=False)
        for _ in range(9):
            x, y = 14 + 30 * next(r), 26 + 20 * next(r)
            s.circle(x, y, 1.6 if kind != 'harlequin' else 2.5)
    if sp.get('sides'):
        a.part('B', clip=body, line=False).rect(18, 36, 46, 40)
    a.part(sp.get('legrole', 'A')).line([(16, 46), (10, 56)], 3).line([(40, 48), (34, 58)], 3)
    a.part(sp.get('legrole', 'A')).ell(6, 54, 14, 58).ell(30, 56, 38, 60)
    head = a.part('A').blob([(4, 32), (10, 22), (26, 22), (28, 32), (16, 38), (6, 38)])
    if kind == 'toad':
        a.eye(13, 25, 1)
        return
    a.part('A').circle(12, 22, 4.5).circle(22, 22, 4.5)
    a.part('E').circle(12, 22, 3.2).circle(22, 22, 3.2)
    a.part('K').rect(10, 21.2, 14, 22.8).rect(20, 21.2, 24, 22.8)


def newt(a, sp, r):
    """Newt. A skin, D spots (ringed), C belly."""
    a.part('A').taper([(42, 40), (52, 42), (62, 38)], 5, 2)
    a.part('A').line([(18, 42), (14, 50)], 2.5).line([(36, 42), (40, 50)], 2.5)
    body = a.part('A').blob([(12, 38), (20, 32), (40, 34), (46, 40), (38, 46), (18, 46)])
    a.part('C', clip=body, line=False).rect(0, 43, 64, 50)
    s = a.part('D', clip=body, line=False)
    for x in (20, 28, 36):
        s.circle(x, 37, 1.3)
    head = a.part('A').blob([(2, 38), (6, 32), (16, 33), (16, 40), (6, 42)])
    a.eye(8, 36, 1)


def dinosaur(a, sp, r):
    """Fossil reptiles. kind: rex, ankylo (Borealopelta), plesio (Elasmosaurus), ptero (Pteranodon). A skin, B armour/wing, C belly, D spikes/crest."""
    kind = sp.get('kind', 'rex')
    if kind == 'ptero':
        w = a.part('B').poly([(30, 30), (2, 20), (4, 28), (30, 40)]).poly([(32, 30), (62, 20), (60, 28), (34, 40)])
        a.part('A').ell(24, 26, 40, 40)
        a.part('A').circle(20, 26, 5)
        a.part('A').poly([(18, 24), (4, 28), (18, 28)])
        a.part('D').poly([(22, 22), (34, 14), (26, 24)])
        a.eye(19, 25, 1)
        return
    if kind == 'plesio':
        a.part('A').poly([(20, 44), (8, 52), (20, 48)]).poly([(40, 44), (52, 54), (44, 46)])
        body = a.part('A').ell(20, 32, 54, 50)
        a.part('C', clip=body, line=False).rect(0, 45, 64, 52)
        a.part('A').taper([(52, 42), (62, 44)], 4, 1.5)
        a.part('A').curve((24, 38), (8, 30), (12, 8), 5, 3.5)
        a.part('A').ell(6, 4, 18, 11)
        a.eye(10, 6, 1)
        return
    if kind == 'ankylo':
        a.part('A').taper([(44, 40), (54, 42), (62, 44)], 6, 3)
        a.part('B').circle(60, 44, 3.5)
        a.part('A').line([(18, 44), (16, 56)], 5).line([(40, 44), (42, 56)], 5)
        body = a.part('B').blob([(8, 42), (14, 26), (34, 22), (52, 30), (50, 44), (14, 48)])
        sp_ = a.part('D')
        for x in range(14, 50, 7):
            sp_.poly([(x, 28), (x + 2, 22), (x + 4, 28)])
        a.part('A').blob([(0, 38), (6, 32), (14, 34), (14, 42), (4, 44)])
        a.eye(6, 37, 1)
        return
    # rex
    a.part('A').taper([(40, 36), (52, 38), (62, 44)], 9, 2)
    a.part('A').line([(30, 44), (28, 58)], 6).line([(38, 44), (40, 58)], 6)
    body = a.part('A').blob([(14, 30), (24, 22), (40, 26), (46, 38), (36, 48), (20, 44)])
    a.part('C', clip=body, line=False).ell(12, 36, 34, 52)
    a.part('A').line([(20, 36), (16, 40)], 2)
    head = a.part('A').blob([(0, 16), (8, 8), (26, 10), (28, 20), (18, 26), (2, 26)])
    a.part('W').rect(2, 22, 16, 23)
    a.part('K').rect(1, 23, 18, 24)
    a.eye(18, 14, 1)
