#!/usr/bin/env node
// Refills every wild area by habitat (atlas/habitats.json). Each area keeps upstream's levels and
// rarity pattern: each distinct upstream species becomes one organism suited to the habitat.
// Organisms with `bc_habitats` (atlas/bc_species.json) are placed by those tags; others are scored
// by keywords in their range and entry, plus a type bonus.
//
// Idempotent. Run: node atlas/apply_wild.js
'use strict';
const C = require('./lib/common');
const { hash } = require('./lib/moves');

const cfg = C.readJSON('atlas/habitats.json');
const map = C.readJSON('atlas/species_map.json');
const orgs = C.loadOrganisms();
const picks = C.readJSON('atlas/picks.json');
const regional = new Set(C.hoennOrder());

// Slots that never appear in the wild: legendaries, fossils and starter lines.
const NOT_WILD = new Set([...(picks.legend_slots || []), ...(picks.fossil_slots || []),
	'TREECKO', 'GROVYLE', 'SCEPTILE', 'TORCHIC', 'COMBUSKEN', 'BLAZIKEN', 'MUDKIP', 'MARSHTOMP', 'SWAMPERT']);
const habitatRe = Object.fromEntries(Object.entries(cfg.habitats).map(([k, v]) => [k, new RegExp(v, 'i')]));

function areaFor(label) {
	if (cfg.areas[label]) return cfg.areas[label];
	const hit = Object.keys(cfg.areas).filter((k) => k.endsWith('*') && label.startsWith(k.slice(0, -1)))
		.sort((a, b) => b.length - a.length)[0];
	return hit ? cfg.areas[hit] : null;
}

/** How well an organism suits a habitat for a kind of encounter (land, water, fish, rock); -1 = never. */
function score(org, habitat, kind, level = 0) {
	const strict = level < 2;
	const h = org.habitat;
	if (kind === 'land' && h === 'aquatic') return -1;
	if ((kind === 'water' || kind === 'fish') && h !== 'aquatic' && h !== 'amphibious') return -1;
	if (kind === 'fish' && org.family !== 'swimmer' && level === 0) return -1;
	if (org.bc_habitats) return org.bc_habitats.includes(habitat) ? 10 : -1;
	const text = `${org.range || ''} ${org.entry || ''} ${org.category || ''}`;
	// Water organisms keep to their water: deep-sea life only in the deep, sea life out of rivers.
	if (h === 'aquatic' || h === 'amphibious') {
		const deep = org.id.startsWith('ds-') || habitatRe.deep.test(text);
		const fresh = habitatRe.fresh.test(text);
		const marine = habitatRe.sea.test(text);
		if (deep !== (habitat === 'deep')) return -1;
		if (strict && habitat === 'fresh' && (!fresh || (marine && h === 'aquatic' && org.family !== 'swimmer' && !/fresh|river|lake/i.test(text)))) return -1;
		if (strict && habitat === 'fresh' && /ocean|marine|whale|shark/i.test(org.name + ' ' + (org.range || ''))) return -1;
		if (habitat === 'sea' && fresh && !marine) return -1;
	}
	let s = habitatRe[habitat].test(text) ? 4 : 0;
	s += (cfg.type_bonus[habitat] || []).filter((t) => org.types.includes(t)).length * 2;
	if (h === 'microscope') s -= 2; // microbes are uncommon finds in the grass
	return s;
}

const wild = C.readJSON('src/data/wild_encounters.json');
const up = JSON.parse(C.upstream('src/data/wild_encounters.json'));
const upByLabel = {};
for (const g of up.wild_encounter_groups) for (const e of g.encounters) upByLabel[e.base_label] = e;

const KIND = { land_mons: 'land', water_mons: 'water', fishing_mons: 'fish', rock_smash_mons: 'rock' };
const uses = {};
let areas = 0;
for (const g of wild.wild_encounter_groups) {
	for (const e of g.encounters) {
		const area = areaFor(e.base_label);
		const upE = upByLabel[e.base_label];
		if (!area || !upE) continue;
		areas++;
		const pool = map.filter((m) => !NOT_WILD.has(m.slot) && (area.pool === 'national' ? !regional.has(m.slot) : regional.has(m.slot)));
		for (const [field, kind] of Object.entries(KIND)) {
			if (!e[field] || !upE[field]) continue;
			const habitat = kind === 'land' ? area.land : kind === 'rock' ? area.rock || 'rock' : area.water;
			if (!habitat) continue;
			const upMons = upE[field].mons;
			const distinct = [...new Set(upMons.map((m) => m.species))];
			// Best-suited organisms, spreading use across areas; stable per area.
			let scored = pool.map((m) => ({ m, s: score(orgs[m.id], habitat, kind) })).filter((x) => x.s >= 0);
			// Too few freshwater organisms: borrow from the relaxed rules rather than leave it empty.
			for (let level = 1; level <= 2 && scored.length < distinct.length; level++) {
				scored = pool.map((m) => ({ m, s: score(orgs[m.id], habitat, kind, level) })).filter((x) => x.s >= 0);
			}
			const ranked = scored
				.map((x) => ({ ...x, r: x.s - (uses[x.m.slot] || 0) * 1.5 + (hash(e.base_label + x.m.slot) % 100) / 100 }))
				.sort((a, b) => b.r - a.r);
			if (!ranked.length) continue;
			const chosen = distinct.map((_, i) => ranked[i % ranked.length].m.slot);
			chosen.forEach((s) => (uses[s] = (uses[s] || 0) + 1));
			const sub = Object.fromEntries(distinct.map((sp, i) => [sp, 'SPECIES_' + chosen[i]]));
			e[field].mons = upMons.map((m) => ({ ...m, species: sub[m.species] }));
		}
	}
}
C.write('src/data/wild_encounters.json', JSON.stringify(wild, null, 2) + '\n');
const regionalWild = new Set(Object.keys(uses).filter((s) => regional.has(s)));
console.log(`apply_wild: ${areas} areas, ${Object.keys(uses).length} organisms in the wild (${regionalWild.size} regional)`);
