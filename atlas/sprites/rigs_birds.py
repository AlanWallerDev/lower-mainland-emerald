"""Bird rigs: bird (perch / upright / stand / hover), seabird (flying), owl (front-facing)."""


def _bill(a, kind, hx, hy, role='E'):
    p = a.part(role)
    if kind == 'short':
        p.poly([(hx + 1, hy - 1.6), (hx - 4, hy + .5), (hx + 1, hy + 2)])
    elif kind == 'cone':
        p.poly([(hx + 1, hy - 2.5), (hx - 5, hy + .5), (hx + 1, hy + 3)])
    elif kind == 'hook':
        p.blob([(hx + 1, hy - 3), (hx - 5, hy - 2), (hx - 6, hy + 3), (hx - 3, hy + 1), (hx + 1, hy + 2)], 1)
    elif kind == 'dagger':
        p.poly([(hx + 1, hy - 1.5), (hx - 9, hy + .5), (hx + 1, hy + 2)])
    elif kind == 'long':
        p.poly([(hx + 1, hy - 1), (hx - 13, hy + 2), (hx + 1, hy + 2)])
    elif kind == 'needle':
        p.line([(hx, hy), (hx - 12, hy + 1)], 1.2)
    elif kind == 'spoon':
        p.line([(hx, hy), (hx - 11, hy + 3)], 2).ell(hx - 16, hy + 1, hx - 9, hy + 6)
    elif kind == 'toucan':
        p.blob([(hx + 1, hy - 4), (hx - 10, hy - 4), (hx - 18, hy), (hx - 10, hy + 3), (hx + 1, hy + 4)], 2)
        a.part('D', clip=p, line=False).ell(hx - 20, hy - 6, hx - 11, hy + 6)
    elif kind == 'puffin':
        p.poly([(hx + 1, hy - 5), (hx - 7, hy + 1), (hx + 1, hy + 6)])
        a.part('D', clip=p, line=False).rect(hx - 1, hy - 6, hx + 2, hy + 7)
    elif kind == 'goose':
        p.poly([(hx + 1, hy - 2), (hx - 7, hy), (hx - 7, hy + 2), (hx + 1, hy + 3)])
    return p


def _tail(a, kind, role, x, y):
    p = a.part(role)
    if kind == 'long':
        p.poly([(x - 2, y - 3), (x + 18, y + 8), (x + 16, y + 12), (x - 2, y + 4)])
    elif kind == 'fan':
        for ang in (-30, -15, 0, 15, 30, 45):
            import math
            t = math.radians(ang - 20)
            p.line([(x, y), (x + 16 * math.cos(t), y - 16 * math.sin(t) - 4)], 2.4)
    elif kind == 'forked':
        p.poly([(x - 2, y - 2), (x + 14, y - 4), (x + 8, y + 1), (x + 14, y + 6), (x - 2, y + 4)])
    elif kind == 'streamers':
        p.poly([(x - 2, y - 2), (x + 8, y), (x - 2, y + 4)])
        p.line([(x + 4, y + 1), (x + 20, y + 4)], 1.2)
    else:
        p.poly([(x - 2, y - 3), (x + 8, y + 2), (x + 6, y + 6), (x - 2, y + 4)])
    return p


def bird(a, sp, r):
    """Generic bird. A body/back, B wing, C belly/face, D pattern/crest, E bill, legs K unless legs='E'.
    pose: perch | upright | stand | hover. bill: see _bill. tail: short | long | fan | forked | streamers.
    head: role of the head (default A). neck: role of a long neck (stand pose). crest, tufts, bald, ruff."""
    pose = sp.get('pose', 'perch')
    head_role = sp.get('head', 'A')
    leg_role = sp.get('legs', 'K')
    bill = sp.get('bill', 'short')
    if pose == 'upright':
        a.part(leg_role).ell(18, 54, 28, 58).ell(28, 54, 38, 58)
        body = a.part('A').blob([(18, 24), (32, 18), (42, 30), (40, 52), (28, 58), (16, 50), (14, 36)])
        a.part('C', clip=body, line=False).blob([(10, 30), (24, 26), (28, 60), (10, 60)])
        a.part('B').blob([(30, 26), (40, 30), (42, 48), (34, 50)])
        head = a.part(head_role).blob([(14, 8), (26, 6), (32, 14), (30, 24), (18, 26), (12, 18)])
        if sp.get('face'):
            a.part('C', clip=head, line=False).blob([(10, 10), (22, 8), (24, 20), (12, 24)])
        if sp.get('tufts'):
            a.part('D').curve((26, 10), (34, 10), (40, 18), 2.5, 1.5)
        _bill(a, bill, 13, 15)
        a.eye(19, 13, 1)
        return
    if pose == 'stand':
        _legs = a.part(leg_role)
        _legs.line([(30, 40), (30, 58)], 1.6).line([(36, 40), (37, 58)], 1.6)
        _tail(a, sp.get('tail', 'short'), 'B', 50, 30)
        body = a.part('A').blob([(22, 30), (34, 22), (50, 24), (56, 32), (46, 42), (28, 42)])
        a.part('C', clip=body, line=False).ell(16, 34, 44, 50)
        a.part('B', clip=body).blob([(32, 24), (54, 26), (52, 36), (36, 34)])
        a.part(sp.get('neck', head_role)).curve((28, 30), (16, 22), (16, 12), 5, 4)
        head = a.part(head_role).circle(15, 11, 5.5)
        if sp.get('chinstrap'):
            a.part('C', clip=head, line=False).blob([(14, 10), (20, 9), (21, 17), (15, 17)])
        _bill(a, bill, 11, 11)
        a.eye(14, 9, 1)
        return
    if pose == 'hover':
        w = a.part('B')
        w.blob([(30, 26), (40, 6), (48, 10), (38, 30)]).blob([(26, 26), (24, 8), (30, 8), (32, 26)])
        _tail(a, 'short', 'A', 42, 40)
        body = a.part('A').blob([(18, 28), (30, 22), (42, 30), (44, 40), (32, 44), (20, 40)])
        a.part('D', clip=body, line=False).ell(14, 30, 28, 42)
        head = a.part(head_role).circle(18, 24, 6)
        _bill(a, bill, 13, 24)
        a.eye(17, 22, 1)
        return
    # perch
    leg = a.part(leg_role)
    leg.line([(26, 44), (25, 55)], 1.8).line([(33, 44), (34, 55)], 1.8)
    if sp.get('branch', True):
        a.part('D' if sp.get('branch_role') is None else sp['branch_role']).rect(10, 55, 56, 58)
    _tail(a, sp.get('tail', 'short'), sp.get('tail_role', 'B'), 42, 40)
    body = a.part('A').blob([(16, 30), (28, 22), (42, 26), (48, 38), (38, 48), (22, 46)])
    a.part('C', clip=body, line=False).blob([(10, 32), (24, 30), (30, 52), (12, 52)])
    if sp.get('spots'):
        sp_part = a.part('W' if sp.get('spots') == 'W' else 'D', clip=body, line=False)
        for _ in range(10):
            x, y = 18 + 26 * next(r), 26 + 18 * next(r)
            sp_part.circle(x, y, .8)
    a.part('B', clip=body).blob([(28, 26), (48, 32), (46, 44), (32, 42)])
    if sp.get('ruff'):
        a.part('C').blob([(12, 26), (24, 24), (28, 36), (14, 38)])
        a.part('E').ell(15, 30, 21, 35).ell(21, 31, 27, 36)
    if sp.get('crest'):
        a.part(sp.get('crest_role', head_role)).poly([(18, 14), (30, 6), (26, 16)])
    hr = 7 if not sp.get('bald') else 5
    head = a.part(head_role).circle(17, 20, hr)
    if sp.get('face'):
        a.part('C', clip=head, line=False).blob([(8, 18), (16, 16), (20, 26), (10, 28)])
    if sp.get('hood'):
        a.part('B', clip=head, line=False).blob([(8, 12), (26, 12), (26, 20), (18, 24), (14, 20), (8, 20)])
    if sp.get('throat'):
        a.part('D', clip=body, line=False).ell(12, 24, 22, 34)
    _bill(a, bill, 11, 20)
    a.eye(16, 18, 1 if not sp.get('bigeye') else 2, 'red' if sp.get('eyering') else 'dot')


def seabird(a, sp, r):
    """Seabird in flight. A back/upperwing, B wingtips, C underparts, D head mark, E bill. tail kind."""
    import math
    span = sp.get('span', 1.0)
    w = a.part('A')
    w.blob([(28, 30), (24 - 22 * span, 16), (22 - 20 * span, 20), (30, 36)])
    w.blob([(34, 30), (36 + 24 * span, 14), (38 + 22 * span, 19), (36, 36)])
    if sp.get('tips'):
        a.part('B', clip=w, line=False).ell(-8, 8, 10, 26).ell(50, 6, 70, 24)
    _tail(a, sp.get('tail', 'short'), sp.get('tail_role', 'A'), 44, 34)
    body = a.part('C').blob([(14, 32), (28, 28), (44, 32), (46, 36), (30, 40), (16, 38)])
    a.part('A', clip=body, line=False).ell(16, 24, 50, 33)
    head = a.part(sp.get('head', 'C')).circle(14, 31, 5.5)
    if sp.get('cap'):
        a.part('D', clip=head, line=False).ell(8, 24, 20, 31)
    if sp.get('stripe'):
        a.part('D', clip=head, line=False).rect(8, 29, 18, 31)
    _bill(a, sp.get('bill', 'dagger'), 9, 32)
    a.eye(12, 30, 1)


def owl(a, sp, r):
    """Front-facing owl (or potoo). A plumage, C facial disc/belly, D bars/spots, E eyes, tufts."""
    potoo = sp.get('potoo', False)
    a.part('E' if not potoo else 'K').ell(20, 54, 28, 58).ell(34, 54, 42, 58)
    if potoo:
        a.part('D').rect(26, 56, 38, 64)
    body = a.part('A').blob([(16, 30), (32, 22), (48, 30), (48, 50), (32, 58), (16, 50)])
    a.part('C', clip=body, line=False).ell(22, 34, 42, 60)
    bars = a.part('D', clip=body, line=False)
    if sp.get('pattern') == 'spots':
        for _ in range(16):
            x, y = 18 + 28 * next(r), 28 + 28 * next(r)
            bars.circle(x, y, .9)
    else:
        for y in range(32, 58, 4):
            for x in range(18, 48, 6):
                bars.rect(x + (y % 8) / 2, y, x + 2.5 + (y % 8) / 2, y + 1)
    a.part('A').blob([(14, 34), (20, 32), (22, 50), (16, 52)]).blob([(50, 34), (44, 32), (42, 50), (48, 52)])
    head = a.part('A').blob([(12, 18), (20, 8), (44, 8), (52, 18), (48, 30), (16, 30)])
    if sp.get('tufts'):
        a.part('A').poly([(16, 12), (14, 2), (22, 9)]).poly([(48, 12), (50, 2), (42, 9)])
    if not potoo:
        a.part('C', clip=head).ell(15, 11, 32, 28).ell(32, 11, 49, 28)
    eye_r = 4.5 if potoo else 4
    a.part('E').circle(24, 19, eye_r).circle(40, 19, eye_r)
    a.part('K').circle(24, 19, 2).circle(40, 19, 2)
    a.part('D' if potoo else 'K').poly([(30, 22), (34, 22), (32, 27)])
