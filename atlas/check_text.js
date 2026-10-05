#!/usr/bin/env node
// Report script text lines wider than the message box. Lines kept verbatim from upstream are skipped
// (placeholders like {STR_VAR_1} are measured at a worst-case width), as are hand-laid-out blocks.
// Usage: node atlas/check_text.js [--all]   (default: only lines of maps and data/text)
'use strict';
const fs = require('fs');
const path = require('path');
const C = require('./lib/common');
const T = require('./lib/text');

const ALL = process.argv.includes('--all');
const files = [];
(function walk(d) {
	for (const e of fs.readdirSync(d, { withFileTypes: true })) {
		const p = path.join(d, e.name);
		if (e.isDirectory()) walk(p);
		else if (/\.inc$/.test(p) && (ALL || /[\\/]text[\\/]|[\\/]scripts\.inc$/.test(p))) files.push(p);
	}
})(C.P('data'));
let hits = 0;
for (const f of files) {
	let orig = '';
	try {
		orig = require('child_process').execFileSync('git', ['show', 'upstream/master:' + path.relative(C.ROOT, f).split(path.sep).join('/')],
			{ cwd: C.ROOT, encoding: 'utf8', maxBuffer: 64 << 20, stdio: ['ignore', 'pipe', 'ignore'] });
	} catch (e) { /* new file */ }
	const kept = new Set(orig.split('\n').map((l) => (l.match(/\.string "(.*)"/) || [])[1]).filter(Boolean)
		.flatMap((s) => s.split(/\\[nlp]/)));
	for (const b of T.findBlocks(fs.readFileSync(f, 'utf8').split('\n'))) {
		const text = b.strings.join('');
		if (/CLEAR_TO|\{\w*ARROW\}/.test(text)) continue;
		for (const line of text.split(/\\[nlp]/)) {
			const w = T.measure(line.replace(/\$$/, ''));
			if (w > T.BOX_WIDTH && !kept.has(line)) {
				hits++;
				console.log(`${path.relative(C.ROOT, f)} ${b.label}: ${w}px "${line}"`);
			}
		}
	}
}
// Item descriptions: the bag's description window leaves 109px per line.
const ITEM_WIDTH = 109;
for (const line of C.read('src/data/text/item_descriptions.h').split('\n')) {
	const m = line.match(/^\s+"(.*?)(?:\\n)?"\)?;?$/);
	if (m && !m[1].includes('{') && T.measure(m[1]) > ITEM_WIDTH) {
		hits++;
		console.log(`item description: ${T.measure(m[1])}px "${m[1]}"`);
	}
}
console.log(`check_text: ${hits} lines too wide (message box ${T.BOX_WIDTH}px, item descriptions ${ITEM_WIDTH}px)`);
process.exitCode = hits ? 1 : 0;
