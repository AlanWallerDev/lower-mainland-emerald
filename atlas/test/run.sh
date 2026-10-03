#!/bin/sh
# Run a harness script against the built ROM. Screenshots land in build/test/ as PNGs.
# Usage: atlas/test/run.sh atlas/test/scripts/opening.txt
set -e
cd "$(dirname "$0")/../.."
OUT=build/test
mkdir -p "$OUT"
[ -x build/harness ] || cc -O2 -o build/harness atlas/test/harness.c -lmgba
sed "s#\$OUT#$OUT#g" "$1" > "$OUT/script.txt"
build/harness pokeemerald_modern.gba "$OUT/script.txt"
for f in "$OUT"/*.ppm; do
	[ -e "$f" ] && python3 -c "import sys; from PIL import Image; Image.open(sys.argv[1]).save(sys.argv[1][:-4] + '.png')" "$f" && rm "$f"
done
ls "$OUT"/*.png
