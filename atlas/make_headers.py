#!/usr/bin/env python3
"""Repaint baked-in text in menu graphics. The TrailNav map header reads "BC MAP" instead of
"HOENN MAP" (letters from the header's own 5x9 font; B and C drawn to match), and the Field Journal
search screen's "POKeDEX" wordmark reads "JOURNAL" in a matching bold font.
Run from the repo root: python3 atlas/make_headers.py (idempotent).
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADER = os.path.join(ROOT, 'graphics', 'pokenav', 'left_headers', 'hoenn_map.png')
WHITE, SHADOW, BG = 1, 2, 8
TOP, ROWS, LEFT, RIGHT = 7, 9, 4, 55  # text box inside the button

EXTRA = {
    'B': ['1111.', '1...1', '1...1', '1...1', '1111.', '1...1', '1...1', '1...1', '1111.'],
    'C': ['.111.', '1...1', '1....', '1....', '1....', '1....', '1....', '1...1', '.111.'],
}


def glyphs_from(im, text):
    """Cut the letters of `text` (as drawn on the header) into 5x9 white-pixel masks."""
    cols = [x for x in range(LEFT, RIGHT + 1) if any(im.getpixel((x, y)) == WHITE for y in range(TOP, TOP + ROWS))]
    runs, start = [], cols[0]
    for a, b in zip(cols, cols[1:] + [None]):
        if b != a + 1:
            runs.append((start, a))
            start = b
    letters = [c for c in text if c != ' ']
    out = {}
    for ch, (a, b) in zip(letters, runs):
        out[ch] = [''.join('1' if im.getpixel((x, y)) == WHITE else '.' for x in range(a, a + 5)) for y in range(TOP, TOP + ROWS)]
    return out


def main():
    im = Image.open(HEADER)
    font = glyphs_from(im, 'HOENN MAP')
    if len(font) != len(set('HOENNMAP')) or font['H'][4] != '11111':
        return  # already repainted
    font.update(EXTRA)
    for y in range(TOP, TOP + ROWS + 1):
        for x in range(LEFT, RIGHT + 1):
            im.putpixel((x, y), BG)
    x0 = LEFT
    for ch in 'BC MAP':
        if ch != ' ':
            g = font[ch]
            for dy, row in enumerate(g):
                for dx, c in enumerate(row):
                    if c == '1':
                        im.putpixel((x0 + dx, TOP + dy), WHITE)
            for dy, row in enumerate(g):
                for dx, c in enumerate(row):
                    if c == '1':
                        for sx, sy in ((x0 + dx + 1, TOP + dy), (x0 + dx, TOP + dy + 1)):
                            if im.getpixel((sx, sy)) == BG:
                                im.putpixel((sx, sy), SHADOW)
        x0 += 6
    im.save(HEADER)


def wordmark():
    path = os.path.join(ROOT, 'graphics', 'pokedex', 'search_menu.png')
    im = Image.open(path)
    INK, PAPER = 15, 3
    if any(im.getpixel((x, 9)) != INK for x in range(14, 25)):
        return  # already repainted
    font = {
        'J': ['......XXXX', '......XXXX', '......XXXX', '......XXXX', 'XXXX..XXXX', '.XXXXXXXX.'],
        'O': ['.XXXXXXXX.', 'XXXX..XXXX', 'XXXX..XXXX', 'XXXX..XXXX', 'XXXX..XXXX', '.XXXXXXXX.'],
        'U': ['XXXX..XXXX', 'XXXX..XXXX', 'XXXX..XXXX', 'XXXX..XXXX', 'XXXX..XXXX', '.XXXXXXXX.'],
        'R': ['XXXXXXXXX.', 'XXXX..XXXX', 'XXXXXXXXX.', 'XXXX.XXXX.', 'XXXX..XXXX', 'XXXX..XXXX'],
        'N': ['XXXX...XXX', 'XXXXX..XXX', 'XXXXXX.XXX', 'XXX.XXXXXX', 'XXX..XXXXX', 'XXX...XXXX'],
        'A': ['.XXXXXXXX.', 'XXXX..XXXX', 'XXXX..XXXX', 'XXXXXXXXXX', 'XXXX..XXXX', 'XXXX..XXXX'],
        'L': ['XXXX......', 'XXXX......', 'XXXX......', 'XXXX......', 'XXXX......', 'XXXXXXXXXX'],
    }
    for y in range(9, 15):
        for x in range(13, 112):
            if im.getpixel((x, y)) == INK:
                im.putpixel((x, y), PAPER)
    text = 'JOURNAL'
    width = len(text) * 10 + (len(text) - 1) * 2
    x0 = 14 + (98 - width) // 2
    for ch in text:
        for dy, row in enumerate(font[ch]):
            for dx, c in enumerate(row):
                if c == 'X':
                    im.putpixel((x0 + dx, 9 + dy), INK)
        x0 += 12
    im.save(path)


main()
wordmark()
