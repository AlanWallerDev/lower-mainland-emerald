# State

Updated at the end of every session. Read this first, then `docs/TASKS.md` and `docs/BC_PLAN.md`.

## Last session: P0, province-wide plan and title (2026-10-04)

**Done**
- `docs/BC_PLAN.md`: plan to take the hack province-wide. Owner approved it (decisions are
  logged in Living Atlas `docs/DECISIONS.md`): Hoenn's map graph reassigned to BC regions,
  202-entry all-BC Field Journal, starters Skunk Cabbage / Morel / American Beaver, villains
  CINDER and RIPTIDE, very rare organisms as legendaries, cryptids (Sasquatch, Caddy,
  Ogopogo) as mythicals, public repo is fine, "Lower Mainland Emerald" title dropped.
- Verified in a Linux cloud container: `make tools && make modern` builds
  `pokeemerald_modern.gba`, and `atlas/test/run.sh atlas/test/scripts/opening.txt` runs
  (needs `gcc-arm-none-eabi`, `libpng-dev`, `libmgba-dev`, Pillow).
- `.gitignore` now keeps `atlas/**/*.js` (upstream ignores every `*.js`).
- Title is **Pokémon BC**: `atlas/make_title.py` restores the original wordmark and draws a
  "BC" banner in place of "EMERALD VERSION". Screenshot: `docs/title.png`. New harness
  script `atlas/test/scripts/title.txt`. The script needs the `upstream` remote
  (`git remote add upstream https://github.com/pret/pokeemerald && git fetch --depth 1 upstream master`).
- Indigenous content decided: common place names only.

**Known issues**
- **The Node pipeline scripts are missing from the repo** (`pick_species.js`,
  `apply_species.js`, `lib/moves.js`, `lib/text.js`, `theme_trainers.js`, `apply_wild.js`,
  `apply_locations.js`, `apply_text.js`, `polish_text.js`, `npc_names.js`, `region_text.js`,
  `apply_type_text.js`). They were never committed because of the `*.js` ignore rule, so
  `atlas/build.sh` can't run. The committed generated sources still build.
- The title screen still shows the Rayquaza silhouette (to become the Marbled Murrelet).
- README "Known gaps" from before still apply.

## Next three tasks

1. Recover the Node pipeline scripts (owner pushes them from a local copy) or rewrite them.
2. P1 design lock: final place table and the 202-entry BC roster list.
3. P2 roster: `atlas/bc_species.json` and the BC-only regional picker.

## Waiting on the owner

- Do you have the `atlas/*.js` and `atlas/lib/*.js` files locally? If so:
  `git pull`, then `git add atlas/*.js atlas/lib/*.js`, commit and push.
- Optional: rename the GitHub repo to match the title (GitHub settings; I can't do it from here).
