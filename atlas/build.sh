#!/bin/sh
# Regenerate everything from the Living Atlas data and build the ROM.
# The species, text and graphics steps rewrite source files; run them from a clean tree
# (git stash or a fresh checkout) when changing the pipeline itself.
#   LIVING_ATLAS_DIR  Living Atlas checkout (default ../living-atlas); falls back to atlas/data/.
set -e
cd "$(dirname "$0")/.."
node atlas/pick_species.js
node atlas/apply_species.js
node atlas/theme_trainers.js
python3 atlas/apply_types.py
python3 atlas/make_sprites.py
python3 atlas/make_title.py
python3 atlas/make_headers.py
node atlas/apply_wild.js
node atlas/apply_locations.js
node atlas/apply_text.js
node atlas/polish_text.js
node atlas/npc_names.js
node atlas/region_text.js
node atlas/apply_type_text.js
node atlas/polish_text.js atlas/type_text.tsv
make modern -j"$(nproc)"
