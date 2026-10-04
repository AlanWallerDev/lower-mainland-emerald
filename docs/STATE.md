# State

Updated at the end of every session. Read this first, then `docs/TASKS.md` and `docs/BC_PLAN.md`.

## Last session: P0, pipeline rewrite (2026-10-04)

**Done**
- Plan approved and logged (see `docs/BC_PLAN.md` and Living Atlas `docs/DECISIONS.md`); title
  is **Pokémon BC** (title screen and credits); Indigenous content limited to common place names.
- **Pipeline rewritten** (the original Node scripts were never committed and are lost).
  `atlas/build.sh` runs end to end, every step is idempotent (a second run changes nothing), and
  the ROM builds and passes the opening harness script.
  - `apply_species.js` + `lib/moves.js`: reproduces the old output exactly for stats, types,
    names, Field Journal entries and evolutions. New rules for abilities (keywords in the Living
    Atlas ability names, then type defaults; legend slots keep upstream abilities), gender, egg
    groups, learnsets (moves of the organism's types in rising power, filtered by body plan:
    no fangs on plants, no punches on birds) and TM/HM/tutor compatibility (HMs by body and
    habitat).
  - `body_colors.py`: Journal colour search from each sprite (the old values were mostly the
    slot's upstream colour).
  - `pick_species.js`: rewritten for the approved design (202 regional slots BC-only). It
    reports today's gap and refuses `--write` until the BC species exist.
  - `theme_trainers.js`: no-op on the current tree (already themed); checked against upstream
    parties (swaps 72 off-type members).
  - `apply_wild.js` + `habitats.json`: habitat table per area, keyword scoring, freshwater /
    sea / deep-sea separation.
  - `rename_text.js` + `lib/replace.js`: edits to `locations.json`, the new `characters.json` or
    new tables in `atlas/text/` are applied once to all game text (tested: SURREY to HOPE
    renamed in 17 files, signs included, then reverted). The two existing phrase tables reapply
    as a no-op.
- `__pycache__` untracked; `.gitignore` keeps `atlas/**/*.js`.

**Gameplay changes from the regeneration**
- Abilities, learnsets, TM/HM/tutor compatibility, egg groups and some gender ratios changed
  for every organism (the old rules were unknown). Wild tables were re-rolled by habitat.
- DELIBIRD slot's organism is now named SNOWMAKER (was BACTERIUM).
- Two over-long Journal entries now end with "…" instead of "....".

**Known issues**
- Freshwater areas borrow non-fish (newts, water bugs, jellies) until BC fish exist.
- The title screen still shows the Rayquaza silhouette (to become the Marbled Murrelet).
- The regional pool still holds worldwide organisms in 129 of 202 slots (P2 fixes this).
- README "Known gaps" still apply.

## Next three tasks

1. P1 design lock: final place table (`atlas/locations.json`) and the 202-entry BC roster list.
2. P2 roster: `atlas/bc_species.json` (with `bc_habitats` tags for `apply_wild.js`), then
   `node atlas/pick_species.js --write`.
3. P3 place renames through `rename_text.js`.

## Waiting on the owner

- Rename the GitHub repo (Settings > General > Repository name), then run
  `git remote set-url origin https://github.com/AlanWallerDev/<new-name>` locally.
