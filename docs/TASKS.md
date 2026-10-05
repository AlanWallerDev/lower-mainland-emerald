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
- [x] Title screen silhouette: Marbled Murrelet in flight (`atlas/make_title_bird.py`, `docs/title.png`)

## P2 Roster
- [x] `atlas/bc_species.json` (Living Atlas schema, `bc-` ids) for new BC species (148)
- [x] Picker: regional slots take BC organisms only; worldwide organisms fill the rest
- [x] Run the picker with `--write` once `bc_species.json` fills the regional slots
- [x] Starters Skunk Cabbage, Morel, American Beaver with three life stages each
- [x] Legendaries and mythicals in their slots
- [x] Cryptid islands (Faraway, Navel Rock, Birth Island, Southern Island) reachable after the credits: the VANCOUVER harbour desk gives all four tickets once the game is cleared (played: `postgame.txt`)
- [x] Sprite specs for every new organism
- [x] Wild tables by real BC habitat per location (`bc_habitats` tags)
- [x] Every trainer party uses BC organisms

## P3 World
- [x] Place renames from the P1 table (towns, landmarks, routes)
- [x] BC TrailNav region map (`atlas/region_map.json`, `make_region_map.py`; TRAILNAV header and BC MAP button by `make_trailnav.py`)
- [x] Palette swap: coast greens, conifer greens, Pacific blue water (`atlas/recolor.json`)
- [x] Conifer tree art: tiered conifer shading on all tree tiles, pointed tops (`atlas/conifer_tiles.py`)
- [ ] New tiles: arbutus coast, sagebrush, cannery, float homes
- [x] Signs and landmark text (town mottos, route signs, HOODOO SPIRE, GLACIER VAULT, CADBORO ROCK, RATTLESNAKE ISLE)

## P4 Story
- [x] CINDER and RIPTIDE: team names, leaders and admins (names in `atlas/characters.json`)
- [x] CINDER and RIPTIDE motives in dialogue (fire and flood) (`atlas/text/07_motives.tsv`)
- [x] Dialogue follows the species map (organism names tracked by `rename_text.js`)
- [x] Area-by-area dialogue pass, LADNER to WHISTLER (`atlas/text/14-35`, read with `node atlas/dump_text.js`)
- [x] MOUNTAIN VIEW legend retold for BC: forest bear and glass reef, calmed by the murrelet
- [x] Elite Four and Champion names: VAUX, CAMERON, NEWMAN (with SMITH and VANCOUVER)
- [ ] Dialogue pass for the BATTLE FRONTIER, TRAINER HILL and TV shows (generic; low priority)

- [x] Regi braille inscriptions shown as Burgess Shale survey notes (played: `survey.txt`)
- [x] Post-game island tickets at the VANCOUVER harbour desk (played: `postgame.txt`)

## P5 Signature maps
- [ ] Burgess Shale dig (Yoho)
- [ ] Adams River salmon run
- [ ] Hecate sponge reef dive

## P6 Polish
- [x] Currency shown as \$ (`atlas/make_dollar.py`)
- [x] Text width checker for messages and item descriptions (`atlas/check_text.js`)
- [ ] Overworld creature sprites (the DEEP COVE clash still shows Groudon and Kyogre shapes), back sprites, move names, playtest fixes
