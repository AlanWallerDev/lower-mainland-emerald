"""Part-based pixel sprite renderer for stand-in organism art.

A sprite is a stack of parts. Each part is a set of shapes (ellipses, polygons, thick lines) drawn on a
64x64 design grid, with a colour role:

    A  main colour (3 tones)        B  secondary colour (3 tones)
    C  light / belly colour (2)     D  pattern colour (2)
    E  accent: beak, bill, eye ring, lure (2)
    W  white                        K  black

Rendering supersamples the shapes, downsamples to 64x64, then shades each part (light rim top-left,
shadow bottom-right), draws a darker line where a part sits on top of another, and outlines the whole
silhouette. The result is a 16-colour indexed image ready for the GBA.
"""
import colorsys
import math
import zlib

from PIL import Image, ImageDraw

S = 4  # supersampling factor
N = 64

BG = (152, 208, 160)
IDX = {'A': (2, 3, 4), 'B': (5, 6, 7), 'C': (8, 9, 8), 'D': (10, 11, 10), 'E': (12, 13, 12),
       'W': (14, 9, 14), 'K': (15, 15, 15)}
OUTLINE = 1


def hexrgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def tone(rgb, f):
    """f < 1 darkens, f > 1 lightens (toward white)."""
    h, l, s = colorsys.rgb_to_hls(*[c / 255 for c in rgb])
    l = l * f if f < 1 else l + (1 - l) * (f - 1)
    return tuple(int(round(c * 255)) for c in colorsys.hls_to_rgb(h, max(0, min(1, l)), s))


def hue(rgb, d, sat=1.0):
    h, l, s = colorsys.rgb_to_hls(*[c / 255 for c in rgb])
    return tuple(int(round(c * 255)) for c in colorsys.hls_to_rgb((h + d) % 1, l, min(1, s * sat)))


def palette(colors, shiny=False):
    """16-colour palette from a spec's role colours (hex strings)."""
    get = lambda k, d: hexrgb(colors.get(k, d))
    a, b = get('A', '#888888'), get('B', colors.get('A', '#666666'))
    c, d, e = get('C', '#e8e0d0'), get('D', '#303030'), get('E', '#e0a020')
    if shiny:
        a, b, d = hue(a, 0.36, 1.2), hue(b, 0.36, 1.2), hue(d, 0.36)
    dark = min((a, b), key=lambda x: sum(x))
    outline = tone(dark, 0.3) if sum(dark) > 120 else (16, 16, 24)
    pal = [BG, outline, a, tone(a, 0.68), tone(a, 1.35), b, tone(b, 0.68), tone(b, 1.35), c, tone(c, 0.78),
           d, tone(d, 0.65) if sum(d) > 90 else tone(d, 1.6), e, tone(e, 0.7), (248, 248, 248), (20, 20, 28)]
    return pal


def rng(seed):
    x = zlib.crc32(seed.encode()) or 1
    while True:
        x ^= (x << 13) & 0xffffffff
        x ^= x >> 17
        x ^= (x << 5) & 0xffffffff
        yield (x & 0xffff) / 0xffff


class Part:
    def __init__(self, art, role, clip=None, line=True):
        self.art, self.role, self.clip, self.edge = art, role, clip, line
        self.mask = Image.new('L', (N * S, N * S), 0)
        self.d = ImageDraw.Draw(self.mask)

    # Shapes (design-grid coordinates, floats allowed)
    def ell(self, x0, y0, x1, y1):
        self.d.ellipse([x0 * S, y0 * S, x1 * S, y1 * S], fill=255)
        return self

    def circle(self, cx, cy, r):
        return self.ell(cx - r, cy - r, cx + r, cy + r)

    def poly(self, pts):
        self.d.polygon([(x * S, y * S) for x, y in pts], fill=255)
        return self

    def blob(self, pts, n=3):
        """Smooth closed shape through rough control points (Chaikin corner cutting)."""
        p = list(pts)
        for _ in range(n):
            q = []
            for i in range(len(p)):
                (x0, y0), (x1, y1) = p[i], p[(i + 1) % len(p)]
                q += [(x0 * .75 + x1 * .25, y0 * .75 + y1 * .25), (x0 * .25 + x1 * .75, y0 * .25 + y1 * .75)]
            p = q
        return self.poly(p)

    def line(self, pts, w):
        w2 = w * S
        sp = [(x * S, y * S) for x, y in pts]
        self.d.line(sp, fill=255, width=max(1, int(round(w2))), joint='curve')
        for x, y in sp:
            self.d.ellipse([x - w2 / 2, y - w2 / 2, x + w2 / 2, y + w2 / 2], fill=255)
        return self

    def taper(self, pts, w0, w1):
        """A line whose width goes from w0 to w1 (tails, tentacles, horns)."""
        n = len(pts)
        for i in range(n - 1):
            t = i / max(1, n - 2)
            self.line([pts[i], pts[i + 1]], w0 + (w1 - w0) * t)
        return self

    def ring(self, cx, cy, r, w):
        """A circle outline of width w (lens rims)."""
        self.circle(cx, cy, r)
        self.d.ellipse([(cx - r + w) * S, (cy - r + w) * S, (cx + r - w) * S, (cy + r - w) * S], fill=0)
        return self

    def rect(self, x0, y0, x1, y1):
        self.d.rectangle([x0 * S, y0 * S, x1 * S, y1 * S], fill=255)
        return self

    def curve(self, p0, p1, p2, w, w1=None, steps=10):
        """Quadratic bezier stroke."""
        pts = [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
                (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]) for t in [i / steps for i in range(steps + 1)]]
        return self.taper(pts, w, w if w1 is None else w1)


class Art:
    def __init__(self):
        self.parts = []
        self.eyes = []

    def part(self, role, clip=None, line=True):
        p = Part(self, role, clip, line)
        self.parts.append(p)
        return p

    def shrink(self, k, cx, cy):
        """Scale everything drawn so far by k about the canvas centre and move that centre to (cx, cy)."""
        size = int(round(N * S * k))
        for p in self.parts:
            small = p.mask.resize((size, size), Image.LANCZOS)
            p.mask = Image.new('L', (N * S, N * S), 0)
            p.mask.paste(small, (int(round((cx - N * k / 2) * S)), int(round((cy - N * k / 2) * S))))
            p.d = ImageDraw.Draw(p.mask)
        self.eyes = [(cx + (x - N / 2) * k, cy + (y - N / 2) * k, size_, st) for x, y, size_, st in self.eyes]

    def eye(self, x, y, size=1, style='dot'):
        """style: dot (black), big (black with highlight), red (E colour iris), white (W ring), pale."""
        self.eyes.append((x, y, size, style))

    # ---- render
    def render(self, back=False):
        masks = []
        for p in self.parts:
            m = p.mask
            if p.clip is not None:
                m = Image.composite(m, Image.new('L', m.size, 0), p.clip.mask)
            m = m.resize((N, N), Image.BOX).point(lambda v: 255 if v >= 100 else 0)
            masks.append(m.load())
        pid = [[-1] * N for _ in range(N)]
        for i, m in enumerate(masks):
            for y in range(N):
                for x in range(N):
                    if m[x, y]:
                        pid[y][x] = i
        sil = lambda x, y: 0 <= x < N and 0 <= y < N and pid[y][x] >= 0
        pidat = lambda x, y: pid[y][x] if 0 <= x < N and 0 <= y < N else -1
        im = Image.new('P', (N, N), 0)
        px = im.load()
        for y in range(N):
            for x in range(N):
                i = pid[y][x]
                if i < 0:
                    continue
                p = self.parts[i]
                base, sh, li = IDX[p.role]
                if p.edge and any(0 <= pidat(x + dx, y + dy) < i for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    px[x, y] = sh
                elif not sil(x + 1, y + 1) or not sil(x + 2, y + 2) or (back and not sil(x - 2, y)):
                    px[x, y] = sh
                elif not sil(x - 1, y - 1):
                    px[x, y] = li
                else:
                    px[x, y] = base
        for y in range(N):
            for x in range(N):
                if pid[y][x] < 0 and any(sil(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    px[x, y] = OUTLINE
        if not back:
            for (ex, ey, size, style) in self.eyes:
                ex, ey = int(round(ex)), int(round(ey))
                r = size
                for dy in range(-r + 1, r):
                    for dx in range(-r + 1, r):
                        if 0 <= ex + dx < N and 0 <= ey + dy < N:
                            px[ex + dx, ey + dy] = {'red': 12, 'pale': 9, 'white': 14}.get(style, 15)
                if style in ('big', 'red', 'white') and size >= 2:
                    px[ex - 1 if size > 1 else ex, ey - 1] = 14 if style != 'white' else 15
                if size == 1:
                    px[ex, ey] = {'red': 12, 'pale': 9, 'white': 14}.get(style, 15)
        return im


def flip(im):
    return im.transpose(Image.FLIP_LEFT_RIGHT)
