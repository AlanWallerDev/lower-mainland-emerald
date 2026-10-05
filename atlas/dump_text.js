#!/usr/bin/env node
// Print each map's script text as one line per block, for reading an area's dialogue at once.
// Usage: node atlas/dump_text.js MapPrefix [MapPrefix...]   e.g. node atlas/dump_text.js OldaleTown Route102
'use strict';
const fs = require('fs');
const C = require('./lib/common');
const T = require('./lib/text');

const prefixes = process.argv.slice(2);
for (const map of fs.readdirSync(C.P('data', 'maps')).sort()) {
	if (!prefixes.some((p) => map === p || map.startsWith(p + '_'))) continue;
	const file = C.P('data', 'maps', map, 'scripts.inc');
	if (!fs.existsSync(file)) continue;
	console.log(`== ${map}`);
	for (const b of T.findBlocks(fs.readFileSync(file, 'utf8').split('\n'))) {
		console.log(`${b.label}: ${b.strings.join('').replace(/\\[nl]/g, ' ').replace(/\$$/, '')}`);
	}
}
