# State

Updated at the end of every session. Read this first, then `docs/TASKS.md` and `docs/BC_PLAN.md`.

## Last session: creature sprites, rigs and baked-in text (2026-10-05)

**Done**
- **Overworld creature sprites** for every walking, chasing and legendary slot, built from each
  slot's battle sprite (`atlas/make_creature_sprites.py`, replacing `make_legend_sprites.py`);
  shared NPC palettes are matched by nearest colour without the townsfolk greens. Dolls (41) and
  the big-doll decoration icons (10) show their organisms too.
- The professor's chaser and the intro creature are the raccoon (ZIGZAGOON slot) again.
- **Rigs**: deer family (`cervid`: moose, elk, deer, caribou) and sea mammals (`sealion`,
  `seaotter`, river otter tail) replace the goat and seal stand-ins.
- Kanto visitors come from the PRAIRIES.
- **Baked-in text** in graphics: TrailNav close-up legend (FIELD STATION, MART, GYM, BATTLE TENT,
  CONTEST HALL; `make_zoom_text.py`), Journal title and menu rows and the BC list label
  (`make_journal_ui.py`), type icons with the hack's type names (`make_type_icons.py`), PC
  storage menu DATA and PARTY (`make_pc_menu.py`). Bag, naming, trade, shop and party graphics
  checked: nothing to change.
- **New BC tiles**: ECHO BAY's huts are plank float homes with slate metal roofs and stovepipes
  (`float_homes.py`, same tile slots). `bc_tiles.py` adds metatiles to a town's own tileset and
  places them: a red Steveston cannery on pilings in RICHMOND's north-east pond (the item ball's
  surf route stays open), sagebrush for every sand pebble on the COQUIHALLA, five arbutus trees on
  VICTORIA's shore grass (placed off events; a reachability check found no cut-off cells). Seen in
  game: harness `newtiles.txt`, `docs/new_tiles.png`.
- **BURGESS SHALE dig**: ROGERS PASS's side cave (SCORCHED SLAB, never renamed until now) is the
  BURGESS SHALE. Surf across the meltwater tarn to the quarry bench: the dig leader tells how mud
  buried soft-bodied animals 500 million years ago and that CHARLES WALCOTT found the beds in 1909,
  gives a HARD STONE ("a chip of the shale", `FLAG_RECEIVED_SHALE_HARD_STONE`, was unused flag
  0x20), then points to HALLUCIGEN, ANOMALO and the sleeping MARRELLA, OPABINIA and PIKAIA (the
  Regi puzzle); a digger says every fossil stays on the mountain. The TM ball moved to a corner.
  Harness `shale.txt`, `docs/burgess_shale.png`.
- **Cushions and posters**: the organism cushions are drawn from their battle sprites like the
  dolls, and named for them with the posters (BEE, FUNGUS, RACCOON, JELLY, GOOSE, LIZARD;
  `atlas/text/42_decor.tsv`). Poster art (secret base tiles) is unchanged.
- **Move names** audited: plain English, no Pokemon names or terms; left as they are.

## Earlier session: dialogue pass, LADNER to WHISTLER (2026-10-05)

The owner delegated all details (story, dialogue, names) to Claude: decide, build, log here.

**Done**
- **Dialogue pass, every story area** (`atlas/text/14-35`; read an area with
  `node atlas/dump_text.js MapPrefix`). Highlights:
  - LADNER is a fishing village on the delta (dykes, snow geese); TSAWWASSEN's footprint sketcher
    hunts SASQUATCH; TOFINO is at the end of the road, not an island; SUMMIT began at the
    BRITANNIA BEACH copper mine; YALE is a gold rush town; KAMLOOPS replants pines after wildfire;
    HARRISON's springs are fault-heated; the COQUIHALLA sands are badlands with a sandstone
    HOODOO SPIRE; the weather gift is a BLACKTAIL deer from a storm; ECHO BAY floats over kelp.
  - MOUNTAIN VIEW's legend: the white bear of the forest (drought, fire) against the glass reef of
    the deep (storms, rising sea), calmed by the marbled murrelet, which nests in old trees and
    feeds at sea. DEEP COVE's crowd cheers the bear, the reef and the little bird.
  - CINDER grunts and leader now speak their fire motive everywhere (no more "expand the land").
  - New place names: HOODOO SPIRE/RUINS/UNDERPASS, GLACIER VAULT (ROGERS PASS), CADBORO ROCK,
    RATTLESNAKE ISLE; Elite Four VAUX (Glacia) and CAMERON (Phoebe), Champion NEWMAN (Wallace).
  - 25 organism cries rewritten to fit (raccoons churr, the lobster mushroom sits still);
    TRAINER restored for NATURALIST; Dragon/Ghost text gone (DRAGON TAMER is FALCONER);
    NANAIMO BARS replace LAVA COOKIES; SPINE and CLAW FOSSILS from the BURGESS SHALE.
  - Grammar slips from the organism swap (plural/singular, 'a'/'an') fixed game-wide.
- **Dollars**: the currency glyph is drawn as $ in every font (`atlas/make_dollar.py`,
  `docs/money.png`).
- **Checks**: `node atlas/check_text.js` flags message lines over 208px and item description
  lines over 109px that differ from upstream; currently 0. `replace.js` rows can be scoped to one
  C variable.
- **Title screen**: a marbled murrelet in flight replaces Rayquaza's silhouette, eye in the
  pulsing marking colour (`atlas/make_title_bird.py`, `docs/title.png`).
- **Legendary overworld sprites**: the spirit bear, sponge reef and murrelet replace Groudon,
  Kyogre and Rayquaza in the hideouts, DEEP COVE and the STAWAMUS CHIEF, built from their battle
  sprites (`atlas/make_legend_sprites.py`; harness `murrelet.txt`, `reef.txt`, `docs/legends.png`).
  Harness command `clearflag`.
- **Battle intros**: the bear's intro is a glowing amber paw print, the reef's a cyan glass-sponge
  lattice, lit by the original palette cycling (`atlas/make_transitions.py`, `docs/intros.png`;
  checked by rendering, not yet seen in a live legendary battle). Rayquaza's intro is abstract
  ring markings and stays.
- **Learnsets**: immobile organisms get body-appropriate openers (ABSORB, ACID for microbes, BUBBLE for
  sponges), GROWTH or HARDEN at level 1, and no charging or body-contact moves (`atlas/lib/moves.js`).
- **ADAMS RIVER salmon run**: surfing meets sockeye spawners, fishing brings up smolts, alevins and
  spawners (`atlas/habitats.json` `run`, `apply_wild.js`); fishers talk about the run.
- **HECATE REEF** cavern holds the reef's real animals: spotted ratfish, lingcod, wolf eel, spot prawn,
  plumose anemone and sunflower sea star (`habitats.json` `residents`).
- **SCOUT** replaces the NINJA BOY trainer class and its lines.
- **Playtest from power-on** (`firstbattle.txt`, replacing `opening.txt`, which had drifted and never
  left the bedroom): clock, rival, RIVER ROAD, starter from the bag, first battle won, lab. It found
  five menu strings that overflowed once {PKMN} became PARTNER (`41_menu_widths`, e.g. "Do what
  with this one?").
- **Rival playtest** (`rival.txt`): from power-on through the lab (answer YES to meeting the rival),
  then a save-and-continue warp to BOUNDARY BAY with REPEL poked on (SaveBlock1 0x13DE); MAY's
  line and battle play (MORELSPORE vs BEAVERKIT, a type disadvantage like Torchic vs Mudkip).
- **Post-game played**: `postgame.txt` (island tickets, `docs/postgame_desk.png`) and
  `survey.txt` (ISLAND CAVE survey note). Harness: `sb1poke`, `reset`, fresh save per run.

**Known issues**
- BATTLE FRONTIER, TRAINER HILL and TV text only had the automatic passes.
- Learnsets are type-based; immobile organisms (plants, fungi, sponges, microbes) now open with
  ABSORB/ACID/BUBBLE and never learn charging or body-contact moves, but some picks are still odd.
- JOHTO's stand-in is "ISLAND". TrailNav town close-ups show the game's own town layouts (fine).

## Next three tasks

1. Fix issues from the owner's playtest reports.
2. Optional: Rayquaza's battle intro as a murrelet; remaining learnset oddities.
3. Optional: more BC tiles (arbutus on OAK BAY's bluffs, a cannery at PRINCE RUPERT).

## Waiting on the owner

- Playtesting is the owner's (2026-10-05): Claude doesn't run long harness playthroughs; it fixes
  reported issues and keeps the short harness scripts working.

- Rename the GitHub repo (Settings > General > Repository name), then run
  `git remote set-url origin https://github.com/AlanWallerDev/<new-name>` locally.

## Earlier session: P1 design lock, P2 roster, P3 place names and BC map (2026-10-05)

**Done**
- **202-entry BC Field Journal** (`docs/ROSTER.md`, generated by `node atlas/roster_doc.js`).
  - `atlas/bc_species.json`: 148 new BC organisms with stats, facts, BC habitat tags and art
    (`atlas/sprites/specs_bc.py`, new `seastar` and `urchin` rigs). Facts were checked; uncertain
    claims were softened.
  - Starters: Skunk Cabbage (seed, shoot, bloom), Morel (spore, mycelium, burn morel), Beaver
    (kit, yearling, adult; the adult is a game-only override of `na-136` with starter-level stats).
  - Legendaries: spirit bear (Groudon), glass sponge reef (Kyogre), marbled murrelet (Rayquaza),
    Vancouver Island marmot (Latias), northern spotted owl (Latios), Marrella / Opabinia / Pikaia
    (Regis, the two Living Atlas fossils overridden to Regi stats), phantom orchid (Jirachi).
    Mythicals: Ogopogo (Deoxys), Sasquatch (Mew), Caddy (Lugia). Fossils: Hallucigenia, Wiwaxia,
    Anomalocaris, Sidneyia.
  - Eleven BC life-stage lines evolve: sockeye (alevin, smolt, spawner), tree frog, western toad,
    rough-skinned newt, Dungeness crab, darner, mourning cloak, plus moon jelly, slime mold,
    tardigrade and the two Living Atlas butterflies/moths.
  - Invasives flagged for the villains to use: barred owl, bullfrog, green crab, Himalayan
    blackberry, Japanese knotweed, Scotch broom (plus starling, house centipede, earthworm,
    death cap from Living Atlas).
- Picker: all `bc_species.json` organisms and `regional_must` claim regional slots first;
  worldwide slots only take organisms with art. Result: 202/202 regional slots are BC.
- Wild areas: rivers now have sturgeon, lamprey, steelhead, sockeye and sticklebacks.
- Trainers: every party (854) uses BC organisms; gyms keep their types; starter lines only in
  rival parties.
- **Place names (P3)**: towns, landmarks and all sea and land routes renamed to the province-wide
  table in `atlas/locations.json` (Squamish, Tofino, Victoria, Hope, Yale, Kamloops, Revelstoke,
  Prince Rupert, Echo Bay; Othello Tunnels, Horne Lake Caves, Wells Gray Cone, Hecate Reef,
  SS Beaver Wreck; Coquihalla, Rogers Pass, Inside Passage…). 40 renames in 94 files, no
  overflowing lines. Build and opening harness pass.

- **BC region map**: TrailNav and Fly map redrawn as BC (`atlas/region_map.json`, drawn by
  `atlas/make_region_map.py`): coast, Vancouver Island, Haida Gwaii, Coast and Rocky Mountains,
  the dry Interior with Okanagan Lake, every town and route at a BC position, and Yukon, Alberta and
  Washington beyond the border. The section grid and positions follow the same file. The device
  reads TRAILNAV and its menu button BC MAP (`atlas/make_trailnav.py`). Screenshot:
  `docs/region_map.png`. New harness command `setflag` and script `trailnav.txt`.

- **Overworld recolour** (`atlas/recolor.json`, `atlas/recolor_tiles.py`): grass, tree and water
  colours swapped in all 290 tileset palettes that use them (seam-free, since tilesets share
  colours). Screenshot: `docs/overworld.png`; harness script `overworld.txt`.

- **Villain teams (P4 start)**: TEAM MAGMA is TEAM CINDER and TEAM AQUA is TEAM RIPTIDE in all
  text, trainer classes, hideouts and the emblem (`atlas/text/04-06`; bare AQUA stays where it is
  the type). Leaders and admins have fictional stand-in names in `atlas/characters.json`:
  ASHBY (Maxie), KENDALL (Tabitha), HOLLIS (Archie), MARINA (Shelly), FINN (Matt). The
  {KYOGRE}/{GROUDON} placeholders follow the species map.

- **Dialogue follows the species map**: `rename_text.js` now tracks organism names too, so all 364
  stale names from the old roster were renamed (the villains wake SPIRITBEAR and SPONGEREEF,
  Wally's partner is the new slot organism). Names that contain a renamed word (SS BEAVER WRECK,
  GALLOPING GOOSE) are shielded. Generated files (species names, Journal text) are excluded.
- **Villain motives**: stand-in lines in `atlas/text/07_motives.tsv`: CINDER wants the old
  forests to burn so they renew; RIPTIDE wants the sea to take back the land. Owner to approve.

- **Conifers**: `atlas/conifer_tiles.py` re-shades the 40 tiles of the tree and its forest variants
  into tiered conifers and points the standalone tops; works on shared tiles, so all variants stay
  consistent (`docs/overworld.png`). In stacked columns the lower tree's point is drawn in front of
  the trunk above (top-layer tip tiles 204/205), so nearer trees overlap farther ones.
- TRAINER stays as the word for trainers in dialogue (owner decision); NATURALIST is not used
  for new text.

- **Text pass**: HOENN leftovers gone; DEVON is the fictional SUMMIT company (SUMMIT GOODS,
  SUMMIT SCOPE); STEVEN is DAWSON and MR. STONE is MR. DAWSON. Stand-in tables for owner review:
  `09_signs.tsv` (BC town mottos), `10-11_observatory.tsv` (PRINCE RUPERT's space center is a
  weather OBSERVATORY launching weather balloons; CINDER steals its hydrogen),
  `12_geography.tsv` (S.S. BEAVER wreck, DEEP COVE in a fjord, WHISTLER up the SEA TO SKY).

- **Post-game islands**: after the credits, the VANCOUVER harbour desk gives the four island
  tickets once (stand-in line, `data/maps/LilycoveCity_Harbor/scripts.inc`), opening the islands of
  Sasquatch, Caddy, Ogopogo and the roaming pair. Played through: `atlas/test/scripts/postgame.txt`
  marks the game cleared, saves with a continue warp into the harbour, resets and talks to the
  desk; all four key items arrive, then the upstream Old Sea Map scene follows.
- **Text pass, continued** (`13_text_fixes.tsv`): last upstream species names (whale watching in
  PRINCE RUPERT, Battle Pike, Mountain View), PRESIDENT DAWSON, TOFINO as a surf town, HOPE's
  founding, the granite STAWAMUS CHIEF; the braille puzzle follows the species map.

- **Survey notes**: the Regi chambers (sealed chamber, desert ruins, island cave, ancient tomb)
  show [Stand-in] Burgess Shale survey notes as normal text instead of braille, with the same
  puzzle hints (`data/text/braille.inc`, `_Note` labels; braille alphabet panels stay as
  decoration). Played: `survey.txt` reads the ISLAND CAVE note, which shows, waits and closes.
- **Harness**: `sb1poke PTR OFF VAL` writes a byte through a save-block pointer (`@gSaveBlock1Ptr`,
  `@gSaveBlock2Ptr`), `reset` restarts the console; each run starts with a fresh battery save.
  Setting `continueGameWarp` (SaveBlock1 0x0C) and `specialSaveWarpFlags` bit 0 (SaveBlock2 0x09)
  before saving puts the player anywhere on CONTINUE.

**Known issues**
- Dialogue still tells Hoenn's story with BC names (P4), so some lines read oddly (e.g. HOPE's
  founding). Pinned for the story: Wally's catch is a STELLER'S JAY (Ralts slot) and NORMAN lends a
  RACCOON (Zigzagoon slot), in `atlas/picks.json`.
- Learnsets are type-based, so a few organisms get odd moves (Morel Spore knows Tackle).
- The title screen still shows Rayquaza. Town zoom maps in the TrailNav are still Hoenn town layouts.
- Elk, deer and caribou use the goat rig; sea lions and otters the seal rig (stand-ins).
- Region names unchanged: KANTO is "INTERIOR" in one line; JOHTO's stand-in is "ISLAND", which
  can't be renamed by word without hitting island place names.
