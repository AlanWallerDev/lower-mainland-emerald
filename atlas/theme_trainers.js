#!/usr/bin/env node
// Every trainer uses BC organisms, and gym leaders, gym trainers (with their rematches), the Elite
// Four and the Champion use organisms of their gym's type. A party member in a worldwide slot, or
// lacking the theme type, is swapped for the closest BC organism (shared type, then stat total);
// custom moves are refilled from the new learnset. Starter lines and legendaries are never swapped in.
//
// Idempotent. Run after atlas/apply_species.js: node atlas/theme_trainers.js
'use strict';
const C = require('./lib/common');

const THEMES = {
	RustboroCity_Gym: 'Stone', DewfordTown_Gym: 'Brawn', MauvilleCity_Gym: 'Charm', LavaridgeTown_Gym_1F: 'Ember',
	LavaridgeTown_Gym_B1F: 'Ember', PetalburgCity_Gym: 'Common', FortreeCity_Gym: 'Sky', MossdeepCity_Gym: 'Mind',
	SootopolisCity_Gym_1F: 'Aqua', SootopolisCity_Gym_B1F: 'Aqua', EverGrandeCity_SidneysRoom: 'Toxin',
	EverGrandeCity_PhoebesRoom: 'Night', EverGrandeCity_GlaciasRoom: 'Frost', EverGrandeCity_DrakesRoom: 'Sky',
	EverGrandeCity_ChampionsRoom: 'Aqua',
};

const map = C.readJSON('atlas/species_map.json');
const orgs = C.loadOrganisms();
const slotOrg = Object.fromEntries(map.map((e) => [e.slot, orgs[e.id]]));
const regional = new Set(C.hoennOrder());

// Level-up learnsets as written by apply_species.js.
const ptrs = C.read('src/data/pokemon/level_up_learnset_pointers.h');
const lu = C.read('src/data/pokemon/level_up_learnsets.h');
function movesAt(slot, level) {
	const arr = ptrs.match(new RegExp(`\\[SPECIES_${slot}\\] = (\\w+)`))[1];
	const body = lu.match(new RegExp(`${arr}\\[\\] = \\{([\\s\\S]*?)LEVEL_UP_END`))[1];
	const known = [...body.matchAll(/LEVEL_UP_MOVE\(\s*(\d+), MOVE_(\w+)\)/g)].filter((m) => +m[1] <= level).map((m) => m[2]);
	const last = [...new Set(known.reverse())].slice(0, 4).reverse();
	while (last.length < 4) last.push('NONE');
	return last;
}

// Trainers of each theme: those battled in the map's scripts, plus their rematch variants.
const trainersH = C.read('src/data/trainers.h');
const themed = {};
for (const [mapDir, type] of Object.entries(THEMES)) {
	const scripts = C.read(`data/maps/${mapDir}/scripts.inc`);
	for (const m of scripts.matchAll(/trainerbattle\w* (TRAINER_\w+)/g)) {
		const base = m[1].replace(/_1$/, '');
		for (const t of [m[1], ...[2, 3, 4, 5].map((n) => `${base}_${n}`)]) {
			if (trainersH.includes(`[${t}] =`)) themed[t] = type;
		}
	}
}

// Slots no trainer swaps in: the player's starter lines and the legendaries.
const picks = C.readJSON('atlas/picks.json');
const NO_SWAP_IN = new Set([...(picks.legend_slots || []), 'TREECKO', 'GROVYLE', 'SCEPTILE', 'TORCHIC', 'COMBUSKEN',
	'BLAZIKEN', 'MUDKIP', 'MARSHTOMP', 'SWAMPERT']);

let parties = C.read('src/data/trainer_parties.h');
let swaps = 0;
const trainers = [...trainersH.matchAll(/\[(TRAINER_\w+)\] =[\s\S]*?\.party = \w+\((sParty_\w+)\)/g)];
const done = new Set();
for (const [, trainer, party] of trainers) {
	if (done.has(party)) continue;
	done.add(party);
	const type = themed[trainer];
	const re = new RegExp(`(static const struct \\w+ ${party}\\[\\] = \\{)([\\s\\S]*?)(\\n\\};)`);
	const pm = parties.match(re);
	if (!pm) continue;
	const used = new Set([...pm[2].matchAll(/SPECIES_(\w+)/g)].map((m) => m[1]));
	const body = pm[2].replace(/\{([^{}]*?\.species = SPECIES_(\w+)[^{}]*?(?:\{[^{}]*\}[^{}]*?)?)\}/g, (whole, inner, slot) => {
		const org = slotOrg[slot];
		if (!org) return whole;
		// Gym and League trainers need their type; everyone uses BC (regional) organisms.
		const offType = type && !org.types.includes(type);
		const starterOut = NO_SWAP_IN.has(slot) && !/May|Brendan|Wally/.test(party); // rivals keep their starters
		if (!offType && !starterOut && regional.has(slot)) return whole;
		const want = type ? [type] : org.types;
		const cands = map.filter((e) => regional.has(e.slot) && !NO_SWAP_IN.has(e.slot) && !used.has(e.slot)
			&& orgs[e.id].types.some((t) => want.includes(t)))
			.sort((a, b) => (orgs[a.id].types[0] === want[0] ? 0 : 50) - (orgs[b.id].types[0] === want[0] ? 0 : 50)
				+ Math.abs(orgs[a.id].bst - org.bst) - Math.abs(orgs[b.id].bst - org.bst));
		if (!cands.length) return whole;
		const pick = cands[0].slot;
		used.add(pick);
		swaps++;
		let out = whole.replace(`SPECIES_${slot}`, `SPECIES_${pick}`);
		const lvl = +(inner.match(/\.lvl = (\d+)/) || [0, 50])[1];
		out = out.replace(/\.moves = \{[^}]*\}/, `.moves = {${movesAt(pick, lvl).map((m) => 'MOVE_' + m).join(', ')}}`);
		return out;
	});
	parties = parties.replace(re, pm[1] + body + pm[3]);
}
C.write('src/data/trainer_parties.h', parties);
console.log(`theme_trainers: ${done.size} parties (${Object.keys(themed).length} themed), ${swaps} party members swapped`);
