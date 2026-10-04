#!/usr/bin/env node
// Gym leaders, gym trainers (with their rematches), the Elite Four and the Champion use organisms
// of their gym's type. A party member whose organism lacks the type is swapped for the closest
// organism (by stat total) that has it; custom moves are refilled from the new learnset.
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

let parties = C.read('src/data/trainer_parties.h');
let swaps = 0;
for (const [trainer, type] of Object.entries(themed)) {
	const block = trainersH.match(new RegExp(`\\[${trainer}\\] =[\\s\\S]*?\\.party = \\w+\\((sParty_\\w+)\\)`));
	if (!block) continue;
	const party = block[1];
	const re = new RegExp(`(static const struct \\w+ ${party}\\[\\] = \\{)([\\s\\S]*?)(\\n\\};)`);
	const pm = parties.match(re);
	if (!pm) continue;
	const used = new Set([...pm[2].matchAll(/SPECIES_(\w+)/g)].map((m) => m[1]));
	const body = pm[2].replace(/\{([^{}]*?\.species = SPECIES_(\w+)[^{}]*?(?:\{[^{}]*\}[^{}]*?)?)\}/g, (whole, inner, slot) => {
		const org = slotOrg[slot];
		if (!org || org.types.includes(type)) return whole;
		// Closest stat total among organisms with the theme type; regional (BC) slots first.
		const cands = map.filter((e) => orgs[e.id].types.includes(type) && !used.has(e.slot))
			.sort((a, b) => (regional.has(b.slot) - regional.has(a.slot)) * 1000
				+ (orgs[a.id].types[0] === type ? 0 : 50) - (orgs[b.id].types[0] === type ? 0 : 50)
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
console.log(`theme_trainers: ${Object.keys(themed).length} trainers, ${swaps} party members swapped`);
