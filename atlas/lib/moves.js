// Engine move data and learnset building. Moves keep their names; types are the retyped ones
// in src/data/battle_moves.h (see atlas/apply_types.py).
'use strict';
const { read, LA_TO_GEN3 } = require('./common');

/** All moves from battle_moves.h: {NAME: {effect, power, type, accuracy, pp}}. */
function loadMoves() {
	const src = read('src/data/battle_moves.h');
	const out = {};
	for (const m of src.matchAll(/\[MOVE_(\w+)\] =\s*\{([\s\S]*?)\n    \},/g)) {
		const f = {};
		for (const k of m[2].matchAll(/\.(\w+) = ([^,\n]+)/g)) f[k[1]] = k[2].trim();
		out[m[1]] = {
			name: m[1], effect: f.effect, power: +f.power, type: (f.type || '').replace('TYPE_', ''),
			accuracy: +f.accuracy, pp: +f.pp,
		};
	}
	return out;
}

/** TM and HM move names in bitfield order. */
function loadTMHM() {
	const src = read('include/constants/tms_hms.h');
	const grab = (name) => [...src.slice(src.indexOf('#define ' + name)).split('\n\n')[0].matchAll(/F\((\w+)\)/g)].map((m) => m[1]);
	return { tms: grab('FOREACH_TM'), hms: grab('FOREACH_HM') };
}

/** Tutor move names in table order. */
function loadTutors() {
	return [...read('src/data/pokemon/tutor_learnsets.h').matchAll(/\[TUTOR_MOVE_(\w+)\] = MOVE_\w+/g)].map((m) => m[1]);
}

// Moves no organism learns by level: one-offs, self-KOs, copy moves and HM field moves.
const NEVER = new Set([
	'NONE', 'STRUGGLE', 'SKETCH', 'TRANSFORM', 'MIMIC', 'METRONOME', 'MIRROR_MOVE', 'SELF_DESTRUCT', 'EXPLOSION',
	'MEMENTO', 'DESTINY_BOND', 'PERISH_SONG', 'SPLASH', 'CUT', 'FLY', 'SURF', 'STRENGTH', 'FLASH', 'ROCK_SMASH',
	'WATERFALL', 'DIVE', 'SECRET_POWER', 'HIDDEN_POWER', 'RETURN', 'FRUSTRATION', 'NATURE_POWER', 'ASSIST',
	'SLEEP_TALK', 'SNORE', 'BIDE', 'DOOM_DESIRE', 'PSYCHO_BOOST', 'SPACIAL_REND', 'ERUPTION', 'WATER_SPOUT',
	'BEAT_UP', 'PRESENT', 'MAGNITUDE', 'SONIC_BOOM', 'DRAGON_RAGE', 'SEISMIC_TOSS', 'NIGHT_SHADE', 'PSYWAVE',
	'SUPER_FANG', 'ENDEAVOR', 'FISSURE', 'GUILLOTINE', 'HORN_DRILL', 'SHEER_COLD', 'LOW_KICK', 'FLAIL', 'REVERSAL',
	'COUNTER', 'MIRROR_COAT', 'TRIPLE_KICK', 'SKY_UPPERCUT', 'BLAST_BURN', 'HYDRO_CANNON', 'FRENZY_PLANT',
	'HYPER_BEAM', 'FOCUS_PUNCH', 'SOLAR_BEAM', 'SKY_ATTACK', 'LUSTER_PURGE', 'MIST_BALL', 'TEETER_DANCE',
	'SPIT_UP', 'SWALLOW', 'STOCKPILE', 'UPROAR', 'SMELLING_SALT', 'FUTURE_SIGHT', 'DREAM_EATER', 'RAGE',
	'RAZOR_WIND', 'SKULL_BASH', 'FAKE_OUT', 'SPIKE_CANNON', 'SELF_DESTRUCT', 'HEAL_BELL', 'AEROBLAST', 'SACRED_FIRE', 'BARRAGE', 'EGG_BOMB',
]);
// First move of each type, given at level 1 (Normal) or level 5 (the organism's own type).
const FIRST = {
	NORMAL: 'TACKLE', FIGHTING: 'ARM_THRUST', FLYING: 'PECK', POISON: 'POISON_STING', GROUND: 'MUD_SLAP',
	ROCK: 'ROCK_THROW', BUG: 'LEECH_LIFE', STEEL: 'METAL_CLAW', FIRE: 'EMBER', WATER: 'BUBBLE', GRASS: 'ABSORB',
	ELECTRIC: 'THUNDER_SHOCK', PSYCHIC: 'CONFUSION', ICE: 'POWDER_SNOW', DARK: 'ASTONISH',
};
// Opening status moves by type (lower a foe stat or set up), used at level 1 and in the mid levels.
const STATUS = {
	NORMAL: ['GROWL', 'LEER', 'TAIL_WHIP', 'DEFENSE_CURL', 'HARDEN', 'FOCUS_ENERGY', 'SWORDS_DANCE', 'SCARY_FACE'],
	FIGHTING: ['BULK_UP', 'DETECT'], FLYING: ['FEATHER_DANCE', 'MIRROR_MOVE', 'ROOST'], POISON: ['POISON_POWDER', 'POISON_GAS', 'TOXIC', 'ACID_ARMOR'],
	GROUND: ['SAND_ATTACK', 'MUD_SPORT', 'SPIKES'], ROCK: ['ROCK_POLISH', 'SANDSTORM'], BUG: ['STRING_SHOT', 'SPIDER_WEB', 'TAIL_GLOW'],
	STEEL: ['IRON_DEFENSE', 'METAL_SOUND'], FIRE: ['SUNNY_DAY', 'WILL_O_WISP'], WATER: ['WITHDRAW', 'RAIN_DANCE', 'WATER_SPORT'],
	GRASS: ['GROWTH', 'LEECH_SEED', 'SYNTHESIS', 'STUN_SPORE', 'SLEEP_POWDER', 'COTTON_SPORE', 'INGRAIN'],
	ELECTRIC: ['THUNDER_WAVE', 'CHARGE'], PSYCHIC: ['CALM_MIND', 'CONFUSION', 'AMNESIA', 'REFLECT', 'LIGHT_SCREEN'],
	ICE: ['HAIL', 'MIST', 'HAZE'], DARK: ['CONFUSE_RAY', 'SPITE', 'SNATCH', 'FAKE_TEARS', 'TORMENT'],
};

const JAWLESS = new Set(['Plant', 'Fungus', 'Bacterium', 'Archaeon', 'Protist', 'Alga', 'Lichen', 'Virus', 'Cnidarian',
	'Sponge', 'Oomycete', 'Slime Mold']);
const CLAWED = new Set(['quadruped', 'many_legged', 'insect', 'low_reptile', 'flier', 'primate']);
const LEGGED = new Set(['quadruped', 'primate', 'flier', 'many_legged', 'insect', 'low_reptile']);

/** Whether an organism's body could plausibly make a move (no fangs on plants, no punches on birds). */
function bodyAllows(org, name) {
	const text = (org.name + ' ' + (org.entry || '')).toLowerCase();
	if (/PUNCH|CHOP|ARM_THRUST|SUBMISSION|CROSS_CHOP/.test(name)) return org.family === 'primate' || org.group === 'Crustacean';
	if (/FANG|BITE|CRUNCH/.test(name)) return !JAWLESS.has(org.group) && org.family !== 'microscope';
	if (/HORN/.test(name)) return /horn|antler|tusk/.test(text);
	if (/KICK|STOMP/.test(name)) return LEGGED.has(org.family);
	if (/CLAW|SWIPES|SLASH|SCRATCH|VICE_GRIP|CRABHAMMER/.test(name)) return CLAWED.has(org.family) || org.group === 'Crustacean';
	if (/PECK/.test(name)) return org.group === 'Bird';
	return true;
}

/** Small stable hash for picking among equal options per organism. */
function hash(s) {
	let h = 2166136261;
	for (const c of s) h = Math.imul(h ^ c.charCodeAt(0), 16777619) >>> 0;
	return h;
}

/**
 * Level-up learnset for an organism: a weak opener and a status move at level 1, then damaging
 * moves of its types in rising power, with a few status moves between. Returns [[level, MOVE]].
 */
function levelUpLearnset(org, moves) {
	const types = [...new Set(org.types.map((t) => LA_TO_GEN3[t]))];
	const h = hash(org.id);
	const usable = Object.values(moves).filter((m) => !NEVER.has(m.name));
	const damaging = (t) => usable.filter((m) => m.type === t && m.power > 1 && bodyAllows(org, m.name)).sort((a, b) => a.power - b.power || a.name.localeCompare(b.name));
	const status = (t) => (STATUS[t] || []).filter((n) => moves[n] && moves[n].power === 0 && !NEVER.has(n));

	// Opener: Scratch for clawed animals, else Tackle; then the first move of its own type at 5.
	const clawed = ['quadruped', 'primate', 'many_legged', 'low_reptile'].includes(org.family);
	const opener = moves[clawed && org.group !== 'Bird' ? 'SCRATCH' : FIRST.NORMAL];
	const firstStatus = status('NORMAL').slice(0, 4);
	const list = [[1, opener.name], [1, firstStatus[h % firstStatus.length]]];
	const firstOk = (n) => n && n !== 'TACKLE' && moves[n] && bodyAllows(org, n);
	const ownFirst = types.map((t) => FIRST[t]).find(firstOk);
	if (ownFirst) list.push([5, ownFirst]);

	// Damaging moves of its types, at most 8, spread over power bands.
	const pool = [];
	for (const t of types) pool.push(...damaging(t));
	if (!types.includes('NORMAL')) pool.push(...damaging('NORMAL').filter((m) => m.power >= 60 && m.power <= 90).slice(0, 2));
	const chosen = [];
	const bands = [[0, 40], [41, 55], [56, 70], [71, 85], [86, 100], [101, 200]];
	for (const [lo, hi] of bands) {
		const inBand = pool.filter((m) => m.power >= lo && m.power <= hi && !chosen.includes(m) && m.name !== opener.name && m.name !== ownFirst);
		for (let k = 0; k < Math.min(2, inBand.length); k++) chosen.push(inBand[(h + k * 7) % inBand.length]);
	}
	const dmg = [...new Set(chosen)].sort((a, b) => a.power - b.power).slice(0, 9);

	// Status moves of its own types, two at most.
	const st = [];
	for (const t of types) for (const n of status(t)) if (!st.includes(n) && !list.some((l) => l[1] === n)) st.push(n);
	const pickedStatus = st.length ? [st[h % st.length], st[(h >> 3) % st.length]].filter((v, i, a) => a.indexOf(v) === i) : [];

	// Levels: damaging moves spread from 5 to ~50 by power; status moves slot in at 12 and 30.
	const span = dmg.length;
	dmg.forEach((m, i) => list.push([Math.round(9 + (41 * i) / Math.max(1, span - 1)) + (h % 3), m.name]));
	if (pickedStatus[0]) list.push([12 + (h % 4), pickedStatus[0]]);
	if (pickedStatus[1]) list.push([30 + (h % 5), pickedStatus[1]]);
	const seen = new Set();
	return list.filter(([, n]) => n && !seen.has(n) && seen.add(n)).sort((a, b) => a[0] - b[0]);
}

module.exports = { loadMoves, loadTMHM, loadTutors, levelUpLearnset, bodyAllows, hash, NEVER };
