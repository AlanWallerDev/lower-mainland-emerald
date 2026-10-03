#!/usr/bin/env python3
"""Contact sheet of harness screenshots: sheet.py out.png cols shot1.ppm shot2.ppm ..."""
import sys

from PIL import Image

out, cols, files = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
ims = [Image.open(f).resize((240, 160), Image.NEAREST) for f in files]
rows = (len(ims) + cols - 1) // cols
sheet = Image.new('RGB', (cols * 244, rows * 164), 'white')
for i, im in enumerate(ims):
    sheet.paste(im, ((i % cols) * 244, (i // cols) * 164))
sheet.save(out)
