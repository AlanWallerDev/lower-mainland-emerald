#!/usr/bin/env node
// Chooses an organism for each of the 386 species slots and writes atlas/species_map.json.
//
// - The 202 Hoenn (regional) slots take BC organisms only: `bc_native` ids in atlas/picks.json
//   plus everything in atlas/bc_species.json. The other 184 slots take worldwide organisms.
// - `forced` slots are fixed first (starters, legendaries, fossils).
// - Life-stage lines go into upstream evolution chains of the same length where possible.
// - Everything else is matched by type and stat total against the slot's upstream values.
//
// Usage: node atlas/pick_species.js          report only
//        node atlas/pick_species.js --write  write atlas/species_map.json
'use strict';
const C = require('./lib/common');

const WRITE = process.argv.includes('--write');
const picks = C.readJSON('atlas/picks.json');
const orgs = C.loadOrganisms();
const exclude = new Set(picks.exclude || []);
const fossilSlots = new Set(picks.fossil_slots || []);

// ---- slots: upstream types, stat totals and evolution chains -------------------------

const upInfo = C.upstream('src/data/pokemon/species_info.h');
const slotInfo = {};
for (const m of upInfo.matchAll(/\[SPECIES_(\w+)\] =\s*\{([^[]*?)\n    \}/g)) {
	const get = (k) => +(m[2].match(new RegExp(`\\.${k}\\s*=\\s*(\\d+)`)) || [0, 0])[1];
	const types = [...m[2].matchAll(/TYPE_(\w+)/g)].map((t) => t[1]);
	slotInfo[m[1]] = { types, bst: ['baseHP', 'baseAttack', 'baseDefense', 'baseSpeed', 'baseSpAttack', 'baseSpDefense'].reduce((a, k) => a + get(k), 0) };
}
const slots = C.speciesSlots().map((s) => s.slot);
const national = C.nationalOrder();
const regional = new Set(C.hoennOrder());

const next = {};
for (const m of C.upstream('src/data/pokemon/evolution.h').matchAll(/\[SPECIES_(\w+)\]\s*=\s*\{\{EVO_\w+, \w+, SPECIES_(\w+)\}/g)) {
	if (!next[m[1]]) next[m[1]] = m[2];
}
const hasPrev = new Set(Object.values(next));
const chains = slots.filter((s) => !hasPrev.has(s) && next[s]).map((s) => {
	const c = [s];
	while (next[c[c.length - 1]] && c.length < 3) c.push(next[c[c.length - 1]]);
	return c;
});

// ---- organism pools --------------------------------------------------------------

const bcIds = new Set(picks.bc_native || []);
if (C.exists('atlas/bc_species.json')) for (const s of C.readJSON('atlas/bc_species.json').species || C.readJSON('atlas/bc_species.json')) bcIds.add(s.id);
// Organisms with stand-in art (atlas/sprites/specs_*.py); a worldwide organism needs art to be picked.
const fs = require('fs');
const hasArt = new Set();
for (const f of fs.readdirSync(C.P('atlas', 'sprites')).filter((x) => /^specs_.*\.py$/.test(x))) {
	for (const m of fs.readFileSync(C.P('atlas', 'sprites', f), 'utf8').matchAll(/^\s*'([a-z]{2}-\d{3})':/gm)) hasArt.add(m[1]);
}
const usable = Object.values(orgs).filter((o) => !exclude.has(o.id) && !o.id.startsWith('fo-') && (bcIds.has(o.id) || hasArt.has(o.id)));
const isBC = (o) => bcIds.has(o.id);

const assign = {}; // slot -> id
const used = new Set();
for (const [slot, id] of Object.entries(picks.forced || {})) {
	if (!orgs[id]) throw new Error(`forced ${slot}: unknown organism ${id}`);
	assign[slot] = id;
	used.add(id);
}

const G3 = C.LA_TO_GEN3;
function cost(o, slot) {
	const si = slotInfo[slot];
	const ot = o.types.map((t) => G3[t]);
	const typeCost = ot[0] === si.types[0] ? 0 : ot.some((t) => si.types.includes(t)) ? 0.5 : 1;
	return typeCost * 60 + Math.abs(o.bst - si.bst);
}

const stageOrder = (a, b) => (a.stage_index || 0) - (b.stage_index || 0) || a.id.localeCompare(b.id);
const loose = []; // line members that found no chain of their length: placed as singles

// Life-stage lines first, as units, into chains of the same length in the right region.
const lines = {};
for (const o of usable) if (o.line && !used.has(o.id)) (lines[o.line] = lines[o.line] || []).push(o);
for (const members of Object.values(lines).sort((a, b) => b.length - a.length)) {
	members.sort(stageOrder);
	const bc = members.every(isBC);
	const fits = chains.filter((c) => c.length === members.length && c.every((s) => !assign[s] && !fossilSlots.has(s)
		&& regional.has(s) === bc));
	if (!fits.length) {
		loose.push(...members);
		continue;
	}
	fits.sort((a, b) => a.reduce((t, s, i) => t + cost(members[i], s), 0) - b.reduce((t, s, i) => t + cost(members[i], s), 0));
	fits[0].forEach((s, i) => { assign[s] = members[i].id; used.add(members[i].id); });
}

/** Cheapest pairs first among `orgList`, into free slots that `slotOk` allows. */
function fill(orgList, slotOk, extra = () => 0) {
	const pairs = [];
	for (const slot of slots) {
		if (assign[slot] || fossilSlots.has(slot) || !slotOk(slot)) continue;
		for (const o of orgList) if (!used.has(o.id)) pairs.push([cost(o, slot) + extra(o, slot), slot, o.id]);
	}
	pairs.sort((a, b) => a[0] - b[0]);
	for (const [, slot, id] of pairs) {
		if (assign[slot] || used.has(id)) continue;
		assign[slot] = id;
		used.add(id);
	}
}

// Must-have BC organisms (everything in bc_species.json plus `regional_must`) claim regional slots
// next, then the remaining BC organisms fill what is left of the region, and worldwide organisms
// fill the national slots.
const must = new Set(picks.regional_must || []);
if (C.exists('atlas/bc_species.json')) for (const s of C.readJSON('atlas/bc_species.json').species) if (!s.override) must.add(s.id);
const singles = usable.filter((o) => !o.line).concat(loose);
fill(singles.filter((o) => must.has(o.id) || loose.includes(o) && isBC(o)), (s) => regional.has(s));
fill(singles.filter(isBC), (s) => regional.has(s));
fill(singles.filter((o) => !isBC(o)).concat(loose.filter((o) => !isBC(o))), (s) => !regional.has(s));
fill(singles.filter(isBC), (s) => !regional.has(s));

// ---- report and write --------------------------------------------------------------

const empty = slots.filter((s) => !assign[s]);
const regionalBC = [...regional].filter((s) => assign[s] && isBC(orgs[assign[s]])).length;
console.log(`pick_species: ${slots.length - empty.length}/${slots.length} slots filled, ${regionalBC}/${regional.size} regional slots hold BC organisms`);
if (empty.length) console.log('  empty: ' + empty.join(' '));

if (WRITE) {
	if (empty.length) throw new Error('not writing: some slots are empty (add BC species to atlas/bc_species.json)');
	const out = slots.map((slot) => {
		const o = orgs[assign[slot]];
		return {
			dex: national.indexOf(slot) + 1, slot, id: o.id, name: o.name, types: o.types, bst: o.bst,
			slot_types: [slotInfo[slot].types[0], slotInfo[slot].types[1] || slotInfo[slot].types[0]], slot_bst: slotInfo[slot].bst,
			local: isBC(o) ? 100 : 10,
		};
	}).sort((a, b) => a.dex - b.dex);
	C.writeJSON('atlas/species_map.json', out);
	console.log('  wrote atlas/species_map.json');
}
