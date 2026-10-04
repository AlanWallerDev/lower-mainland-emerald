// Shared helpers for the atlas pipeline: paths, file IO, organism data and slot tables.
'use strict';
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..', '..');
const P = (...a) => path.join(ROOT, ...a);

const read = (p) => fs.readFileSync(P(p), 'utf8');
const write = (p, s) => fs.writeFileSync(P(p), s);
const readJSON = (p) => JSON.parse(read(p));
const writeJSON = (p, v) => write(p, JSON.stringify(v, null, '\t') + '\n');
const exists = (p) => fs.existsSync(P(p));

/** A file as it is in upstream pret/pokeemerald (needs the `upstream` remote). */
function upstream(p) {
	return execFileSync('git', ['show', 'upstream/master:' + p], { cwd: ROOT, encoding: 'utf8', maxBuffer: 64 << 20 });
}

const LA_TO_GEN3 = {
	Common: 'NORMAL', Brawn: 'FIGHTING', Sky: 'FLYING', Toxin: 'POISON', Soil: 'GROUND',
	Stone: 'ROCK', Chitin: 'BUG', Armor: 'STEEL', Ember: 'FIRE', Aqua: 'WATER',
	Verdant: 'GRASS', Charm: 'ELECTRIC', Mind: 'PSYCHIC', Frost: 'ICE', Night: 'DARK',
};
const GEN3_TO_LA = Object.fromEntries(Object.entries(LA_TO_GEN3).map(([k, v]) => [v, k]));

/**
 * All organisms by id: the Living Atlas database (LIVING_ATLAS_DIR, default ../living-atlas,
 * falling back to atlas/data/species.json) plus the hack's own atlas/bc_species.json.
 */
function loadOrganisms() {
	const la = process.env.LIVING_ATLAS_DIR || path.join(ROOT, '..', 'living-atlas');
	const laFile = path.join(la, 'game', 'data', 'species.json');
	const src = fs.existsSync(laFile) ? laFile : P('atlas', 'data', 'species.json');
	let list = JSON.parse(fs.readFileSync(src, 'utf8'));
	list = list.species || list;
	if (exists('atlas/bc_species.json')) {
		const bc = readJSON('atlas/bc_species.json');
		list = list.concat(bc.species || bc);
	}
	return Object.fromEntries(list.map((s) => [s.id, s]));
}

/** Species slot names in constant order: [{slot, id}] where id is the SPECIES_ number. */
function speciesSlots() {
	const out = [];
	for (const m of read('include/constants/species.h').matchAll(/#define SPECIES_(\w+) (\d+)/g)) {
		const id = +m[2];
		if (m[1] === 'NONE' || m[1] === 'EGG' || m[1].startsWith('OLD_UNOWN') || m[1].startsWith('UNOWN_')) continue;
		if (id < 1 || id >= 412 || out.some((o) => o.id === id)) continue;
		out.push({ slot: m[1], id });
	}
	return out;
}

/** National dex constant names in order, so index + 1 is the national number. */
function nationalOrder() {
	const src = read('include/constants/pokedex.h');
	const body = src.slice(src.indexOf('NATIONAL_DEX_NONE'), src.indexOf('};', src.indexOf('NATIONAL_DEX_NONE')));
	return [...body.matchAll(/NATIONAL_DEX_(\w+)/g)].map((m) => m[1]).filter((n) => n !== 'NONE' && !n.startsWith('OLD_UNOWN')).slice(0, 386);
}

/** Hoenn dex constant names in order (TREECKO first, 202 entries). */
function hoennOrder() {
	const src = read('include/constants/pokedex.h');
	const start = src.indexOf('HOENN_DEX_NONE');
	const body = src.slice(start, src.indexOf('};', start));
	return [...body.matchAll(/HOENN_DEX_(\w+)/g)].map((m) => m[1]).filter((n) => n !== 'NONE').slice(0, 202);
}

/** In-game name for an organism: atlas/names.json, else its name squeezed to 10 characters. */
function gameName(org, names) {
	if (names[org.id]) return names[org.id];
	const upper = require('./text').sanitize(org.name).toUpperCase().replace(/[^A-Z0-9 .'’-]/g, '');
	return upper.length <= 10 ? upper : upper.replace(/\s+/g, '').slice(0, 10);
}

/** Replace the body of a `[KEY] = ...` C initializer list entry. */
function replaceBlock(src, startRe, endStr, replacement) {
	const m = src.match(startRe);
	if (!m) throw new Error('block not found: ' + startRe);
	const end = src.indexOf(endStr, m.index);
	return src.slice(0, m.index) + replacement + src.slice(end + endStr.length);
}

module.exports = {
	ROOT, P, read, write, readJSON, writeJSON, exists, upstream,
	LA_TO_GEN3, GEN3_TO_LA, loadOrganisms, speciesSlots, nationalOrder, hoennOrder, gameName, replaceBlock,
};
