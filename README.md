# Lower Mainland Emerald

A hack of Pokémon Emerald, built on the [pret/pokeemerald](https://github.com/pret/pokeemerald)
decompilation, where every creature is a real organism from the *Living Atlas* species database
and the region is the Lower Mainland of British Columbia.

**This repository holds source only. It never contains ROMs.** You build the game yourself.

## What's different

| Area | Change |
|---|---|
| Organisms | All 386 species replaced with Living Atlas organisms, southwest-BC species first (banana slug, red fox, beaver, orca, bald eagle, plus fungi, kelp and slime molds). Stats, types, Field Journal entries, heights and weights come from the database. Only real life stages evolve (caterpillars, moon jellies, slime molds). |
| Types | The 15 Living Atlas types (Common, Ember, Aqua, Verdant, Frost, Brawn, Toxin, Soil, Sky, Mind, Chitin, Stone, Night, Armor, Charm) with the Living Atlas type chart. Ghost and Dragon are retired; their moves were retyped. |
| Art | Stand-in sprites drawn per organism from its own art spec: a body rig (fox, raccoon, orca, puffin, owl, butterfly, jelly, mushroom, sequoia, tardigrade…) with the organism's real colours and markings. Microbes appear in a microscope field. New title logo. |
| Places | Towns, routes and landmarks renamed to Lower Mainland places: Ladner, Richmond, Burnaby, Steveston, Surrey, Harrison, Vancouver, Deep Cove, Whistler, River Road, Burns Bog, Sea to Sky… |
| Text | No Pokémon terms: organisms, partners, FIELD JOURNAL, FIELD STATION, FIELD JAR, TRAILNAV, NATURALIST, NATURE LEAGUE. Old species names in dialogue are now the organisms. |
| Wild areas | Every route, cave and sea refilled by habitat (forest, meadow, cave, volcanic, cemetery, power plant, fresh water, sea, deep sea…). |
| Nuzlocke | Built in, chosen once at new game: first encounter per area only (dupes and shiny clauses), fainted partners are gone for good, every catch is nicknamed. |
| Game speed | OPTIONS → GAME SPEED 1x / 2x / 4x. Speeds up walking, battles and the intro; menus and screen transitions stay at normal speed. |

## Build

Requirements: the pokeemerald toolchain (see [INSTALL.md](INSTALL.md); `make modern` needs
`arm-none-eabi-gcc`, plus `libpng`), Node 18+, Python 3 with Pillow.

```sh
make tools
make modern            # builds pokeemerald_modern.gba from the committed sources
```

The generated sources are committed, so `make modern` is all you need to play. To regenerate them
from the Living Atlas data (for example after the database changes), run `atlas/build.sh` on a
clean tree.

## The atlas/ folder

| File | What it does |
|---|---|
| `pick_species.js`, `picks.json` | Chooses 386 organisms (BC first) and matches them to slots by type and stat total. Writes `species_map.json`. |
| `names.json` | 10-character in-game names. |
| `apply_species.js`, `lib/moves.js` | Species data, Field Journal, learnsets, TM/tutor compatibility, evolutions. |
| `apply_types.py` | Type names, chart, retyped moves, type icons. |
| `make_sprites.py`, `sprites/` | Stand-in art: `sprites/engine.py` renderer, `rigs_*.py` body rigs, `specs_*.py` one entry per organism (rig, colours, markings). Preview: `python3 -m atlas.sprites.preview out.png all`. |
| `make_title.py` | Title logo. |
| `apply_wild.js` | Habitat-based wild encounters. |
| `locations.json`, `apply_locations.js` | Place names. |
| `apply_text.js`, `lib/text.js` | Terminology pass and re-wrapping to the message box. |
| `polish_text.js`, `polish_text.tsv` | Hand-checked phrase fixes on top of the terminology pass (grammar, leftovers). |
| `test/harness.c`, `test/run.sh`, `test/scripts/` | Headless mGBA runner with scripted input and screenshots. |

C changes live in `src/nuzlocke.c` (rules), `src/option_menu.c` and `src/main.c` (game speed),
and small hooks marked `Living Atlas` across the battle, item and save code.

## Known gaps

- Overworld sprites of creatures in cutscenes (e.g. the one chasing the professor) are still the original art.
- Back sprites are mirrored front sprites, not true rear views.
- Dialogue was converted automatically, then given a hand-checked grammar pass (`atlas/polish_text.tsv`). Some lines still read stiffly, and dialogue still names the original types (FIRE-type and so on) rather than the new ones.
- Few freshwater species exist in the database, so some rivers and ponds borrow coastal organisms.
- Move names are unchanged.
- The boot screen keeps the original copyright notice for the base game.

The original decompilation README is in [README.pret.md](README.pret.md).
