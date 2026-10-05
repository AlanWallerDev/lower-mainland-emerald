# Pokémon BC

A hack of Pokémon Emerald, built on the [pret/pokeemerald](https://github.com/pret/pokeemerald)
decompilation, where every creature is a real organism from the *Living Atlas* species database
and the region is British Columbia. The hack is being expanded province-wide: see [docs/BC_PLAN.md](docs/BC_PLAN.md).

**This repository holds source only. It never contains ROMs.** You build the game yourself.

## What's different

| Area | Change |
|---|---|
| Organisms | A 202-entry BC Field Journal: every regional organism lives in BC (148 added for the hack in `atlas/bc_species.json`, the rest from Living Atlas). Starters Skunk Cabbage, Morel and Beaver; very rare BC organisms as legendaries; Sasquatch, Caddy and Ogopogo as mythicals. The other 184 slots hold worldwide organisms. Only real life stages evolve. Full list: [docs/ROSTER.md](docs/ROSTER.md). |
| Types | The 15 Living Atlas types (Common, Ember, Aqua, Verdant, Frost, Brawn, Toxin, Soil, Sky, Mind, Chitin, Stone, Night, Armor, Charm) with the Living Atlas type chart. Ghost and Dragon are retired; their moves were retyped. |
| Title | **Pokémon BC**: original wordmark, "BC" banner in place of "EMERALD VERSION" (`atlas/make_title.py`). |
| Art | Stand-in sprites drawn per organism from its own art spec: a body rig (fox, raccoon, orca, puffin, owl, butterfly, jelly, mushroom, sequoia, tardigrade…) with the organism's real colours and markings. Microbes appear in a microscope field. New title logo. |
| Places | Towns, routes and landmarks renamed across BC: Ladner, Richmond, Squamish, Tofino, Victoria, Hope, Kamloops, Revelstoke, Vancouver, Prince Rupert, Deep Cove, Whistler; the Coquihalla, Rogers Pass, the Inside Passage, Hecate Reef, Burns Bog, Sea to Sky… |
| Text | No Pokémon terms: organisms, partners, FIELD JOURNAL, FIELD STATION, FIELD JAR, TRAILNAV, NATURALIST, NATURE LEAGUE. Old species names in dialogue are now the organisms. |
| Wild areas | Every route, cave and sea refilled by habitat (forest, meadow, cave, volcanic, cemetery, power plant, fresh water, sea, deep sea…). |
| Nuzlocke | Built in, chosen once at new game: first encounter per area only (dupes and shiny clauses), partners that faint (in battle or from poison) are released after the fight, every catch is nicknamed, and losing your whole party ends the run and erases the save. |
| Game speed | OPTIONS → GAME SPEED 1x / 2x / 4x. Speeds up walking, battles and the intro; menus and screen transitions stay at normal speed. |

## Build

Requirements: the pokeemerald toolchain (see [INSTALL.md](INSTALL.md); `make modern` needs
`arm-none-eabi-gcc`, plus `libpng`), Node 18+, Python 3 with Pillow.

```sh
make tools
make modern            # builds pokeemerald_modern.gba from the committed sources
```

The generated sources are committed, so `make modern` is all you need to play. To regenerate them
after changing anything in `atlas/` (or the Living Atlas data), run `atlas/build.sh`. Every step is
idempotent and works on the committed tree. The picker and the title step need the pret remote:
`git remote add upstream https://github.com/pret/pokeemerald && git fetch --depth 1 upstream master`.

## The atlas/ folder

| File | What it does |
|---|---|
| `pick_species.js`, `picks.json` | Chooses an organism for each of the 386 slots: the 202 regional slots take BC organisms only (`bc_native` plus `bc_species.json`), the rest take worldwide ones. Life stages go into evolution chains; the rest match by type and stat total. Reports by default; `--write` writes `species_map.json` (refused while any slot is empty). Not part of `build.sh`. |
| `bc_species.json` | The hack's BC organisms (Living Atlas schema plus `bc_habitats`, `stage_index`, `invasive`; `override` entries replace a Living Atlas organism for the hack only). Art in `sprites/specs_bc.py`. |
| `roster_doc.js` | Writes `docs/ROSTER.md` from the current map. |
| `names.json` | 10-character in-game names (others come from the organism's name). |
| `apply_species.js`, `lib/moves.js` | Stats, types, abilities, gender, egg groups, names, Field Journal entries and text, evolutions (real life stages only), level-up, TM/HM and tutor learnsets. |
| `body_colors.py` | Field Journal colour search: each species' body colour from its sprite. |
| `apply_types.py` | Type names, chart, retyped moves, type icons. |
| `make_sprites.py`, `sprites/` | Stand-in art: `sprites/engine.py` renderer, `rigs_*.py` body rigs, `specs_*.py` one entry per organism (rig, colours, markings). Preview: `python3 -m atlas.sprites.preview out.png all`. |
| `make_title.py` | Title logo: original wordmark plus a "BC" banner. |
| `region_map.json`, `make_region_map.py` | The BC region map (TrailNav and Fly): terrain grid, section cells and landmark positions, drawn into the map tiles, tilemap, section grid and section positions. |
| `recolor.json`, `recolor_tiles.py` | Overworld recolour: exact colours swapped in every tileset palette (mossy grass, conifer greens, Pacific water). |
| `conifer_tiles.py` | Conifer trees: re-shades every tree tile in the general tileset into drooping tiers and points the standalone tree tops. |
| `make_trailnav.py` | TRAILNAV header and BC MAP button in the device graphics. |
| `make_headers.py` | Repaints baked-in menu text: "BC MAP" TrailNav header, "JOURNAL" search-screen wordmark. |
| `theme_trainers.js` | Every trainer uses BC organisms; gym leaders, gym trainers, Elite Four and Champion get organisms of their gym's type. |
| `apply_wild.js`, `habitats.json` | Wild encounters by habitat. Each area keeps upstream's levels and rarity pattern. |
| `rename_text.js`, `locations.json`, `characters.json`, `text/` | Keeps game text in step: edit a name in `locations.json` or `characters.json`, or add a table to `text/`, and it is applied once everywhere (`text/applied.json` records what is applied). Phrases match across line breaks; overflowing lines are re-wrapped. |
| `lib/text.js`, `lib/replace.js`, `lib/common.js` | Font widths and wrapping, find-and-replace across game text, shared data helpers. |
| `test/harness.c`, `test/run.sh`, `test/scripts/` | Headless mGBA runner with scripted input and screenshots (`setflag @gSaveBlock1Ptr FLAG` sets a save flag; `trailnav.txt` opens the BC map). |

The original one-time passes that converted upstream text (terminology, character names, region
name, type names) are not kept as scripts: they would corrupt the converted text if rerun. The
committed text is the baseline, and `rename_text.js` applies changes on top of it.

C changes live in `src/nuzlocke.c` (rules), `src/option_menu.c` and `src/main.c` (game speed),
and small hooks marked `Living Atlas` across the battle, item and save code.

## Known gaps

- Overworld sprites of creatures in cutscenes (e.g. the one chasing the professor) are still the original art.
- Back sprites are mirrored front sprites, not true rear views.
- Dialogue was converted automatically, then given a hand-checked grammar pass (`atlas/polish_text.tsv`). Some lines still read stiffly.
- Move names are unchanged.
- The boot screen keeps the original copyright notice for the base game.

The original decompilation README is in [README.pret.md](README.pret.md).
