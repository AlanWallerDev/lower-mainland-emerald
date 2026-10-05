#!/bin/sh
# Run a harness script against the built ROM. Screenshots land in build/test/ as PNGs.
# Usage: atlas/test/run.sh atlas/test/scripts/opening.txt
set -e
cd "$(dirname "$0")/../.."
OUT=build/test
mkdir -p "$OUT"
[ build/harness -nt atlas/test/harness.c ] || cc -O2 -o build/harness atlas/test/harness.c -lmgba
SB1=$(awk '$2 == "gSaveBlock1Ptr" {print $1; exit}' pokeemerald_modern.map)
sed -e "s#\$OUT#$OUT#g" -e "s#@gSaveBlock1Ptr#$SB1#g" "$1" > "$OUT/script.txt"
build/harness pokeemerald_modern.gba "$OUT/script.txt"
for f in "$OUT"/*.ppm; do
	[ -e "$f" ] && python3 -c "import sys; from PIL import Image; Image.open(sys.argv[1]).save(sys.argv[1][:-4] + '.png')" "$f" && rm "$f"
done
ls "$OUT"/*.png
