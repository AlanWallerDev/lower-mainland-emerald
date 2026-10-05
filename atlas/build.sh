#!/bin/sh
# Regenerate the hack's generated sources from atlas/ data and build the ROM.
# Every step is idempotent and works on the committed tree.
#   LIVING_ATLAS_DIR  Living Atlas checkout (default ../living-atlas); falls back to atlas/data/.
# The picker and the title need the pret remote:
#   git remote add upstream https://github.com/pret/pokeemerald && git fetch --depth 1 upstream master
# To re-pick organisms for the slots (after editing atlas/picks.json or atlas/bc_species.json),
# run `node atlas/pick_species.js --write` first.
set -e
cd "$(dirname "$0")/.."
python3 atlas/apply_types.py
node atlas/apply_species.js
node atlas/theme_trainers.js
python3 atlas/make_sprites.py
python3 atlas/make_creature_sprites.py
python3 atlas/body_colors.py
python3 atlas/make_title.py
python3 atlas/make_dollar.py
python3 atlas/make_title_bird.py
python3 atlas/make_transitions.py
python3 atlas/make_headers.py
python3 atlas/make_trailnav.py
python3 atlas/make_zoom_text.py
python3 atlas/make_journal_ui.py
python3 atlas/make_region_map.py
python3 atlas/recolor_tiles.py
python3 atlas/conifer_tiles.py
node atlas/apply_wild.js
node atlas/rename_text.js
make modern -j"$(nproc)"
