# Tasks

Phases come from `docs/BC_PLAN.md`. Keep each task finishable in one session.

## P0 Housekeeping
- [x] Expansion plan approved
- [x] Build and headless harness verified in the cloud container
- [x] `docs/STATE.md`, `docs/TASKS.md`, `CLAUDE.md`
- [x] Rewrite the Node pipeline scripts so `atlas/build.sh` runs again

## P1 Design lock
- [x] Final Hoenn-to-BC place table in `atlas/locations.json` (towns, routes, landmarks)
- [x] 202-entry BC roster list: slot, organism, habitat, life-stage lines (`docs/ROSTER.md`)
- [x] Title chosen (Pokémon BC); new title logo
- [ ] Title screen silhouette: Rayquaza to Marbled Murrelet

## P2 Roster
- [x] `atlas/bc_species.json` (Living Atlas schema, `bc-` ids) for new BC species (148)
- [x] Picker: regional slots take BC organisms only; worldwide organisms fill the rest
- [x] Run the picker with `--write` once `bc_species.json` fills the regional slots
- [x] Starters Skunk Cabbage, Morel, American Beaver with three life stages each
- [x] Legendaries and mythicals in their slots
- [ ] Cryptid islands (Faraway, Navel Rock, Birth Island) reachable after the credits without tickets
- [x] Sprite specs for every new organism
- [x] Wild tables by real BC habitat per location (`bc_habitats` tags)
- [x] Every trainer party uses BC organisms

## P3 World
- [x] Place renames from the P1 table (towns, landmarks, routes)
- [x] BC TrailNav region map (`atlas/region_map.json`, `make_region_map.py`; TRAILNAV header and BC MAP button by `make_trailnav.py`)
- [x] Palette swap: coast greens, conifer greens, Pacific blue water (`atlas/recolor.json`)
- [ ] Conifer tree art: redraw the 32x32 tree and its ~30 forest variants (tips, edges, overlaps)
- [ ] New tiles: arbutus coast, sagebrush, cannery, float homes
- [ ] Signs and landmark text

## P4 Story
- [ ] CINDER and RIPTIDE: names, grunts, leaders, hideouts
- [ ] Area-by-area dialogue rewrite, checked with mGBA scripts

## P5 Signature maps
- [ ] Burgess Shale dig (Yoho)
- [ ] Adams River salmon run
- [ ] Hecate sponge reef dive

## P6 Polish
- [ ] Overworld creature sprites, back sprites, move names, playtest fixes
