"""Mammal rigs. Each draws facing left on the 64x64 grid. sp is the species spec (params), r an RNG."""


def _legs(a, role, xs, y0, y1, w=4.5, paw=None):
    p = a.part(role)
    for x in xs:
        p.line([(x, y0), (x, y1)], w)
    if paw:
        q = a.part(paw)
        for x in xs:
            q.ell(x - w / 2 - .5, y1 - 2, x + w / 2 + 1, y1 + 1)
    return p


def canid(a, sp, r):
    """Fox / wolf. A coat, B legs and ear backs, C chest/cheek/tail tip, D muzzle tip."""
    fox = sp.get('fox', False)
    legrole = 'B' if sp.get('socks') else 'A'
    _legs(a, legrole, [22, 44], 40, 57, 4)
    tail = a.part('A')
    if fox:
        tail.blob([(48, 32), (58, 24), (63, 30), (62, 42), (56, 46), (50, 40)])
    else:
        tail.blob([(48, 32), (56, 34), (61, 44), (58, 50), (53, 46), (49, 38)])
    if sp.get('tailtip'):
        a.part('C', clip=tail).ell(56, 36, 66, 50)
    body = a.part('A').blob([(16, 30), (30, 24), (48, 26), (54, 34), (50, 44), (32, 46), (18, 44)])
    a.part('C', clip=body).blob([(12, 30), (26, 34), (28, 50), (14, 50)])
    _legs(a, legrole, [27, 48], 42, 59, 4.5)
    head = a.part('A').blob([(6, 20), (12, 12), (24, 12), (28, 22), (22, 30), (10, 30)])
    a.part('A').poly([(10, 20), (0, 25), (2, 28), (12, 28)])  # snout
    a.part('C').blob([(2, 25), (12, 24), (16, 30), (6, 30)])
    ear = 7 if fox else 6
    a.part('A').poly([(12, 14), (13, 14 - ear), (18, 13)])
    a.part('A').poly([(19, 13), (23, 13 - ear), (25, 16)])
    a.part('B', clip=None).poly([(13.5, 12), (14, 14 - ear + 3), (16.5, 12.5)])
    a.part('K').circle(1.5, 25.5, 1.6)
    a.eye(14, 19, 1)


def procyonid(a, sp, r):
    """Raccoon. A grey coat, B dark (mask, legs, rings), C white face marks."""
    _legs(a, 'B', [24, 42], 42, 57, 4)
    tail = a.part('A').blob([(46, 34), (56, 30), (62, 36), (60, 46), (52, 44)])
    for x in (50, 55, 59):
        a.part('B', clip=tail, line=False).rect(x, 26, x + 2.2, 50)
    body = a.part('A').blob([(14, 34), (24, 24), (42, 24), (52, 32), (48, 46), (28, 48), (16, 46)])
    a.part('C', clip=body, line=False).ell(16, 40, 40, 52)
    _legs(a, 'B', [20, 46], 44, 59, 4.5)
    head = a.part('A').blob([(4, 26), (8, 14), (22, 12), (28, 22), (22, 32), (8, 32)])
    a.part('C', clip=head, line=False).blob([(2, 22), (14, 16), (26, 18), (24, 30), (6, 32)])
    a.part('B', clip=head).blob([(4, 20), (14, 18), (24, 20), (20, 25), (12, 24), (4, 25)])
    a.part('A').poly([(8, 16), (9, 9), (14, 14)])
    a.part('A').poly([(17, 13), (21, 7), (23, 15)])
    a.part('K').circle(2.5, 27, 1.5)
    a.eye(12, 21, 1, 'white')


def bear(a, sp, r):
    """Bear. A coat, B muzzle/darker legs, D claws."""
    polar = sp.get('polar', False)
    _legs(a, 'B', [20, 40], 44, 58, 7)
    body = a.part('A').blob([(10, 34), (20, 22), (36, 18), (52, 24), (58, 38), (52, 50), (24, 52), (12, 46)])
    if sp.get('hump'):
        a.part('A').ell(28, 15, 44, 28)
    _legs(a, 'A', [26, 48], 44, 60, 8, paw='B')
    head = a.part('A').blob([(2, 26), (6, 16), (18, 14), (24, 22), (20, 32), (6, 34)])
    a.part('B').blob([(0, 27), (8, 24), (10, 32), (2, 33)])
    a.part('A').circle(9, 15, 3.2)
    a.part('A').circle(19, 15, 3.2)
    a.part('K').circle(1.5, 27.5, 1.6)
    a.eye(10, 22, 1)


def mustelid(a, sp, r):
    """Skunk (stripes=True, A black, C white) or wolverine (A dark brown, B tan side band)."""
    _legs(a, 'A', [22, 42], 42, 57, 4)
    if sp.get('stripes'):
        tail = a.part('A').blob([(44, 34), (54, 20), (62, 22), (62, 36), (54, 44)])
    else:
        tail = a.part('A').blob([(46, 36), (56, 34), (60, 42), (52, 46)])
    body = a.part('A').blob([(12, 36), (22, 28), (44, 28), (52, 38), (46, 48), (20, 48)])
    if sp.get('stripes'):
        a.part('C', clip=body, line=False).curve((14, 32), (32, 24), (50, 34), 4)
        a.part('C', clip=tail, line=False).curve((48, 34), (56, 26), (62, 26), 4)
    else:
        a.part('B', clip=body, line=False).curve((14, 38), (32, 32), (52, 38), 5)
    _legs(a, 'A', [18, 46], 44, 59, 4.5)
    head = a.part('A').blob([(2, 32), (6, 24), (18, 24), (22, 32), (16, 40), (6, 40)])
    if sp.get('stripes'):
        a.part('C', clip=head, line=False).rect(9, 22, 11.5, 34)
    a.part('A').circle(12, 24, 2.5)
    a.part('K').circle(1.5, 34, 1.4)
    a.eye(10, 30, 1)


def bovid(a, sp, r):
    """Bison / muskox / bighorn / mountain goat. A coat, B wool/hump/skirt, C rump/muzzle, D horns."""
    kind = sp.get('kind', 'bison')
    leg = 'B' if kind == 'goat' else 'A'
    _legs(a, leg, [22, 46], 40, 57, 4.5)
    body = a.part('A').blob([(14, 30), (26, 22), (50, 26), (58, 34), (54, 46), (24, 46), (14, 42)])
    if kind in ('bison', 'muskox'):
        a.part('B').blob([(10, 18), (26, 12), (34, 20), (34, 40), (18, 46), (8, 36)])
    if kind == 'muskox':
        a.part('B').blob([(12, 30), (56, 30), (60, 50), (12, 52)])
    if kind == 'sheep':
        a.part('C', clip=body, line=False).ell(48, 28, 64, 46)
    _legs(a, leg, [27, 51], 44, 59, 5, paw='K')
    head = a.part('A' if kind != 'bison' else 'B').blob([(2, 30), (4, 20), (14, 16), (20, 24), (14, 36), (4, 38)])
    if kind in ('bison', 'goat'):
        a.part('B').poly([(4, 34), (12, 34), (8, 44)])  # beard
    if kind == 'sheep':
        a.part('C').blob([(0, 30), (6, 28), (8, 36), (2, 37)])
        a.part('D').curve((14, 18), (26, 10), (22, 28), 5, 3)
    elif kind == 'goat':
        a.part('D').curve((10, 18), (11, 8), (16, 6), 2.5, 1.5)
        a.part('D').curve((14, 18), (16, 8), (20, 6), 2.5, 1.5)
    elif kind == 'muskox':
        a.part('D').blob([(6, 18), (18, 15), (22, 24), (18, 28), (16, 20), (8, 21)])
    else:
        a.part('D').curve((12, 18), (16, 12), (14, 8), 3, 1.5)
    a.eye(8, 25, 1)


def cat(a, sp, r):
    """Big cat. A coat, C belly, D rosettes, long tail."""
    _legs(a, 'A', [22, 44], 40, 57, 4.5)
    tail = a.part('A').curve((50, 34), (62, 40), (60, 22), 4 if sp.get('thicktail') else 3, 4.5 if sp.get('thicktail') else 2.5)
    body = a.part('A').blob([(14, 32), (26, 24), (48, 26), (54, 34), (48, 44), (24, 46), (14, 42)])
    a.part('C', clip=body, line=False).ell(14, 40, 50, 54)
    spots = a.part('D', clip=body, line=False)
    for (x, y) in [(22, 30), (30, 28), (38, 30), (46, 32), (26, 36), (34, 35), (42, 38)]:
        spots.ell(x - 2, y - 1.6, x + 2, y + 1.6)
    a.part('D', clip=tail, line=False).rect(56, 20, 64, 22).rect(57, 28, 64, 30)
    _legs(a, 'A', [27, 49], 42, 59, 5, paw='C')
    head = a.part('A').blob([(4, 22), (8, 14), (20, 14), (24, 22), (18, 30), (6, 30)])
    a.part('C').blob([(2, 24), (10, 23), (12, 30), (4, 30)])
    a.part('A').poly([(8, 16), (9, 10), (13, 15)])
    a.part('A').poly([(16, 14), (19, 9), (21, 16)])
    a.part('D', clip=head, line=False).circle(15, 25, 1).circle(18, 20, 1)
    a.part('K').circle(2.5, 24.5, 1.3)
    a.eye(10, 19, 1)


def rodent(a, sp, r):
    """Groundhog / ground squirrel / lemming / beaver. A coat, B tail (beaver) or dark, C belly, E teeth."""
    kind = sp.get('kind', 'groundhog')
    if kind == 'beaver':
        a.part('B').blob([(40, 50), (52, 42), (63, 44), (62, 56), (46, 58)])
    elif kind == 'squirrel':
        a.part('A').curve((40, 44), (54, 40), (52, 26), 3, 4)
    upright = kind in ('groundhog', 'squirrel')
    if upright:
        body = a.part('A').blob([(16, 24), (30, 18), (40, 30), (40, 52), (20, 54), (14, 40)])
        a.part('C', clip=body, line=False).ell(14, 30, 30, 56)
        a.part('A').line([(18, 34), (14, 40)], 4)
        head = a.part('A').blob([(12, 12), (24, 8), (32, 16), (28, 26), (16, 26)])
        a.part('C').blob([(10, 18), (18, 18), (20, 26), (12, 26)])
        a.part('A').circle(26, 10, 2.5)
        a.part('K').circle(10.5, 19.5, 1.3)
        a.part('W').rect(12, 24, 14, 27)
        a.eye(18, 15, 1)
    else:
        body = a.part('A').blob([(10, 40), (20, 28), (40, 28), (50, 40), (44, 52), (16, 52)])
        a.part('C', clip=body, line=False).ell(10, 44, 44, 58)
        _legs(a, 'A', [18, 40], 48, 56, 4)
        head = a.part('A').blob([(4, 36), (10, 28), (20, 30), (22, 40), (12, 46), (4, 44)])
        a.part('K').circle(4, 38, 1.2)
        if kind == 'beaver':
            a.part('E').rect(5, 42, 8, 46)
        a.part('A').circle(16, 30, 2.5)
        a.eye(11, 35, 1)


def hare(a, sp, r):
    """Hare. A coat, D ear tips, long hind feet."""
    body = a.part('A').blob([(14, 38), (24, 28), (44, 30), (52, 42), (46, 54), (20, 54)])
    a.part('A').ell(38, 46, 58, 56)
    a.part('A').circle(54, 38, 4)
    a.part('A').line([(18, 46), (16, 56)], 4)
    head = a.part('A').blob([(4, 28), (10, 20), (22, 22), (24, 32), (14, 38), (6, 36)])
    a.part('A').curve((14, 22), (16, 8), (22, 2), 4, 3)
    a.part('A').curve((18, 22), (24, 10), (30, 6), 4, 3)
    a.part('D').circle(22, 3, 2).circle(30, 6.5, 2)
    a.part('K').circle(4.5, 30, 1.2)
    a.eye(12, 27, 1, 'big')


def opossum(a, sp, r):
    """Opossum. A grey coat, C white face, E pink nose/ears/tail."""
    a.part('E').curve((48, 44), (62, 46), (60, 30), 2.5, 1.5)
    _legs(a, 'K', [22, 42], 42, 56, 4)
    body = a.part('A').blob([(14, 36), (24, 26), (44, 28), (52, 38), (46, 48), (20, 48)])
    _legs(a, 'K', [18, 46], 44, 58, 4.5)
    head = a.part('C').blob([(0, 36), (8, 26), (20, 26), (22, 36), (14, 42), (4, 42)])
    a.part('K').circle(16, 25, 3)
    a.part('E').circle(1, 36, 1.4)
    a.eye(10, 31, 1)


def armadillo(a, sp, r):
    """Armadillo. A shell, B skin/head, C bands highlight. fairy=True: pink shell on white fur."""
    fairy = sp.get('fairy', False)
    if fairy:
        a.part('C').blob([(10, 40), (20, 30), (46, 30), (54, 44), (46, 54), (16, 54)])
    a.part('B').curve((48, 46), (58, 50), (62, 44), 3.5, 2)
    _legs(a, 'B', [22, 42], 46, 56, 4)
    shell = a.part('A').blob([(14, 38), (22, 24), (44, 24), (54, 38), (50, 48), (16, 48)])
    for x in range(24, 48, 5):
        a.part('A', clip=shell).rect(x, 20, x + 0.8, 52)
    head = a.part('B').blob([(2, 42), (6, 34), (16, 34), (18, 42), (8, 46)])
    a.part('B').poly([(8, 34), (10, 28), (13, 34)])
    a.eye(9, 39, 1)


def sloth(a, sp, r):
    """Three-toed sloth hanging from a branch. A fur, B face mask, C face, D branch."""
    a.part('D').rect(0, 8, 64, 13)
    a.part('A').line([(18, 12), (22, 26)], 5).line([(44, 12), (40, 26)], 5)
    body = a.part('A').blob([(14, 24), (32, 18), (50, 24), (52, 40), (32, 48), (14, 40)])
    head = a.part('A').circle(26, 40, 10)
    a.part('C').ell(18, 34, 34, 48)
    a.part('B').blob([(17, 38), (24, 36), (30, 38), (34, 42), (28, 41), (20, 41)])
    a.part('K').circle(26, 44, 1.4)
    a.eye(21, 39, 1)
    a.eye(30, 39, 1)


def primate(a, sp, r):
    """Howler monkey. A fur, B mantle, curled tail."""
    a.part('A').curve((40, 44), (62, 40), (56, 20), 3, 2)
    body = a.part('A').blob([(18, 24), (36, 20), (44, 34), (40, 50), (20, 50), (14, 36)])
    a.part('B', clip=body, line=False).ell(30, 22, 50, 44)
    a.part('A').line([(20, 30), (10, 44), (12, 56)], 4).line([(36, 46), (40, 58)], 5).line([(22, 48), (20, 58)], 5)
    head = a.part('A').circle(20, 16, 9)
    a.part('K').ell(12, 14, 24, 26)
    a.eye(15, 16, 1, 'white')
    a.eye(21, 16, 1, 'white')


def bat(a, sp, r):
    """Bat with wings spread. A fur, B wing membrane, E nose/ears."""
    w = a.part('B')
    w.poly([(32, 26), (4, 14), (2, 34), (10, 30), (14, 40), (22, 34), (32, 40)])
    w.poly([(32, 26), (60, 14), (62, 34), (54, 30), (50, 40), (42, 34), (32, 40)])
    body = a.part('A').ell(24, 24, 40, 46)
    head = a.part('A').circle(32, 20, 7)
    a.part('E').poly([(26, 16), (25, 6), (30, 13)]).poly([(34, 13), (39, 6), (38, 16)])
    a.part('E').circle(32, 23, 2)
    a.eye(29, 18, 1)
    a.eye(35, 18, 1)


def elephant(a, sp, r):
    """Elephant. A grey skin, B darker ear, W tusks."""
    _legs(a, 'A', [24, 46], 40, 58, 7)
    body = a.part('A').blob([(14, 26), (30, 16), (52, 20), (60, 34), (56, 46), (24, 46), (14, 40)])
    _legs(a, 'A', [30, 52], 42, 60, 8, paw='C')
    head = a.part('A').blob([(4, 20), (10, 12), (22, 12), (24, 26), (16, 34), (8, 32)])
    a.part('A').curve((8, 28), (2, 40), (6, 52), 6, 3)
    a.part('B').blob([(14, 10), (28, 8), (32, 22), (26, 34), (16, 30)])
    a.part('W').curve((10, 32), (6, 38), (2, 36), 2.5, 1.5)
    a.eye(10, 21, 1)


def platypus(a, sp, r):
    """Platypus. A brown fur, E bill, B flat tail."""
    a.part('B').blob([(44, 38), (62, 34), (63, 46), (46, 48)])
    body = a.part('A').blob([(12, 38), (22, 30), (44, 32), (50, 42), (40, 50), (16, 50)])
    a.part('A').line([(18, 46), (14, 54)], 4).line([(38, 48), (42, 56)], 4)
    head = a.part('A').ell(8, 30, 24, 46)
    a.part('E').blob([(0, 38), (10, 34), (12, 42), (2, 44)])
    a.eye(14, 36, 1)


def pinniped(a, sp, r):
    """Walrus (tusks), elephant seal (nose) or manatee. A skin, B flippers, C muzzle, W tusks."""
    kind = sp.get('kind', 'walrus')
    if kind == 'manatee':
        a.part('A').blob([(46, 34), (62, 28), (62, 50), (48, 46)])
        body = a.part('A').blob([(4, 34), (14, 24), (40, 24), (50, 36), (40, 48), (12, 48)])
        a.part('B').line([(16, 42), (12, 52)], 4)
        a.part('C').blob([(0, 34), (8, 30), (10, 40), (2, 42)])
        a.eye(10, 32, 1)
        return
    a.part('B').blob([(48, 48), (62, 44), (62, 56), (50, 56)])
    body = a.part('A').blob([(12, 30), (22, 18), (40, 22), (52, 40), (50, 54), (20, 56), (10, 44)])
    a.part('B').blob([(16, 44), (8, 56), (24, 56)])
    head = a.part('A').blob([(4, 22), (10, 12), (22, 14), (24, 26), (16, 32), (6, 32)])
    if kind == 'walrus':
        a.part('C').blob([(2, 24), (14, 22), (16, 32), (4, 32)])
        a.part('W').line([(6, 30), (5, 44)], 2.5).line([(12, 30), (12, 44)], 2.5)
    else:
        a.part('A').blob([(0, 20), (8, 18), (10, 28), (2, 30)])
    a.eye(12, 19, 1)


def whale(a, sp, r):
    """Whales. A back, C belly/patches, D mottling. kind: orca, humpback, blue, fin, gray, sperm, beaked, narwhal."""
    kind = sp.get('kind', 'blue')
    a.part('A').blob([(48, 31), (58, 30), (64, 25), (62, 33), (64, 40), (58, 35), (48, 35)])  # flukes, edge-on
    if kind == 'sperm':
        body = a.part('A').blob([(6, 22), (32, 20), (52, 29), (56, 33), (40, 42), (8, 44)])
    else:
        body = a.part('A').blob([(6, 33), (16, 25), (36, 23), (54, 31), (56, 33), (36, 44), (14, 44)])
    belly = a.part('C', clip=body, line=False)
    if kind == 'orca':
        belly.blob([(6, 37), (22, 38), (32, 46), (8, 46)])
        a.part('C', clip=body, line=False).ell(17, 28, 25, 32)
        a.part('C', clip=body, line=False).ell(36, 34, 48, 41)
        a.part('A').poly([(30, 25), (34, 6), (40, 25)])
    elif kind in ('fin', 'blue', 'beaked', 'narwhal', 'gray'):
        belly.ell(2, 38, 58, 52)
        if kind in ('fin', 'blue'):
            a.part('A').poly([(40, 27), (45, 22), (47, 29)])
    if kind in ('blue', 'gray', 'narwhal', 'beaked'):
        m = a.part('D', clip=body, line=False)
        for _ in range(9):
            x, y = 12 + 38 * next(r), 25 + 11 * next(r)
            m.ell(x - 1.5, y - 1, x + 1.5, y + 1)
    if kind == 'humpback':
        a.part('C').curve((22, 40), (16, 52), (8, 58), 4, 2.5)
        bumps = a.part('C', clip=body, line=False)
        for x in (10, 14, 18):
            bumps.circle(x, 29, 1)
    else:
        a.part('A').curve((22, 40), (20, 46), (16, 49), 4, 2)
    if kind == 'narwhal':
        a.part('W').line([(8, 32), (0, 27)], 1.6)
    a.eye(14, 33, 1)
