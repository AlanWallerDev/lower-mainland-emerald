# Pokémon BC: notes for Claude

A Pokémon Emerald decomp hack set in British Columbia, using Living Atlas organisms. Claude
builds; the owner directs. Owner decisions are logged in the Living Atlas repo's
`docs/DECISIONS.md`.

## Session loop

1. Read `docs/STATE.md`, `docs/TASKS.md` and `docs/BC_PLAN.md`.
2. Take the next unchecked task (or the one the owner names).
3. Regenerate and build with `sh atlas/build.sh` (or just `make modern -j8`); check visible changes with
   `atlas/test/run.sh atlas/test/scripts/<script>.txt` and look at the PNGs in `build/test/`.
4. Update `docs/STATE.md` and tick `docs/TASKS.md`; commit and push.

## Rules

- Never commit ROMs.
- No Pokémon terms in game text (organisms, partners, FIELD JOURNAL, NATURALIST, NATURE LEAGUE).
- Story text is the owner's call; new lines are stand-ins until approved.
- Villains stay fictional. Historical figures: deceased, heroic or neutral roles only.
- Indigenous content: common place names only; no sacred figures, crests, art or stories. Cryptids use their common English names only.
- C changes are marked with a `Living Atlas` comment.
- Generated sources come from `atlas/build.sh`; change `atlas/` data and rebuild, not the generated files. Text changes go through `atlas/rename_text.js` (names in `locations.json` / `characters.json`, phrase tables in `atlas/text/`).
