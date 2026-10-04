// Game text helpers: pixel widths in the normal font, .inc text blocks, and re-wrapping to the
// message box.
'use strict';
const { read } = require('./common');

/** Usable width of the standard message box, in pixels. */
const BOX_WIDTH = 208;

let widths = null;
function loadWidths() {
	if (widths) return widths;
	const table = read('src/fonts.c').match(/gFontNormalLatinGlyphWidths\[\] = \{([\s\S]*?)\};/)[1]
		.split(/[\s,]+/).filter(Boolean).map(Number);
	widths = new Map();
	for (const m of read('charmap.txt').matchAll(/^'(.+?)'\s*=\s*([0-9A-F]{2})\s*$/gm)) {
		const ch = m[1] === "\\'" ? "'" : m[1];
		if (!widths.has(ch)) widths.set(ch, table[parseInt(m[2], 16)]);
	}
	return widths;
}

// Placeholders and their widest likely expansion.
const NAME_WIDTH = { PLAYER: 42, RIVAL: 42, STR_VAR_1: 60, STR_VAR_2: 60, STR_VAR_3: 60 };

/** Width in pixels of one line of game text (no line breaks). */
function measure(s) {
	const w = loadWidths();
	let total = 0;
	for (let i = 0; i < s.length; i++) {
		const c = s[i];
		if (c === '{') {
			const end = s.indexOf('}', i);
			const tag = s.slice(i + 1, end).split(' ')[0];
			total += NAME_WIDTH[tag] || (/^(COLOR|SHADOW|HIGHLIGHT|PAUSE|PLAY_|FONT_|CLEAR|WAIT|RESET|KUN|ESCAPE)/.test(tag) ? 0 : 60);
			i = end;
		} else if (c === '\\') {
			i++;
		} else {
			total += w.get(c) ?? 6;
		}
	}
	return total;
}

/** Replace characters the game font lacks: degrees, macrons, straight double quotes, okina. */
function sanitize(s) {
	let open = true;
	return s
		.replace(/°([CF])\b/g, ' degrees $1').replace(/°/g, ' degrees')
		.replace(/[āĀ]/g, (c) => (c === 'ā' ? 'a' : 'A')).replace(/[ēĒ]/g, (c) => (c === 'ē' ? 'e' : 'E'))
		.replace(/[ōŌ]/g, (c) => (c === 'ō' ? 'o' : 'O')).replace(/[ūŪ]/g, (c) => (c === 'ū' ? 'u' : 'U'))
		.replace(/[īĪ]/g, (c) => (c === 'ī' ? 'i' : 'I')).replace(/ø/g, 'o').replace(/Ø/g, 'O')
		.replace(/[ʻʼ‘]/g, '’').replace(/[–—]/g, '-')
		.replace(/"/g, () => ((open = !open) ? '”' : '“'));
}

/** Split a logical message into lines no wider than `width` pixels (and `maxChars`), breaking at spaces. */
function wrapParagraph(text, width = BOX_WIDTH, maxChars = Infinity) {
	const words = text.split(' ').filter((x) => x !== '');
	const lines = [];
	let cur = '';
	for (const word of words) {
		const next = cur ? cur + ' ' + word : word;
		if (cur && (measure(next) > width || next.length > maxChars)) {
			lines.push(cur);
			cur = word;
		} else {
			cur = next;
		}
	}
	if (cur) lines.push(cur);
	return lines;
}

/**
 * Parse a block of `.string "..."` lines into paragraphs of plain text: \n and \l become
 * spaces, \p starts a new paragraph. Returns null for text that uses other layout tricks.
 */
function blockToParagraphs(strings) {
	let s = strings.join('');
	if (!s.endsWith('$')) return null;
	s = s.slice(0, -1);
	return s.split('\\p').map((p) => p.replace(/\\[nl]/g, ' ').replace(/ +/g, ' ').trim());
}

/** Lay paragraphs out as `.string` lines in Emerald's style (\n, then \l, \p between paragraphs). */
function paragraphsToStrings(paras, width = BOX_WIDTH) {
	const out = [];
	paras.forEach((p, pi) => {
		const lines = wrapParagraph(p, width);
		lines.forEach((line, li) => {
			const last = li === lines.length - 1;
			const end = !last ? (li === 0 ? '\\n' : '\\l') : pi < paras.length - 1 ? '\\p' : '$';
			out.push(line + end);
		});
	});
	return out;
}

/**
 * Find text blocks in an .inc/.s file: a label line followed by `.string` lines.
 * Returns [{label, start, end, indent, strings}] with line indices into `lines`.
 */
function findBlocks(lines) {
	const blocks = [];
	for (let i = 0; i < lines.length; i++) {
		const lab = lines[i].match(/^(\w+)::?\s*$/);
		if (!lab || !/^\s*\.string "/.test(lines[i + 1] || '')) continue;
		const strings = [];
		let j = i + 1;
		let indent = lines[j].match(/^\s*/)[0];
		while (j < lines.length) {
			const m = lines[j].match(/^\s*\.string "(.*)"\s*$/);
			if (!m) break;
			strings.push(m[1]);
			j++;
			if (m[1].endsWith('$')) break;
		}
		blocks.push({ label: lab[1], start: i + 1, end: j, indent, strings });
		i = j - 1;
	}
	return blocks;
}

module.exports = { BOX_WIDTH, sanitize, measure, wrapParagraph, blockToParagraphs, paragraphsToStrings, findBlocks };
