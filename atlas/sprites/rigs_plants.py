"""Plant, fungus, lichen, slime-mould and macroscopic alga rigs."""
import math


def _ground(a, role='D', y=56):
    a.part(role).rect(0, y, 64, 64)


def conifer(a, sp, r):
    """Redwood / sequoia. A foliage, B trunk (red-brown), D ground."""
    _ground(a)
    a.part('B').poly([(28, 60), (30, 10), (34, 10), (38, 60)])
    f = a.part('A')
    for k in range(5):
        y = 8 + k * 9
        w = 6 + k * 3.5
        f.blob([(32, y - 4), (32 + w, y + 6), (32, y + 8), (32 - w, y + 6)], 2)
    a.part('B').rect(29, 50, 37, 58)


def tree(a, sp, r):
    """Broadleaf tree / shrub. A foliage, B trunk, C highlights, D fruit/flowers, E ground.
    kind: generic, baobab, sausage, cacao, coffee, ginkgo, mangrove, quiver, joshua, acacia."""
    kind = sp.get('kind', 'generic')
    a.part('E').rect(0, 56, 64, 64)
    if kind == 'mangrove':
        a.part('E').rect(0, 50, 64, 64)
        roots = a.part('B')
        for x in (18, 26, 38, 46):
            roots.curve((32, 36), (x, 40), (x - 2, 56), 1.6, 1.2)
    if kind == 'baobab':
        a.part('B').blob([(20, 58), (22, 26), (42, 26), (44, 58)])
        br = a.part('B')
        for x in (18, 26, 38, 46):
            br.line([(32, 28), (x, 14)], 2)
        a.part('A').ell(8, 6, 26, 18).ell(36, 6, 56, 18)
        return
    if kind in ('quiver', 'joshua'):
        a.part('B').line([(32, 58), (32, 32)], 6)
        br = a.part('B')
        for (x, y) in [(18, 18), (26, 12), (40, 12), (48, 20)]:
            br.line([(32, 34), (x, y)], 3.5)
        tufts = a.part('A')
        for (x, y) in [(18, 18), (26, 12), (40, 12), (48, 20)]:
            if kind == 'joshua':
                for k in range(8):
                    t = k * math.pi / 4
                    tufts.line([(x, y), (x + 6 * math.cos(t), y + 6 * math.sin(t))], 1.4)
            else:
                tufts.ell(x - 5, y - 5, x + 5, y + 3)
        return
    if kind == 'acacia':
        a.part('B').line([(32, 58), (32, 30)], 4).line([(32, 36), (20, 24)], 2.5).line([(32, 34), (46, 24)], 2.5)
        a.part('A').blob([(4, 24), (20, 14), (44, 14), (60, 24), (32, 28)])
        g = a.part('D')
        for x in (24, 32, 40):
            g.circle(x, 30, 2.5)
        return
    trunk_w = 5 if kind != 'coffee' else 3
    a.part('B').line([(32, 58), (32, 30)], trunk_w)
    crown = a.part('A')
    if kind == 'ginkgo':
        for (x, y) in [(18, 22), (28, 14), (40, 14), (48, 24), (24, 30), (40, 30), (32, 22)]:
            crown.poly([(x, y + 4), (x - 6, y - 4), (x + 6, y - 4)])
    elif kind == 'coffee':
        crown.blob([(12, 40), (16, 18), (32, 10), (48, 18), (52, 40), (32, 46)])
    else:
        crown.blob([(6, 30), (14, 12), (32, 6), (50, 12), (58, 30), (44, 40), (20, 40)])
    a.part('C', clip=crown, line=False).ell(16, 10, 34, 22)
    fr = a.part('D')
    if kind == 'sausage':
        for x in (18, 28, 38, 46):
            fr.line([(x, 34), (x, 40)], .7)
            fr.ell(x - 2, 40, x + 2, 52)
    elif kind == 'cacao':
        for (x, y) in [(29, 42), (35, 48), (30, 50)]:
            fr.ell(x - 3, y - 4, x + 3, y + 4)
    elif kind == 'coffee':
        for _ in range(10):
            x, y = 16 + 32 * next(r), 16 + 26 * next(r)
            fr.circle(x, y, 1.6)
    elif kind == 'avocado':
        for (x, y) in [(18, 36), (44, 34), (30, 38)]:
            fr.line([(x, y - 4), (x, y)], .7)
            fr.blob([(x, y), (x + 3, y + 5), (x, y + 9), (x - 3, y + 5)], 2)


def cactus(a, sp, r):
    """Saguaro (arms) or bunny-ears (pads). A body, B ribs/glochid dots, C flowers, D ground."""
    _ground(a)
    if sp.get('kind') == 'pads':
        p = a.part('A')
        for (x, y, w, h) in [(32, 44, 9, 12), (20, 30, 7, 9), (44, 30, 7, 9), (26, 18, 5, 7), (40, 18, 5, 7)]:
            p.ell(x - w, y - h, x + w, y + h)
        d = a.part('B', clip=p, line=False)
        for _ in range(30):
            x, y = 12 + 40 * next(r), 10 + 44 * next(r)
            d.circle(x, y, .6)
        return
    body = a.part('A')
    body.line([(32, 58), (32, 10)], 10)
    body.line([(26, 38), (16, 36), (16, 20)], 7).line([(38, 32), (48, 30), (48, 16)], 7)
    rib = a.part('B', clip=body, line=False)
    for x in (30, 34, 15, 47):
        rib.rect(x, 0, x + .8, 64)
    a.part('C').circle(32, 8, 2.5).circle(16, 18, 2).circle(48, 14, 2)


def flower(a, sp, r):
    """Flowering plant. A bloom, B bloom centre / second colour, C leaves, D stem/ground, E third colour.
    kind: sunflower, lotus, slipper, paradise, protea, periwinkle, milkweed, chili, starflower, spike, puya, papyrus."""
    kind = sp.get('kind', 'sunflower')
    if kind == 'lotus':
        a.part('E').rect(0, 50, 64, 64)
        a.part('C').ell(4, 46, 30, 54).ell(36, 48, 60, 56)
        a.part('D').line([(32, 50), (32, 30)], 2)
        p = a.part('A')
        for k in range(-2, 3):
            p.blob([(32, 32), (32 + k * 7 - 4, 18), (32 + k * 7, 12), (32 + k * 7 + 4, 18)], 2)
        a.part('B').ell(27, 26, 37, 32)
        return
    if kind == 'puya':
        _ground(a)
        a.part('C').blob([(10, 58), (32, 40), (54, 58)])
        a.part('A').blob([(26, 44), (28, 4), (36, 4), (38, 44)])
        d = a.part('B', line=False)
        for y in range(8, 42, 4):
            d.rect(27, y, 37, y + 1.2)
        return
    if kind == 'spike':
        _ground(a)
        a.part('C').blob([(8, 58), (20, 44), (32, 48), (44, 44), (56, 58)])
        a.part('A').ell(26, 6, 38, 50)
        d = a.part('B', line=False)
        for y in range(10, 48, 5):
            d.rect(27, y, 37, y + 1.5)
        return
    if kind == 'papyrus':
        a.part('E').rect(0, 52, 64, 64)
        st = a.part('D')
        for x0, x1 in [(24, 16), (32, 32), (40, 48)]:
            st.line([(x0, 58), (x1, 20)], 1.6)
        heads = a.part('A')
        for x1 in (16, 32, 48):
            for k in range(9):
                t = math.radians(200 + k * 17.5)
                heads.line([(x1, 20), (x1 + 10 * math.cos(t), 20 + 10 * math.sin(t))], .9)
        return
    if kind == 'starflower':
        _ground(a)
        a.part('C').rect(18, 40, 46, 58)
        p = a.part('A')
        for k in range(5):
            t = math.radians(-90 + k * 72)
            p.poly([(32, 30), (32 + 22 * math.cos(t - .25), 30 + 22 * math.sin(t - .25)), (32 + 26 * math.cos(t), 30 + 26 * math.sin(t)), (32 + 22 * math.cos(t + .25), 30 + 22 * math.sin(t + .25))])
        stripes = a.part('B', clip=p, line=False)
        for y in range(4, 60, 4):
            stripes.rect(0, y, 64, y + 1)
        a.part('E').circle(32, 30, 4)
        return
    _ground(a)
    stem = a.part('D').line([(32, 58), (32, 26)], 2)
    leaves = a.part('C')
    leaves.blob([(32, 46), (14, 38), (20, 48)]).blob([(32, 40), (50, 32), (44, 44)])
    if kind == 'sunflower':
        p = a.part('A')
        for k in range(12):
            t = k * math.pi / 6
            p.blob([(32, 18), (32 + 13 * math.cos(t - .2), 18 + 13 * math.sin(t - .2)), (32 + 17 * math.cos(t), 18 + 17 * math.sin(t)), (32 + 13 * math.cos(t + .2), 18 + 13 * math.sin(t + .2))], 1)
        a.part('B').circle(32, 18, 7.5)
    elif kind == 'slipper':
        a.part('E').poly([(32, 14), (20, 6), (24, 16)]).poly([(32, 14), (44, 6), (40, 16)])
        a.part('A').blob([(24, 16), (32, 12), (40, 16), (40, 30), (32, 34), (24, 30)])
        a.part('B').line([(32, 16), (32, 30)], .8)
    elif kind == 'paradise':
        a.part('A').blob([(12, 26), (40, 18), (52, 24), (40, 26)])
        p = a.part('B')
        for k in range(4):
            p.poly([(30, 20), (24 + k * 6, 4), (28 + k * 6, 6)])
        a.part('E').poly([(34, 20), (40, 8), (38, 20)])
    elif kind == 'protea':
        p = a.part('A')
        for k in range(9):
            t = math.radians(200 + k * 17.5)
            p.blob([(32, 26), (32 + 14 * math.cos(t - .15), 26 + 14 * math.sin(t - .15)), (32 + 18 * math.cos(t), 26 + 18 * math.sin(t)), (32 + 14 * math.cos(t + .15), 26 + 14 * math.sin(t + .15))], 1)
        a.part('B').ell(25, 14, 39, 28)
    elif kind == 'periwinkle':
        p = a.part('A')
        for k in range(5):
            t = math.radians(-90 + k * 72)
            p.circle(32 + 8 * math.cos(t), 18 + 8 * math.sin(t), 5.5)
        a.part('B').circle(32, 18, 2.5)
    elif kind == 'milkweed':
        for (x, y) in [(24, 16), (40, 18)]:
            c = a.part('A')
            for k in range(7):
                t = k * math.pi / 3.5
                c.circle(x + 5 * math.cos(t), y + 5 * math.sin(t), 2.2)
        a.part('B').blob([(42, 34), (52, 28), (54, 36), (46, 42)], 2)
    elif kind == 'chili':
        a.part('C').blob([(14, 30), (32, 16), (50, 30), (32, 36)])
        p = a.part('A')
        for (x, y) in [(22, 34), (40, 34), (32, 38)]:
            p.taper([(x, y), (x + 1, y + 6), (x - 1, y + 12)], 3, 1)


def carnivore(a, sp, r):
    """Carnivorous plant. A trap, B inside/teeth, C leaves, D ground. kind: flytrap, pitcher (cobra lily), sundew."""
    kind = sp.get('kind', 'flytrap')
    _ground(a)
    if kind == 'pitcher':
        a.part('A').taper([(30, 58), (30, 36), (28, 22)], 5, 9)
        hood = a.part('A').blob([(16, 18), (24, 8), (38, 8), (42, 18), (34, 24), (22, 24)])
        a.part('B').blob([(18, 22), (24, 24), (22, 32), (16, 28)])
        sp_ = a.part('C', clip=hood, line=False)
        for _ in range(10):
            x, y = 18 + 22 * next(r), 8 + 16 * next(r)
            sp_.circle(x, y, 1)
        return
    if kind == 'sundew':
        lv = a.part('C')
        for k in range(6):
            t = math.radians(180 + k * 36)
            lv.line([(32, 54), (32 + 20 * math.cos(t), 54 + 20 * math.sin(t))], 3)
        g = a.part('A')
        for k in range(6):
            t = math.radians(180 + k * 36)
            for j in range(3):
                x = 32 + (12 + j * 4) * math.cos(t)
                y = 54 + (12 + j * 4) * math.sin(t)
                g.line([(x, y), (x + 2 * math.cos(t + 1.5), y + 2 * math.sin(t + 1.5))], .8)
        dew = a.part('B')
        for k in range(6):
            t = math.radians(180 + k * 36)
            dew.circle(32 + 22 * math.cos(t), 54 + 22 * math.sin(t), 1.2)
        return
    a.part('C').blob([(14, 58), (32, 48), (50, 58)])
    for (cx, cy, s) in [(20, 30, 1.0), (44, 24, .9)]:
        a.part('C').line([(32, 54), (cx, cy + 10 * s)], 2)
        lo = a.part('A').blob([(cx - 10 * s, cy), (cx, cy - 2 * s), (cx + 10 * s, cy), (cx, cy + 8 * s)], 2)
        a.part('B', clip=lo, line=False).ell(cx - 8 * s, cy - 1, cx + 8 * s, cy + 5 * s)
        t = a.part('C')
        for k in range(-4, 5):
            t.line([(cx + k * 2.2 * s, cy - 1), (cx + k * 2.6 * s, cy - 5 * s)], .7)


def succulent(a, sp, r):
    """Living stones / mother of thousands / resurrection plant / jackal food. A body, B top window/marks, C plantlets, D ground."""
    kind = sp.get('kind', 'stones')
    _ground(a, 'D', 50)
    if kind == 'stones':
        for cx in (22, 42):
            st = a.part('A').blob([(cx - 9, 52), (cx - 9, 36), (cx, 30), (cx + 9, 36), (cx + 9, 52)])
            a.part('B', clip=st, line=False).ell(cx - 7, 30, cx + 7, 38)
        a.part('E').circle(32, 32, 3)
        return
    if kind == 'thousands':
        a.part('A').line([(32, 52), (32, 20)], 3)
        lv = a.part('A')
        for (x, y, s) in [(20, 42, -1), (44, 36, 1), (20, 28, -1), (44, 22, 1)]:
            lv.blob([(32, y), (32 + s * 18, y - 6), (32 + s * 22, y + 2), (32 + s * 8, y + 6)], 2)
        pl = a.part('C')
        for (x, y) in [(10, 36), (16, 40), (52, 30), (56, 34), (12, 22), (52, 16)]:
            pl.circle(x, y, 1.6)
        return
    if kind == 'resurrection':
        ball = a.part('A')
        for k in range(10):
            t = k * math.pi / 5
            ball.curve((32, 40), (32 + 14 * math.cos(t), 40 + 10 * math.sin(t)), (32 + 6 * math.cos(t + 1), 36 + 6 * math.sin(t + 1)), 3, 1.5)
        a.part('B').circle(32, 38, 4)
        return
    # jackal food (Hydnora): fleshy lobed flower breaking through sand
    lo = a.part('A')
    for k in range(3):
        t = math.radians(-90 + k * 120)
        lo.blob([(32, 40), (32 + 18 * math.cos(t - .4), 40 + 14 * math.sin(t - .4)), (32 + 20 * math.cos(t), 40 + 16 * math.sin(t)), (32 + 18 * math.cos(t + .4), 40 + 14 * math.sin(t + .4))], 2)
    a.part('B').circle(32, 40, 6)
    bristles = a.part('E')
    for k in range(3):
        t = math.radians(-90 + k * 120)
        bristles.line([(32 + 8 * math.cos(t), 40 + 6 * math.sin(t)), (32 + 18 * math.cos(t), 40 + 14 * math.sin(t))], 1.2)


def frondplant(a, sp, r):
    """Cycad / horsetail / ghost pipe / killer alga. A plant, B trunk/joints, D ground. kind: cycad, horsetail, ghostpipe, caulerpa."""
    kind = sp.get('kind', 'cycad')
    if kind == 'caulerpa':
        a.part('D').rect(0, 52, 64, 64)
        a.part('A').line([(0, 52), (64, 50)], 2)
        fr = a.part('A')
        for x in (12, 26, 40, 54):
            fr.line([(x, 52), (x, 22)], 2)
            for y in range(24, 50, 4):
                fr.line([(x, y), (x - 4, y - 3)], 1.2).line([(x, y), (x + 4, y - 3)], 1.2)
        return
    _ground(a)
    if kind == 'cycad':
        a.part('B').rect(27, 30, 37, 58)
        sc = a.part('B', line=False)
        for y in range(32, 58, 4):
            sc.rect(27, y, 37, y + .8)
        fr = a.part('A')
        for k in range(7):
            t = math.radians(200 + k * 23)
            fr.curve((32, 30), (32 + 16 * math.cos(t), 30 + 12 * math.sin(t)), (32 + 28 * math.cos(t), 34 + 20 * math.sin(t)), 3, 1.5)
        return
    if kind == 'horsetail':
        st = a.part('A')
        for x in (20, 32, 44):
            st.line([(x, 58), (x + (x - 32) * .1, 10)], 3)
        j = a.part('B', clip=st, line=False)
        for y in range(14, 58, 6):
            j.rect(0, y, 64, y + 1.2)
        br = a.part('A')
        for x in (20, 32, 44):
            for y in range(18, 50, 6):
                br.line([(x, y), (x - 5, y + 4)], .8).line([(x, y), (x + 5, y + 4)], .8)
        a.part('B').ell(42, 4, 48, 14)
        return
    # ghost pipe
    st = a.part('A')
    for (x, lean) in [(22, -6), (32, 0), (42, 6)]:
        st.curve((x, 58), (x, 30), (x + lean, 18), 3, 2.5)
        st.blob([(x + lean - 4, 16), (x + lean + 4, 16), (x + lean + 2, 26), (x + lean - 2, 26)], 1)
    a.part('B').circle(32, 26, 1).circle(16, 26, 1)


def kelp(a, sp, r):
    """Giant kelp: stipe with floats and blades. A blades, B stipe, C floats."""
    a.part('D').rect(0, 58, 64, 64)
    a.part('B').curve((32, 60), (24, 30), (36, 0), 2, 1.5)
    bl = a.part('A')
    for k in range(6):
        y = 50 - k * 8
        x = 32 + 4 * math.sin(k)
        side = 1 if k % 2 else -1
        bl.blob([(x, y), (x + side * 18, y - 10), (x + side * 22, y - 6), (x + side * 6, y + 2)], 2)
    fl = a.part('C')
    for k in range(6):
        y = 50 - k * 8
        x = 32 + 4 * math.sin(k)
        fl.circle(x + (2 if k % 2 else -2), y - 1, 1.8)


def mushroom(a, sp, r):
    """Mushroom. A cap, B stem, C spots/gills, D ground, E volva/net. kind: agaric, deathcap, termite, veiled."""
    kind = sp.get('kind', 'agaric')
    _ground(a)
    if kind == 'termite':
        a.part('B').taper([(32, 58), (32, 30), (32, 18)], 4, 3)
        cap = a.part('A').blob([(14, 22), (24, 14), (32, 6), (40, 14), (50, 22), (32, 22)])
        a.part('C', clip=cap, line=False).circle(32, 10, 3)
        return
    a.part('B').rect(28, 26, 36, 58)
    if kind == 'deathcap':
        a.part('E').blob([(24, 58), (26, 50), (38, 50), (40, 58)])
        a.part('E').rect(26, 32, 38, 34)
    if kind == 'veiled':
        net = a.part('E')
        net.blob([(18, 54), (24, 26), (40, 26), (46, 54)])
        holes = a.part('D', clip=net, line=False)
        for y in range(30, 54, 4):
            for x in range(20, 46, 4):
                holes.circle(x + (y % 8) / 2, y, 1)
        a.part('B').rect(28, 22, 36, 56)
    cap = a.part('A').blob([(8, 28), (14, 14), (32, 6), (50, 14), (56, 28), (32, 30)] if kind != 'veiled' else
                          [(18, 24), (22, 12), (32, 8), (42, 12), (46, 24), (32, 26)])
    if sp.get('spots'):
        s = a.part('C', clip=cap, line=False)
        for (x, y) in [(18, 18), (28, 12), (40, 13), (46, 21), (24, 23), (36, 20)]:
            s.circle(x, y, 2)
    a.part('C').rect(12, 27, 52, 30) if kind == 'agaric' else None


def bracket(a, sp, r):
    """Shelf fungus on a log (chicken of the woods). A shelves, B edges, D log."""
    a.part('D').rect(0, 8, 22, 64)
    for (y, w) in [(16, 40), (28, 46), (40, 38)]:
        sh = a.part('A').blob([(18, y), (18 + w, y + 2), (18 + w * .9, y + 8), (18, y + 10)], 2)
        a.part('B', clip=sh, line=False).rect(0, y + 6, 64, y + 12)


def birdsnest(a, sp, r):
    """Bird's nest fungus: cups holding egg-like peridioles. A cups, B eggs, D wood."""
    a.part('D').rect(0, 46, 64, 64)
    for (x, w) in [(18, 10), (40, 12), (54, 7)]:
        cup = a.part('A').poly([(x - w, 30), (x + w, 30), (x + w * .5, 48), (x - w * .5, 48)])
        a.part('K', clip=cup).ell(x - w + 1, 28, x + w - 1, 34)
        a.part('B').circle(x - 3, 33, 2).circle(x + 2, 33, 2)


def mold(a, sp, r):
    """Mould colony on food. A sporangia/colony, B stalks/hyphae, D substrate. kind: pin (bread mould), brush (penicillium), fuzz, grapes (noble rot), potato."""
    kind = sp.get('kind', 'pin')
    if kind == 'grapes':
        a.part('B').line([(32, 4), (32, 18)], 2)
        g = a.part('D')
        for (x, y) in [(26, 22), (36, 22), (22, 30), (32, 30), (42, 30), (26, 38), (36, 38), (30, 46)]:
            g.circle(x, y, 6)
        f = a.part('A', clip=g, line=False)
        for _ in range(30):
            x, y = 16 + 32 * next(r), 16 + 34 * next(r)
            f.circle(x, y, 1)
        return
    if kind == 'potato':
        lf = a.part('D').blob([(4, 40), (20, 12), (44, 10), (60, 34), (40, 54), (14, 54)])
        a.part('A', clip=lf, line=False).blob([(14, 30), (30, 20), (44, 30), (34, 44), (18, 42)])
        a.part('B').line([(10, 50), (60, 20)], 1.2)
        return
    a.part('D').blob([(0, 50), (16, 44), (48, 44), (64, 50), (64, 64), (0, 64)])
    st = a.part('B')
    heads = []
    for k in range(9):
        x = 6 + k * 6.5
        h = 16 + 14 * next(r)
        st.line([(x, 48), (x + 2 * (next(r) - .5), 48 - h)], 1 if kind != 'fuzz' else 2)
        heads.append((x, 48 - h))
    hd = a.part('A')
    for (x, y) in heads:
        if kind == 'brush':
            for k in range(-2, 3):
                hd.line([(x, y), (x + k * 2, y - 5)], 1)
        elif kind == 'fuzz':
            hd.circle(x, y, 3.5)
        else:
            hd.circle(x, y, 2.2)


def rust(a, sp, r):
    """Cedar-apple rust: gall with orange gelatinous horns on a twig. A horns, B gall, D twig."""
    a.part('D').line([(0, 40), (64, 30)], 3)
    a.part('B').circle(32, 36, 8)
    h = a.part('A')
    for k in range(10):
        t = k * math.pi / 5
        h.taper([(32 + 6 * math.cos(t), 36 + 6 * math.sin(t)), (32 + 20 * math.cos(t), 36 + 18 * math.sin(t))], 3, 2)


def ergot(a, sp, r):
    """Ergot: dark sclerotia sprouting from a rye head. A sclerotia, B grain head, D stalk."""
    a.part('D').line([(32, 64), (32, 14)], 1.6)
    g = a.part('B')
    for y in range(10, 44, 5):
        g.ell(26, y, 32, y + 5).ell(32, y, 38, y + 5)
    a.part('A').taper([(30, 24), (24, 18), (20, 8)], 3, 2).taper([(34, 32), (42, 26), (46, 16)], 3, 2)


def hatthrower(a, sp, r):
    """Pilobolus on dung: glassy swollen stalks with black caps. A stalk, B caps, D dung."""
    a.part('D').blob([(0, 54), (20, 44), (44, 44), (64, 52), (64, 64), (0, 64)])
    for x in (20, 34, 46):
        a.part('A').taper([(x, 50), (x, 34), (x, 26)], 2, 5)
        a.part('B').ell(x - 3, 20, x + 3, 26)


def lichen(a, sp, r):
    """Lichen on rock. A thallus, B rock, C fruiting cups/tips. kind: crust (leafy lobes), tufts (fog lichen)."""
    rock = a.part('B').blob([(2, 58), (6, 34), (24, 22), (44, 24), (60, 38), (62, 58)])
    if sp.get('kind') == 'tufts':
        t = a.part('A')
        for _ in range(9):
            x, y = 12 + 40 * next(r), 26 + 26 * next(r)
            for k in range(5):
                t.line([(x, y), (x - 4 + k * 2, y - 8)], 1.2)
        return
    lo = a.part('A', clip=rock)
    for _ in range(7):
        x, y = 12 + 40 * next(r), 28 + 26 * next(r)
        lo.blob([(x - 7, y), (x - 3, y - 6), (x + 5, y - 5), (x + 7, y + 2), (x, y + 6)], 2)
    c = a.part('C', clip=lo, line=False)
    for _ in range(8):
        x, y = 10 + 44 * next(r), 26 + 28 * next(r)
        c.circle(x, y, 1)


def slimemold(a, sp, r):
    """Slime moulds. A body, B stalk/veins, C sorus, D substrate. kind: foam (dog vomit), candy (pink/white beads), slug, fruiting."""
    kind = sp.get('kind', 'foam')
    a.part('D').rect(0, 48, 64, 64)
    if kind == 'fruiting':
        a.part('B').taper([(32, 50), (32, 30), (32, 16)], 3, 1.4)
        a.part('A').circle(32, 12, 7)
        return
    if kind == 'slug':
        a.part('A').taper([(54, 46), (36, 44), (18, 42), (8, 40)], 4, 7)
        a.part('B').line([(54, 46), (64, 48)], 1)
        return
    if kind == 'candy':
        for x in (16, 28, 40, 50):
            a.part('B').line([(x, 48), (x, 34)], 1.6)
            a.part('A').circle(x, 32, 4.5)
        return
    f = a.part('A').blob([(4, 50), (10, 30), (26, 24), (44, 26), (58, 36), (60, 50)])
    holes = a.part('C', clip=f, line=False)
    for _ in range(14):
        x, y = 10 + 46 * next(r), 28 + 20 * next(r)
        holes.circle(x, y, 1.2)


def snowalga(a, sp, r):
    """Watermelon snow: pink patches on a snowfield. A pink, C snow, D sky/rock."""
    a.part('D').poly([(0, 30), (20, 10), (36, 22), (52, 6), (64, 20), (64, 64), (0, 64)])
    snow = a.part('C').poly([(0, 36), (20, 18), (36, 28), (52, 14), (64, 26), (64, 64), (0, 64)])
    p = a.part('A', clip=snow, line=False)
    for _ in range(8):
        x, y = 6 + 52 * next(r), 30 + 30 * next(r)
        p.blob([(x - 6, y), (x, y - 3), (x + 7, y), (x, y + 3)], 2)


def wineglass(a, sp, r):
    """Mermaid's wineglass (Acetabularia): green stalks with umbrella caps. A caps, B stalks, D rock."""
    a.part('D').rect(0, 54, 64, 64)
    for (x, h) in [(18, 22), (32, 12), (46, 26)]:
        a.part('B').line([(x, 56), (x, h)], 1.4)
        cap = a.part('A').ell(x - 8, h - 3, x + 8, h + 3)
        rib = a.part('A', clip=cap)
        for k in range(-3, 4):
            rib.line([(x, h), (x + k * 3, h + 3)], .5)
