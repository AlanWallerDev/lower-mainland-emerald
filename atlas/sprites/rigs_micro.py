"""Microscopic organisms, drawn inside a magnifying glass (C is the lens's field colour): the view is
drawn full size, then shrunk into the lens, which gets a dark rim, a glint and a handle.
A main cell colour, B secondary (nucleus, shell, flagella), D detail, E glow/eyespot."""
import math


def _field(a):
    a.part('C').circle(32, 32, 30)


def micro(a, sp, r):
    """shape: rod, rods, coccus, cluster, chain, diplo, spiral, vibrio, filament, square, lobed, branching,
    stalked, magnet, cable, colony, tetrad, virus_rod, virus_ico, virus_giant, amoeba, slipper, pear, barrel,
    trumpet, bell, longworm, swan, euglena, giardia, eyed, diatom, radiolarian, foram, testate, urn, sun,
    dino, crescent, golden, didymo, chromat, tardigrade, tun, rotifer, nematode, gastrotrich, placozoan,
    spore, anchor, budding, hyphae, sporangium, asgard, desmid, chlamy, volvox, redcell."""
    shape = sp.get('shape', 'rod')
    _field(a)
    f = SHAPES.get(shape)
    if f is None:
        raise KeyError(shape)
    f(a, sp, r)
    _magnifier(a)


LENS = (26, 26, 23.5)  # centre and radius of the lens after shrinking the 30-radius field


def _magnifier(a):
    cx, cy, rad = LENS
    a.shrink(rad / 30, cx, cy)
    a.part('K', line=False).ring(cx, cy, rad + 2.5, 3)
    a.part('W', line=False).curve((cx - rad * .62, cy - rad * .05), (cx - rad * .62, cy - rad * .62),
                                  (cx - rad * .05, cy - rad * .62), 1.6)
    d = (rad + 2.5) / 2 ** .5
    a.part('K').line([(cx + d, cy + d), (cx + d + 3, cy + d + 3)], 4.5)   # collar
    a.part('D').line([(cx + d + 3, cy + d + 3), (61, 61)], 6)            # grip


def _flagella(a, pts, role='B', w=.8):
    a.part(role).taper(pts, w, w * .6)


def rod(a, sp, r):
    a.part('A').line([(18, 36), (46, 28)], 12)
    if sp.get('flag'):
        _flagella(a, [(46, 28), (54, 22), (58, 28), (62, 22)])
    a.part('B', line=False).line([(26, 34), (38, 30)], 2)


def rods(a, sp, r):
    p = a.part('A')
    for _ in range(6):
        x, y = 14 + 32 * next(r), 14 + 32 * next(r)
        t = next(r) * math.pi
        p.line([(x - 5 * math.cos(t), y - 5 * math.sin(t)), (x + 5 * math.cos(t), y + 5 * math.sin(t))], 5)
    if sp.get('flag'):
        fl = a.part('B')
        for _ in range(4):
            x, y = 14 + 32 * next(r), 14 + 32 * next(r)
            fl.curve((x, y), (x + 4, y - 6), (x + 8, y - 2), .7, .5)


def coccus(a, sp, r):
    a.part('A').circle(32, 32, 14)
    a.part('B', line=False).circle(30, 30, 4)


def cluster(a, sp, r):
    p = a.part('A')
    for (x, y) in [(26, 26), (34, 24), (40, 30), (22, 34), (30, 34), (38, 38), (28, 42), (44, 22)]:
        p.circle(x, y, 5)


def chain(a, sp, r):
    p = a.part('A')
    for k in range(7):
        p.circle(10 + k * 7, 32 + 6 * math.sin(k * .7), 4)


def diplo(a, sp, r):
    a.part('A').circle(24, 32, 9).circle(40, 32, 9)


def tetrad(a, sp, r):
    a.part('A').circle(25, 25, 7).circle(39, 25, 7).circle(25, 39, 7).circle(39, 39, 7)


def spiral(a, sp, r):
    pts = [(10 + k * 3, 32 + 8 * math.sin(k * .9)) for k in range(16)]
    a.part('A').taper(pts, 4.5, 4)
    if sp.get('magnets'):
        m = a.part('K')
        for k in range(4, 12, 2):
            m.circle(pts[k][0], pts[k][1], 1)
    _flagella(a, [pts[-1], (58, 28), (62, 34)])


def vibrio(a, sp, r):
    a.part('A').curve((16, 40), (30, 20), (46, 34), 9, 8)
    _flagella(a, [(46, 34), (54, 40), (60, 36)])


def filament(a, sp, r):
    p = a.part('A')
    pts = [(6 + k * 4, 32 + 6 * math.sin(k * .5)) for k in range(14)]
    p.taper(pts, 6, 6)
    d = a.part('B', clip=p, line=False)
    for x in range(8, 60, 5):
        d.rect(x, 0, x + .8, 64)
    if sp.get('sulfur'):
        s = a.part('E', clip=p, line=False)
        for (x, y) in pts[::2]:
            s.circle(x, y, 1)


def square(a, sp, r):
    a.part('A').rect(16, 16, 48, 48)
    g = a.part('E', line=False)
    for (x, y) in [(22, 24), (34, 30), (26, 40), (40, 42)]:
        g.circle(x, y, 1.5)


def lobed(a, sp, r):
    a.part('A').blob([(18, 30), (24, 18), (36, 20), (46, 26), (44, 40), (34, 46), (22, 42)])


def branching(a, sp, r):
    p = a.part('A')
    p.line([(10, 50), (30, 32), (54, 14)], 2)
    for (x, y) in [(20, 41), (30, 32), (42, 23)]:
        p.line([(x, y), (x + 6, y + 10)], 1.6).line([(x, y), (x - 6, y - 8)], 1.6)
    sp_ = a.part('B')
    for (x, y) in [(56, 12), (26, 51), (36, 42), (48, 33), (14, 33), (24, 24), (36, 15)]:
        for k in range(3):
            sp_.circle(x + k * 1.6, y - k * 1.6, 1)


def stalked(a, sp, r):
    a.part('B').line([(40, 40), (54, 52)], 1.4)
    a.part('A').curve((16, 26), (24, 20), (40, 38), 9, 8)


def magnet(a, sp, r):
    spiral(a, dict(sp, magnets=True), r)


def cable(a, sp, r):
    p = a.part('A')
    for k in range(16):
        p.rect(2 + k * 4, 30, 5.5 + k * 4, 34)
    a.part('E', line=False).line([(2, 32), (62, 32)], .6)


def colony(a, sp, r):
    a.part('B').blob([(12, 32), (20, 16), (40, 14), (52, 30), (44, 48), (22, 50)])
    p = a.part('A')
    for _ in range(22):
        x, y = 18 + 28 * next(r), 18 + 28 * next(r)
        p.circle(x, y, 2)


def virus_rod(a, sp, r):
    v = a.part('A').rect(10, 26, 54, 38)
    d = a.part('B', clip=v, line=False)
    for x in range(12, 54, 3):
        d.rect(x, 26, x + 1, 38)


def virus_ico(a, sp, r):
    s = sp.get('size', 14)
    pts = [(32 + s * math.cos(math.radians(30 + k * 60)), 30 + s * math.sin(math.radians(30 + k * 60))) for k in range(6)]
    v = a.part('A').poly(pts)
    a.part('B', clip=v).poly([(32, 30 - s), (32 + s * .87, 30 + s * .5), (32 - s * .87, 30 + s * .5)])
    if sp.get('tail'):
        a.part('B').rect(30, 30 + s, 34, 30 + s + 12)
        legs = a.part('B')
        for dx in (-8, -3, 3, 8):
            legs.line([(32, 30 + s + 12), (32 + dx, 30 + s + 18)], 1)


def virus_giant(a, sp, r):
    virus_ico(a, dict(sp, size=17), r)
    h = a.part('D')
    for k in range(24):
        t = k * math.pi / 12
        h.line([(32 + 17 * math.cos(t), 30 + 17 * math.sin(t)), (32 + 23 * math.cos(t), 30 + 23 * math.sin(t))], 1)


def amoeba(a, sp, r):
    a.part('A').blob([(10, 30), (18, 14), (30, 22), (40, 10), (54, 24), (48, 36), (56, 48), (36, 46), (24, 54), (14, 42)])
    a.part('B').circle(32, 32, 5)
    v = a.part('D', line=False)
    for _ in range(6):
        x, y = 18 + 28 * next(r), 20 + 24 * next(r)
        v.circle(x, y, 1.2)


def slipper(a, sp, r):
    c = a.part('A').blob([(10, 30), (20, 22), (40, 22), (54, 30), (40, 40), (20, 40)])
    cil = a.part('A')
    for k in range(20):
        t = k * math.pi / 10
        cil.line([(32 + 22 * math.cos(t), 31 + 9 * math.sin(t)), (32 + 26 * math.cos(t), 31 + 12 * math.sin(t))], .6)
    a.part('B').ell(26, 27, 36, 35)
    a.part('D', line=False).blob([(18, 32), (26, 30), (24, 36)])


def pear(a, sp, r):
    a.part('A').blob([(32, 12), (44, 26), (44, 44), (32, 52), (20, 44), (20, 26)])
    cil = a.part('A')
    for k in range(16):
        t = k * math.pi / 8
        cil.line([(32 + 13 * math.cos(t), 33 + 19 * math.sin(t)), (32 + 16 * math.cos(t), 33 + 23 * math.sin(t))], .6)
    a.part('B').circle(32, 36, 5)


def barrel(a, sp, r):
    a.part('A').ell(18, 18, 46, 48)
    b = a.part('B')
    b.rect(16, 26, 48, 28).rect(16, 38, 48, 40)
    a.part('D').poly([(28, 18), (32, 10), (36, 18)])


def trumpet(a, sp, r):
    a.part('A').blob([(12, 14), (36, 10), (48, 18), (40, 30), (34, 52), (28, 54), (26, 30)])
    cil = a.part('D')
    for k in range(10):
        cil.line([(14 + k * 3.2, 12 - (k % 2)), (14 + k * 3.2, 8)], .6)
    beads = a.part('B')
    for k in range(5):
        beads.circle(34 - k * .4, 20 + k * 6, 1.5)


def bell(a, sp, r):
    a.part('B').curve((32, 34), (24, 44), (32, 58), 1, 1)
    a.part('A').blob([(18, 16), (46, 16), (40, 34), (24, 34)])
    cil = a.part('D')
    for k in range(9):
        cil.line([(18 + k * 3.5, 16), (18 + k * 3.5, 12)], .6)


def longworm(a, sp, r):
    pts = [(8 + k * 3.5, 32 + 4 * math.sin(k * .5)) for k in range(15)]
    a.part('A').taper(pts, 5, 4)
    a.part('B').line([pts[6], pts[9]], 2)


def swan(a, sp, r):
    a.part('A').blob([(28, 36), (36, 28), (50, 32), (54, 42), (42, 48), (30, 46)])
    a.part('A').curve((32, 34), (16, 30), (12, 10), 3, 1.2)
    a.part('B').circle(42, 40, 3)


def euglena(a, sp, r):
    a.part('A').blob([(10, 32), (18, 26), (40, 24), (54, 30), (40, 38), (18, 38)])
    ch = a.part('B', line=False)
    for x in (20, 26, 32, 38, 44):
        ch.ell(x - 2, 28, x + 2, 34)
    a.part('E').circle(14, 30, 2)
    _flagella(a, [(10, 32), (4, 26), (8, 18), (4, 12)])


def chlamy(a, sp, r):
    a.part('A').ell(20, 22, 44, 50)
    a.part('B', line=False).blob([(22, 30), (32, 46), (42, 30), (40, 44), (24, 44)])
    a.part('E').circle(24, 30, 2)
    _flagella(a, [(30, 22), (24, 12), (18, 10)])
    _flagella(a, [(34, 22), (40, 12), (46, 10)])


def giardia(a, sp, r):
    a.part('A').blob([(32, 10), (46, 22), (44, 40), (32, 54), (20, 40), (18, 22)])
    a.part('B').circle(26, 26, 4).circle(38, 26, 4)
    for (p0, p1) in [((26, 40), (14, 56)), ((38, 40), (50, 56)), ((32, 52), (32, 62)), ((22, 34), (8, 40)), ((42, 34), (56, 40))]:
        _flagella(a, [p0, p1])


def eyed(a, sp, r):
    a.part('A').blob([(14, 32), (22, 20), (42, 20), (50, 32), (42, 46), (22, 46)])
    a.part('K').circle(26, 30, 5)
    a.part('E').circle(25, 29, 2)
    a.part('D').line([(30, 44), (50, 50)], 1)


def diatom(a, sp, r):
    if sp.get('pennate'):
        v = a.part('A').blob([(8, 32), (20, 24), (44, 24), (56, 32), (44, 40), (20, 40)])
        d = a.part('B', clip=v, line=False)
        for x in range(10, 56, 3):
            d.rect(x, 20, x + .8, 44)
        a.part('B').line([(10, 32), (54, 32)], .8)
    else:
        v = a.part('A').circle(32, 32, 18)
        d = a.part('B', clip=v, line=False)
        for k in range(16):
            t = k * math.pi / 8
            d.line([(32, 32), (32 + 18 * math.cos(t), 32 + 18 * math.sin(t))], .8)


def radiolarian(a, sp, r):
    sp_ = a.part('B')
    for k in range(12):
        t = k * math.pi / 6
        sp_.line([(32, 32), (32 + 28 * math.cos(t), 32 + 28 * math.sin(t))], 1)
    v = a.part('A').circle(32, 32, 14)
    h = a.part('C', clip=v, line=False)
    for _ in range(14):
        x, y = 20 + 24 * next(r), 20 + 24 * next(r)
        h.circle(x, y, 1.6)


def foram(a, sp, r):
    ps = a.part('D')
    for k in range(10):
        t = k * math.pi / 5
        ps.line([(32, 32), (32 + 28 * math.cos(t), 32 + 28 * math.sin(t))], .6)
    sh = a.part('A')
    for k in range(7):
        t = k * .8
        rr = 4 + k * 1.6
        sh.circle(32 + (8 - k) * math.cos(t), 32 + (8 - k) * math.sin(t), rr)


def testate(a, sp, r):
    a.part('A').ell(12, 22, 52, 44)
    a.part('B').ell(26, 30, 38, 38)
    a.part('D').blob([(26, 44), (22, 52), (32, 48), (40, 54), (38, 44)])


def urn(a, sp, r):
    v = a.part('A').blob([(32, 10), (44, 22), (46, 40), (38, 52), (26, 52), (18, 40), (20, 22)])
    g = a.part('B', clip=v, line=False)
    for _ in range(18):
        x, y = 20 + 24 * next(r), 14 + 38 * next(r)
        g.circle(x, y, 1.4)
    a.part('D').blob([(28, 52), (26, 58), (36, 58), (36, 52)])


def sun(a, sp, r):
    ax = a.part('B')
    for k in range(18):
        t = k * math.pi / 9
        ax.line([(32, 32), (32 + 28 * math.cos(t), 32 + 28 * math.sin(t))], .9)
    a.part('A').circle(32, 32, 13)
    a.part('D', line=False).circle(32, 32, 4)


def dino(a, sp, r):
    a.part('A').circle(32, 32, 18)
    g = a.part('E', line=False)
    for _ in range(12):
        x, y = 20 + 24 * next(r), 20 + 24 * next(r)
        g.circle(x, y, 1.2)
    _flagella(a, [(32, 50), (34, 58), (30, 62)])


def crescent(a, sp, r):
    a.part('A').curve((14, 44), (32, 10), (50, 44), 8, 4)
    a.part('B').circle(32, 24, 3)


def golden(a, sp, r):
    p = a.part('A')
    for (x, y) in [(24, 24), (40, 24), (32, 38), (20, 40), (44, 40)]:
        p.circle(x, y, 7)
    d = a.part('B', line=False)
    for (x, y) in [(24, 24), (40, 24), (32, 38), (20, 40), (44, 40)]:
        d.circle(x - 1, y - 1, 2)


def didymo(a, sp, r):
    st = a.part('B')
    for k in range(6):
        st.curve((32, 60), (20 + k * 5, 40), (14 + k * 7, 14), 1.2, 1)
    ce = a.part('A')
    for k in range(6):
        ce.ell(10 + k * 7, 8, 18 + k * 7, 18)


def chromat(a, sp, r):
    v = a.part('A').ell(14, 18, 50, 48)
    a.part('B', clip=v, line=False).ell(20, 26, 30, 40).ell(34, 26, 44, 40)
    sc = a.part('D', clip=v, line=False)
    for x in range(14, 50, 4):
        sc.rect(x, 16, x + .8, 50)


def tardigrade(a, sp, r):
    legs = a.part('A')
    for x in (16, 26, 36, 46):
        legs.line([(x, 40), (x - 2, 52)], 4.5)
    cl = a.part('K')
    for x in (16, 26, 36, 46):
        cl.line([(x - 2, 53), (x - 5, 56)], .7).line([(x - 2, 53), (x, 57)], .7)
    body = a.part('A').blob([(6, 34), (12, 24), (32, 20), (52, 24), (58, 34), (50, 44), (14, 44)])
    seg = a.part('A', clip=body)
    for x in (20, 30, 40, 50):
        seg.rect(x, 18, x + .8, 46)
    a.part('B').circle(8, 32, 3)
    a.eye(10, 28, 1)


def tun(a, sp, r):
    body = a.part('A').blob([(14, 32), (22, 22), (42, 22), (50, 32), (42, 42), (22, 42)])
    seg = a.part('A', clip=body)
    for x in (24, 30, 36, 42):
        seg.rect(x, 18, x + .8, 46)


def rotifer(a, sp, r):
    a.part('A').blob([(26, 20), (38, 20), (42, 36), (36, 54), (28, 54), (22, 36)])
    a.part('A').line([(32, 54), (32, 62)], 2)
    for cx in (24, 40):
        wheel = a.part('B').circle(cx, 16, 6)
        cil = a.part('D')
        for k in range(10):
            t = k * math.pi / 5
            cil.line([(cx + 6 * math.cos(t), 16 + 6 * math.sin(t)), (cx + 9 * math.cos(t), 16 + 9 * math.sin(t))], .6)
    a.part('E').circle(32, 36, 3)


def nematode(a, sp, r):
    pts = [(6 + k * 4, 32 + 10 * math.sin(k * .6)) for k in range(14)]
    a.part('A').taper(pts, 4, 1.5)
    a.part('B', line=False).taper(pts[2:10], 1.2, 1.2)


def gastrotrich(a, sp, r):
    b = a.part('A').blob([(32, 10), (40, 18), (38, 30), (42, 46), (36, 54), (28, 54), (22, 46), (26, 30), (24, 18)])
    sp_ = a.part('B')
    for y in range(16, 50, 4):
        sp_.line([(24, y), (20, y - 2)], .6).line([(40, y), (44, y - 2)], .6)
    a.part('A').line([(28, 54), (24, 60)], 1.6).line([(36, 54), (40, 60)], 1.6)


def placozoan(a, sp, r):
    a.part('A').blob([(8, 30), (16, 14), (34, 18), (50, 10), (56, 30), (48, 48), (28, 52), (12, 44)])
    d = a.part('B', line=False)
    for _ in range(20):
        x, y = 14 + 36 * next(r), 16 + 30 * next(r)
        d.circle(x, y, .9)


def spore(a, sp, r):
    v = a.part('A').blob([(32, 12), (46, 26), (44, 44), (32, 52), (20, 44), (18, 26)])
    a.part('B').ell(24, 16, 31, 28).ell(33, 16, 40, 28)
    _flagella(a, [(32, 52), (28, 58), (34, 62)])


def anchor(a, sp, r):
    a.part('A').line([(32, 8), (32, 36)], 4)
    arms = a.part('A')
    for ang in (210, 330, 90):
        t = math.radians(ang)
        arms.curve((32, 36), (32 + 14 * math.cos(t), 36 - 10 * math.sin(t)), (32 + 26 * math.cos(t), 36 - 4 * math.sin(t) + (16 if ang == 90 else 0)), 3, 1.5)
    a.part('B').circle(32, 10, 3)


def budding(a, sp, r):
    p = a.part('A')
    p.ell(14, 22, 38, 46).ell(34, 18, 50, 32).ell(30, 40, 42, 52)
    if sp.get('hyph'):
        p.line([(38, 30), (58, 18)], 3)
    a.part('B', line=False).circle(24, 32, 3)


def hyphae(a, sp, r):
    p = a.part('A')
    p.line([(6, 52), (30, 34), (58, 30)], 2).line([(30, 34), (36, 10)], 2).line([(18, 44), (10, 26)], 1.6)
    if sp.get('loops'):
        lo = a.part('B')
        for (x, y) in [(36, 12), (10, 24), (58, 30)]:
            lo.circle(x, y, 4)
        lc = a.part('C')
        for (x, y) in [(36, 12), (10, 24), (58, 30)]:
            lc.circle(x, y, 2)
        a.part('D').taper([(40, 50), (50, 44), (60, 48)], 2.5, 1.5)
    if sp.get('root'):
        a.part('B').taper([(2, 10), (30, 20), (62, 14)], 7, 5)
    if sp.get('black'):
        a.part('A').circle(30, 34, 8)


def sporangium(a, sp, r):
    a.part('B').line([(32, 40), (20, 56)], 1).line([(32, 40), (44, 58)], 1).line([(32, 40), (32, 60)], 1)
    a.part('A').circle(32, 28, 13)
    z = a.part('D', line=False)
    for _ in range(8):
        x, y = 24 + 16 * next(r), 20 + 16 * next(r)
        z.circle(x, y, 1.3)


def asgard(a, sp, r):
    a.part('A').circle(32, 32, 10)
    t = a.part('A')
    for k in range(7):
        ang = k * math.pi * 2 / 7
        t.curve((32 + 8 * math.cos(ang), 32 + 8 * math.sin(ang)), (32 + 16 * math.cos(ang + .4), 32 + 16 * math.sin(ang + .4)), (32 + 24 * math.cos(ang), 32 + 24 * math.sin(ang)), 2, 1.4)


def desmid(a, sp, r):
    v = a.part('A')
    for side in (-1, 1):
        v.blob([(32, 32), (32 + side * 20, 12), (32 + side * 26, 22), (32 + side * 22, 32), (32 + side * 26, 42), (32 + side * 20, 52)], 1)
    a.part('B').rect(31, 14, 33, 50)


def volvox(a, sp, r):
    v = a.part('A').circle(32, 32, 24)
    c = a.part('B', clip=v, line=False)
    for _ in range(40):
        x, y = 10 + 44 * next(r), 10 + 44 * next(r)
        c.circle(x, y, .9)
    d = a.part('D')
    for (x, y, s) in [(26, 28, 5), (38, 36, 6), (30, 42, 4)]:
        d.circle(x, y, s)


def redcell(a, sp, r):
    a.part('A').circle(32, 32, 15)
    a.part('B', line=False).circle(32, 32, 8)
    if sp.get('flag'):
        _flagella(a, [(30, 17), (24, 8)])
        _flagella(a, [(34, 17), (40, 8)])


def blob(a, sp, r):
    """Macroscopic jelly blob (star jelly / Nostoc colony) on grass."""
    a.part('D').rect(0, 48, 64, 64)
    a.part('A').blob([(8, 48), (14, 30), (30, 24), (46, 28), (56, 44), (40, 52), (18, 52)])
    a.part('B', line=False).ell(20, 30, 34, 38)


SHAPES = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k not in ('micro',)}
__all__ = ['micro']
