#!/usr/bin/env node
// Keeps game text in step with the hack's name lists and text tables. Every change is applied
// exactly once, and atlas/text/applied.json records what the text already contains:
//
// 1. Names: atlas/locations.json (towns, places, routes, regions) and atlas/characters.json.
//    When a value differs from the one recorded in applied.json, the old name is renamed to the
//    new one in all game text (whole words only).
// 2. Tables: each atlas/text/*.tsv not yet listed in applied.json is applied once, in file-name
//    order. Rows are `from<TAB>to[<TAB>label]`; phrases match across line breaks and overflowing
//    lines are re-wrapped. A table whose first line is `# mode: words` matches whole words only.
//
// Usage: node atlas/rename_text.js [--dry-run]
'use strict';
const fs = require('fs');
const path = require('path');
const C = require('./lib/common');
const R = require('./lib/replace');

const DRY = process.argv.includes('--dry-run');
const STATE = 'atlas/text/applied.json';

function currentNames() {
	const out = {};
	const loc = C.readJSON('atlas/locations.json');
	for (const sec of ['towns', 'places', 'routes', 'regions']) {
		for (const [k, v] of Object.entries(loc[sec] || {})) out[`${sec}.${k}`] = v;
	}
	for (const [k, v] of Object.entries(C.readJSON('atlas/characters.json').characters)) out[`characters.${k}`] = v;
	return out;
}

const names = currentNames();
const state = C.exists(STATE) ? C.readJSON(STATE) : null;
if (!state) {
	// First run: the committed text already holds every current name and the two original tables.
	C.writeJSON(STATE, { tables: ['01_polish.tsv', '02_type_text.tsv'], names });
	console.log('rename_text: recorded the current text as the baseline');
	process.exit(0);
}

// ---- 1. names -------------------------------------------------------------------------
const renames = Object.keys(names)
	.filter((k) => state.names[k] && state.names[k] !== names[k])
	.map((k) => ({ key: k, from: state.names[k], to: names[k] }));
if (renames.length) {
	// Two steps through placeholders, so swaps and chains (A->B, B->C) stay correct.
	const step1 = renames.map((r, i) => ({ from: r.from, to: `@@NAME${i}@@` }));
	const step2 = renames.map((r, i) => ({ from: `@@NAME${i}@@`, to: r.to }));
	for (const r of renames) console.log(`  ${r.key}: ${r.from} -> ${r.to}`);
	if (!DRY) {
		const a = R.applyRows(step1, { words: true });
		R.applyRows(step2);
		console.log(`rename_text: ${renames.length} names renamed in ${a.files} files`);
	}
}
for (const k of Object.keys(names)) if (!state.names[k]) console.log(`  ${k}: new name ${names[k]} recorded (nothing to rename)`);

// ---- 2. tables ------------------------------------------------------------------------
const dir = C.P('atlas', 'text');
const tables = fs.readdirSync(dir).filter((f) => f.endsWith('.tsv')).sort();
for (const t of tables) {
	if (state.tables.includes(t)) continue;
	const file = path.join(dir, t);
	const words = /^# mode: words/.test(fs.readFileSync(file, 'utf8'));
	const rows = R.readTable(file);
	if (DRY) {
		console.log(`  would apply ${t} (${rows.length} rows)`);
		continue;
	}
	const r = R.applyRows(rows, { words });
	console.log(`rename_text: ${t}: ${r.strings} strings in ${r.files} files`);
	state.tables.push(t);
}

if (!DRY) C.writeJSON(STATE, { tables: state.tables, names });
