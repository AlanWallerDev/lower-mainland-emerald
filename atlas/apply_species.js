#!/usr/bin/env node
// Writes every organism in atlas/species_map.json into its species slot: base stats, types,
// abilities, gender, egg groups, name, Field Journal entry and text, evolutions (real life
// stages only), and level-up, TM/HM and tutor learnsets.
//
// Idempotent: it rewrites the fields it owns and leaves the rest of each file alone.
// Body colours are set by atlas/body_colors.py after the sprites are drawn.
// Run from anywhere: node atlas/apply_species.js
'use strict';
const C = require('./lib/common');
const T = require('./lib/text');
const MV = require('./lib/moves');

const map = C.readJSON('atlas/species_map.json');
const orgs = C.loadOrganisms();
const names = C.readJSON('atlas/names.json');
const picks = C.readJSON('atlas/picks.json');
const LEGENDS = new Set(picks.legend_slots);
const moves = MV.loadMoves();
const { tms, hms } = MV.loadTMHM();
const tutors = MV.loadTutors();

const entries = map.map((e) => {
	const org = orgs[e.id];
	if (!org) throw new Error(`${e.slot}: unknown organism ${e.id}`);
	return { ...e, org };
});
const bySlot = Object.fromEntries(entries.map((e) => [e.slot, e]));
const slotOf = Object.fromEntries(entries.map((e) => [e.id, e.slot]));

// ---- rules ----------------------------------------------------------------

const gen3 = (org) => {
	const t = org.types.map((x) => 'TYPE_' + C.LA_TO_GEN3[x]);
	return [t[0], t[1] || t[0]];
};

const NO_SEX = new Set(['Plant', 'Fungus', 'Lichen', 'Alga', 'Slime Mold', 'Bacterium', 'Archaeon', 'Protist', 'Virus',
	'Oomycete', 'Sponge', 'Placozoan', 'Ediacaran', 'Mystery']);
function genderRatio(org, current) {
	const note = org.sex_note || '';
	if (NO_SEX.has(org.group) || org.family === 'microscope' || /mating types/.test(note)) return 'MON_GENDERLESS';
	if (/♀ only/.test(note)) return 'MON_FEMALE';
	if (/♂ only/.test(note)) return 'MON_MALE';
	if (/Mostly ♀/.test(note)) return 'PERCENT_FEMALE(75)';
	if (/Hermaphrodite|→/.test(note)) return 'PERCENT_FEMALE(50)';
	// Otherwise keep the slot's ratio unless it was genderless.
	return /GENDERLESS|MON_FEMALE|MON_MALE/.test(current) ? 'PERCENT_FEMALE(50)' : current;
}

const EGG = {
	Plant: 'GRASS', Fungus: 'GRASS', Alga: 'GRASS', Lichen: 'MINERAL', 'Slime Mold': 'AMORPHOUS', Bacterium: 'AMORPHOUS',
	Archaeon: 'AMORPHOUS', Protist: 'AMORPHOUS', Oomycete: 'AMORPHOUS', Virus: 'AMORPHOUS', Placozoan: 'AMORPHOUS',
	Insect: 'BUG', Arachnid: 'BUG', Myriapod: 'BUG', Springtail: 'BUG', Chelicerate: 'BUG', Arthropod: 'BUG',
	'Velvet Worm': 'BUG', Tardigrade: 'BUG', Bird: 'FLYING', Pterosaur: 'FLYING', Fish: 'WATER_2', Chordate: 'WATER_2',
	Mollusk: 'WATER_3', Cnidarian: 'WATER_3', Annelid: 'WATER_3', Crustacean: 'WATER_3', Sponge: 'WATER_3',
	Echinoderm: 'WATER_3', Tunicate: 'WATER_3', Nematode: 'WATER_3', Rotifer: 'WATER_3', Loriciferan: 'WATER_3',
	Gastrotrich: 'WATER_3', Lobopodian: 'WATER_3', Ediacaran: 'MINERAL', Amphibian: 'WATER_1', Reptile: 'MONSTER',
	Dinosaur: 'MONSTER', 'Marine Reptile': 'MONSTER', Synapsid: 'MONSTER', Mammal: 'FIELD', Mystery: 'AMORPHOUS',
};
function eggGroups(org, slot) {
	if (LEGENDS.has(slot)) return ['EGG_GROUP_NO_EGGS_DISCOVERED', 'EGG_GROUP_NO_EGGS_DISCOVERED'];
	const a = EGG[org.group] || 'FIELD';
	let b = a;
	if (org.family === 'primate') b = 'HUMAN_LIKE';
	else if (org.habitat !== 'land' && org.habitat !== 'microscope' && !a.startsWith('WATER')) b = 'WATER_1';
	return ['EGG_GROUP_' + a, 'EGG_GROUP_' + b];
}

// Living Atlas ability names -> engine abilities, by keyword. First match wins.
const ABILITY_WORDS = [
	[/venom|sting|toxin|toxic|poison|nettle|irritant/, 'POISON_POINT'],
	[/stench|smell|odou?r|musk|reek|stink/, 'STENCH'],
	[/spine|quill|spike|barb|thorn|prickl|bristle/, 'ROUGH_SKIN'],
	[/armou?r|shell|plate|scute|carapace|chitin/, 'SHELL_ARMOR'],
	[/blubber|fat|fur|down|insulat|thick/, 'THICK_FAT'],
	[/swim|fin|current|stream|torpedo|dive/, 'SWIFT_SWIM'],
	[/glow|biolumin|lantern|luminous|light organ|sparkle/, 'ILLUMINATE'],
	[/sun|photosynth|solar|leaf|chloro/, 'CHLOROPHYLL'],
	[/spore|seed|pollen/, 'EFFECT_SPORE'],
	[/eye|vision|sight|keen|watch|lookout/, 'KEEN_EYE'],
	[/electric|charge|shock|static|volt/, 'STATIC'],
	[/heat|fire|flame|burn|hot|thermal/, 'FLAME_BODY'],
	[/regener|regrow|clone|heal|longev|renew/, 'NATURAL_CURE'],
	[/camoufl|hide|cryptic|mimic|disguise|blend/, 'SAND_VEIL'],
	[/burrow|dig|tunnel|underground/, 'ARENA_TRAP'],
	[/sticky|glue|cling|grip|sucker|suction/, 'STICKY_HOLD'],
	[/shed|molt|moult/, 'SHED_SKIN'],
	[/float|drift|parachute|glide|balloon|levitat/, 'LEVITATE'],
	[/slime|mucus|ooze|goo/, 'LIQUID_OOZE'],
	[/jaw|teeth|tooth|bite|fang|tusk|horn|antler|roar|threat/, 'INTIMIDATE'],
	[/muscle|strength|brute|charge|ram|power/, 'GUTS'],
	[/swarm|colony|herd|flock|pack|school|hive/, 'SWARM'],
	[/clever|brain|mind|smart|memory|learn|navig/, 'SYNCHRONIZE'],
	[/dormant|tun|sleep|hibernat|torpor|cyst/, 'EARLY_BIRD'],
	[/sprint|speed|fast|dash|flee|escape/, 'RUN_AWAY'],
	[/cold|frost|ice|antifreeze|snow/, 'THICK_FAT'],
	[/song|call|sing|voice|echo/, 'SOUNDPROOF'],
	[/cute|charm|display|court|bright|color|colour/, 'CUTE_CHARM'],
];
const TYPE_ABILITIES = {
	Verdant: ['OVERGROW', 'CHLOROPHYLL'], Ember: ['BLAZE', 'FLASH_FIRE'], Aqua: ['TORRENT', 'WATER_VEIL'],
	Chitin: ['SWARM', 'SHIELD_DUST'], Sky: ['KEEN_EYE', 'EARLY_BIRD'], Toxin: ['POISON_POINT', 'LIQUID_OOZE'],
	Soil: ['SAND_VEIL', 'ARENA_TRAP'], Stone: ['STURDY', 'ROCK_HEAD'], Armor: ['SHELL_ARMOR', 'CLEAR_BODY'],
	Charm: ['STATIC', 'CUTE_CHARM'], Mind: ['SYNCHRONIZE', 'INNER_FOCUS'], Frost: ['THICK_FAT', 'WATER_VEIL'],
	Night: ['INSOMNIA', 'KEEN_EYE'], Brawn: ['GUTS', 'HUSTLE'], Common: ['RUN_AWAY', 'PICKUP'],
};
function abilities(org, slot, current) {
	if (LEGENDS.has(slot)) return current; // Drizzle, Drought, Air Lock and friends drive the story.
	const out = [];
	for (const name of org.abilities || []) {
		const low = name.toLowerCase();
		const hit = ABILITY_WORDS.find(([re, ab]) => re.test(low) && !out.includes(ab));
		if (hit) out.push(hit[1]);
	}
	for (const t of org.types) for (const ab of TYPE_ABILITIES[t] || []) if (out.length < 2 && !out.includes(ab)) out.push(ab);
	return '{' + out.slice(0, 2).map((a) => 'ABILITY_' + a).join(', ') + '}';
}

// ---- species_info.h --------------------------------------------------------

let info = C.read('src/data/pokemon/species_info.h');
for (const e of entries) {
	const { org, slot } = e;
	const re = new RegExp(`(\\[SPECIES_${slot}\\] =\\s*\\{)([\\s\\S]*?)(\\n    \\},?\\n)`);
	const m = info.match(re);
	if (!m) throw new Error('species_info: no block for ' + slot);
	const get = (k) => (m[2].match(new RegExp(`\\.${k}\\s*=\\s*(.*?),?\\n`)) || [])[1];
	const set = {
		baseHP: org.stats.hp, baseAttack: org.stats.atk, baseDefense: org.stats.def, baseSpeed: org.stats.spe,
		baseSpAttack: org.stats.spa, baseSpDefense: org.stats.spd,
		types: `{ ${gen3(org).join(', ')} }`,
		itemCommon: 'ITEM_NONE', itemRare: 'ITEM_NONE',
		genderRatio: genderRatio(org, get('genderRatio')),
		eggGroups: `{ ${eggGroups(org, slot).join(', ')} }`,
		abilities: abilities(org, slot, get('abilities')),
	};
	let body = m[2];
	for (const [k, v] of Object.entries(set)) {
		body = body.replace(new RegExp(`(\\.${k}\\s*=\\s*)(.*?)(,?\\n)`), (_, a, __, c) => a + v + c);
	}
	info = info.replace(re, m[1] + body + m[3]);
}
C.write('src/data/pokemon/species_info.h', info);

// ---- names ------------------------------------------------------------------

let sn = C.read('src/data/text/species_names.h');
for (const e of entries) {
	sn = sn.replace(new RegExp(`(\\[SPECIES_${e.slot}\\] = _\\(")[^"]*("\\))`), `$1${C.gameName(e.org, names)}$2`);
}
C.write('src/data/text/species_names.h', sn);

// ---- Field Journal entries and text ----------------------------------------------

/** Whole sentences of the entry that fit in four lines of 38 characters (first sentence always). */
function journalLines(entry) {
	const sentences = T.sanitize(entry).match(/[^.!?]+[.!?]+(\s|$)/g) || [T.sanitize(entry)];
	let text = '';
	let lines = [];
	for (const s of sentences.map((x) => x.trim())) {
		const next = T.wrapParagraph(text ? text + ' ' + s : s, T.BOX_WIDTH, 38);
		if (text && next.length > 4) break;
		text = text ? text + ' ' + s : s;
		lines = next;
	}
	if (lines.length > 4) {
		// The first sentence alone is too long: cut the fourth line and end it with an ellipsis.
		lines = lines.slice(0, 4);
		let last = lines[3].split(' ');
		while (last.length > 1 && (last.join(' ') + '…').length > 38) last.pop();
		lines[3] = last.join(' ').replace(/[,;:]$/, '') + '…';
	}
	return lines;
}

let pe = C.read('src/data/pokemon/pokedex_entries.h');
let pt = C.read('src/data/pokemon/pokedex_text.h');
for (const e of entries) {
	const { org, slot } = e;
	const re = new RegExp(`(\\[NATIONAL_DEX_${slot}\\] =\\s*\\{)([\\s\\S]*?)(\\n    \\},)`);
	const m = pe.match(re);
	if (!m) throw new Error('pokedex_entries: no block for ' + slot);
	const category = T.sanitize(org.category).toUpperCase().replace(/[^A-Z0-9 '.-]/g, '').slice(0, 11);
	const height = Math.max(1, Math.round(org.height_in * 0.254));
	const weight = Math.max(1, Math.round(org.weight_lb * 4.536));
	let body = m[2]
		.replace(/(\.categoryName = _\(")[^"]*("\))/, `$1${category}$2`)
		.replace(/(\.height = )\d+/, `$1${height}`)
		.replace(/(\.weight = )\d+/, `$1${weight}`);
	pe = pe.replace(re, m[1] + body + m[3]);
	const textName = body.match(/\.description = (\w+)/)[1];
	const lines = journalLines(org.entry);
	const literal = lines.map((l, i) => `    "${l.replace(/"/g, '\\"')}${i < lines.length - 1 ? '\\n' : ''}"`).join('\n');
	pt = pt.replace(new RegExp(`(const u8 ${textName}\\[\\] = _\\(\\n)[\\s\\S]*?(\\);)`), `$1${literal}$2`);
}
C.write('src/data/pokemon/pokedex_entries.h', pe);
C.write('src/data/pokemon/pokedex_text.h', pt);

// ---- evolutions: only real life stages -----------------------------------------------

const lines = {};
for (const e of entries) if (e.org.line) (lines[e.org.line] = lines[e.org.line] || []).push(e);
const evo = [];
for (const members of Object.values(lines)) {
	members.sort((a, b) => a.id.localeCompare(b.id));
	const levels = members.length >= 3 ? [14, 28] : [18];
	for (let i = 0; i < members.length - 1; i++) {
		evo.push(`    [SPECIES_${members[i].slot}] = {{EVO_LEVEL, ${levels[Math.min(i, levels.length - 1)]}, SPECIES_${members[i + 1].slot}}},`);
	}
}
C.write('src/data/pokemon/evolution.h',
	'// Generated by atlas/apply_species.js. Only Living Atlas life stages evolve.\n' +
	'const struct Evolution gEvolutionTable[NUM_SPECIES][EVOS_PER_MON] =\n{\n' + evo.join('\n') + '\n};\n');

// ---- level-up learnsets ----------------------------------------------------------

const ptrs = C.read('src/data/pokemon/level_up_learnset_pointers.h');
let lu = C.read('src/data/pokemon/level_up_learnsets.h');
const learned = {};
for (const e of entries) {
	const arr = ptrs.match(new RegExp(`\\[SPECIES_${e.slot}\\] = (\\w+)`))[1];
	const set = MV.levelUpLearnset(e.org, moves);
	// Later life stages keep what the earlier stage knew.
	learned[e.slot] = set;
	const rows = set.map(([lv, mvName]) => `    LEVEL_UP_MOVE(${String(lv).padStart(2)}, MOVE_${mvName}),`).join('\n');
	lu = lu.replace(new RegExp(`(static const u16 ${arr}\\[\\] = \\{\\n)[\\s\\S]*?(    LEVEL_UP_END)`), `$1${rows}\n$2`);
}
C.write('src/data/pokemon/level_up_learnsets.h', lu);

// ---- TM/HM compatibility ---------------------------------------------------------

const UNIVERSAL_TM = ['TOXIC', 'HIDDEN_POWER', 'PROTECT', 'RETURN', 'FRUSTRATION', 'DOUBLE_TEAM', 'FACADE', 'SECRET_POWER', 'REST'];
const WEATHER = { SUNNY_DAY: ['Ember', 'Verdant', 'Common'], RAIN_DANCE: ['Aqua'], SANDSTORM: ['Soil', 'Stone'], HAIL: ['Frost'] };
const STRONG = new Set(['quadruped', 'primate', 'low_reptile', 'serpentine', 'dinosaur']);

function hmOk(org, hm) {
	const t = new Set(org.types);
	const fam = org.family;
	const micro = fam === 'microscope';
	const text = (org.entry || '').toLowerCase();
	switch (hm) {
	case 'CUT': return !micro && (t.has('Verdant') || t.has('Chitin') || t.has('Brawn') || t.has('Armor') || t.has('Night') || ['quadruped', 'insect', 'many_legged', 'primate', 'low_reptile'].includes(fam));
	case 'FLY': return t.has('Sky') && fam === 'flier' && org.weight_lb >= 1;
	case 'SURF': case 'DIVE': case 'WATERFALL': return !micro && (t.has('Aqua') || org.habitat === 'aquatic' || org.habitat === 'amphibious');
	case 'STRENGTH': case 'ROCK_SMASH': return !micro && (t.has('Brawn') || t.has('Stone') || t.has('Soil') || t.has('Armor') || (STRONG.has(fam) && org.stats.atk >= 70));
	case 'FLASH': return t.has('Charm') || t.has('Mind') || t.has('Ember') || /glow|light|biolumin/.test(text);
	}
	return false;
}

function tmOk(org, name) {
	if (UNIVERSAL_TM.includes(name)) return true;
	if (name === 'ATTRACT') return !NO_SEX.has(org.group) && org.family !== 'microscope';
	if (WEATHER[name]) return WEATHER[name].some((t) => org.types.includes(t));
	const m = moves[name];
	if (!m || !org.types.some((t) => C.LA_TO_GEN3[t] === m.type)) return false;
	return MV.bodyAllows(org, name);
}

let tm = C.read('src/data/pokemon/tmhm_learnsets.h');
for (const e of entries) {
	const on = tms.filter((n) => tmOk(e.org, n)).concat(hms.filter((n) => hmOk(e.org, n)));
	const block = `    [SPECIES_${e.slot}] = { .learnset = {\n` + on.map((n) => `        .${n} = TRUE,\n`).join('') + '    } },';
	tm = tm.replace(new RegExp(`    \\[SPECIES_${e.slot}\\] = \\{ \\.learnset = \\{\\n[\\s\\S]*?    \\} \\},`), block);
}
C.write('src/data/pokemon/tmhm_learnsets.h', tm);

// ---- tutors ------------------------------------------------------------------------

const UNIVERSAL_TUTOR = ['MIMIC', 'SUBSTITUTE', 'SNORE', 'ENDURE', 'SWAGGER', 'SLEEP_TALK'];
const BODY_TUTOR = ['BODY_SLAM', 'DOUBLE_EDGE'];
let tu = C.read('src/data/pokemon/tutor_learnsets.h');
for (const e of entries) {
	const org = e.org;
	const on = tutors.filter((n) => {
		if (UNIVERSAL_TUTOR.includes(n)) return true;
		if (BODY_TUTOR.includes(n)) return org.family !== 'microscope' && org.family !== 'sessile';
		const m = moves[n];
		return m && m.power > 0 && org.types.some((t) => C.LA_TO_GEN3[t] === m.type) && MV.bodyAllows(org, n);
	});
	const pad = `[SPECIES_${e.slot}]`.padEnd(26);
	const body = on.length ? '(' + on.map((n) => `TUTOR(MOVE_${n})`).join('\n                                | ') + ')' : '(0)';
	tu = tu.replace(new RegExp(`    \\[SPECIES_${e.slot}\\]\\s*= \\([\\s\\S]*?\\),\\n`), `    ${pad} = ${body},\n`);
}
C.write('src/data/pokemon/tutor_learnsets.h', tu);

console.log(`apply_species: ${entries.length} organisms written, ${evo.length} evolutions`);
