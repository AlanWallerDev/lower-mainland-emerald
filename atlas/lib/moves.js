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
	'BONE_CLUB', 'BONE_RUSH', 'BONEMERANG', 'PAY_DAY', 'SOFT_BOILED', 'MILK_DRINK', 'OCTAZOOKA', 'SPIKE_CANNON',
]);
// First move of each type, given at level 1 (Normal) or level 5 (the organism's own type).
// Fallbacks in order: the first one the organism's body allows.
const FIRST = {
	NORMAL: ['TACKLE'], FIGHTING: ['ARM_THRUST', 'DOUBLE_KICK', 'KARATE_CHOP'], FLYING: ['PECK', 'GUST'],
	POISON: ['POISON_STING', 'ACID', 'SMOG'], GROUND: ['MUD_SLAP'], ROCK: ['ROCK_THROW'], BUG: ['LEECH_LIFE'],
	STEEL: ['METAL_CLAW', 'IRON_DEFENSE'], FIRE: ['EMBER'], WATER: ['BUBBLE', 'WATER_GUN'], GRASS: ['ABSORB'],
	ELECTRIC: ['THUNDER_SHOCK'], PSYCHIC: ['CONFUSION'], ICE: ['POWDER_SNOW'], DARK: ['ASTONISH', 'BITE', 'SPITE'],
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

// Organisms that can't move their whole body: no charging or body-contact moves, and their own opener.
const SESSILE = new Set(['Plant', 'Fungus', 'Bacterium', 'Archaeon', 'Protist', 'Alga', 'Lichen', 'Virus', 'Sponge',
	'Oomycete', 'Slime Mold']);
const SESSILE_OPENER = { Bacterium: 'ACID', Archaeon: 'ACID', Protist: 'ACID', Virus: 'ACID', Sponge: 'BUBBLE' };
const VERTEBRATE = new Set(['Mammal', 'Bird', 'Reptile', 'Amphibian', 'Fish', 'Dinosaur', 'Pterosaur', 'Marine Reptile',
	'Synapsid', 'Mystery']);
const ARTHROPOD = new Set(['Insect', 'Arachnid', 'Crustacean', 'Myriapod', 'Chelicerate', 'Arthropod', 'Springtail']);
// Moves a whole-body charge or a big movement makes: never for sessile organisms or microbes.
const HEAVY = /^(.*TACKLE|BODY_SLAM|TAKE_DOWN|DOUBLE_EDGE|QUICK_ATTACK|HEADBUTT|EXTREME_SPEED|RAPID_SPIN|ROLLOUT|SLAM|STOMP|THRASH|OUTRAGE|FACADE|AERIAL_ACE|WING_ATTACK|DIG|DIVE|ROCK_SMASH|BRICK_BREAK|ICE_BALL|STEEL_WING|PURSUIT|ASTONISH|COVET|THIEF|KNOCK_OFF|FAINT_ATTACK|AGILITY|BULK_UP|DOUBLE_TEAM|MINIMIZE|FLAME_WHEEL|CLAMP|SWORDS_DANCE|DRAGON_DANCE|TEETER_DANCE|BOUNCE|SUPERPOWER|REVENGE|VITAL_THROW|FALSE_SWIPE|POUND|FURY_ATTACK|PIN_MISSILE|TWINEEDLE|FURY_CUTTER|.*_TAIL|BONE.*|DOUBLE_SLAP|COMET_PUNCH|METEOR_MASH|.*_PUNCH|.*_KICK|.*_FANG|.*_CLAW)$/;
// Microbes can still bump, wrap and squeeze.
const MICRO_OK = new Set(['TACKLE', 'QUICK_ATTACK', 'WRAP', 'BIND', 'CONSTRICT']);

/** Body facts about an organism, read from its group, body family, weight and name/entry text. */
function body(org) {
	const text = (org.name + ' ' + (org.entry || '')).toLowerCase();
	const name = org.name.toLowerCase();
	const g = org.group;
	const fam = org.family;
	const micro = fam === 'microscope';
	const sessile = SESSILE.has(g) || fam === 'sessile';
	const vert = VERTEBRATE.has(g) && !micro;
	const hoofed = /deer|elk|moose|caribou|bison|sheep|goat|muskox|pronghorn|boar|horse|rhino|hippo/.test(name) || /elephant(?! seal)/.test(name);
	const frog = /frog|toad|tadpole/.test(name);
	const raptor = /eagle|hawk|owl|falcon|osprey|kite|harrier|vulture|condor|kestrel|merlin/.test(name);
	const whale = /whale|porpoise|dolphin|orca|narwhal|manatee/.test(name);
	const cephalopod = /octopus|squid|argonaut|cuttle|ammonite/.test(name);
	const shelled = /turtle|tortoise|snail|oyster|clam|mussel|scallop|abalone|geoduck|crab|hermit|barnacle|isopod|armadillo|horseshoe|ammonite|argonaut|limpet|lobster|prawn|shrimp/.test(name);
	const tailed = (vert && !frog && !/sasquatch|bat\b/.test(name) && g !== 'Bird') || g === 'Bird'
		|| /scorpion|lobster|prawn|shrimp|crayfish|mayfly|darner|nymph|horseshoe|tadpole|tailed frog/.test(name);
	return {
		text, name, g, fam, micro, sessile, vert, frog, raptor, cephalopod,
		animal: !micro && !sessile,
		voiced: (['Mammal', 'Bird', 'Mystery', 'Dinosaur', 'Pterosaur'].includes(g) && !/manatee/.test(name))
			|| (frog && !/tadpole/.test(name)) || /cricket|locust|cicada|katydid|grasshopper/.test(name),
		tailed: tailed && !micro,
		eyed: (vert || ARTHROPOD.has(g) || cephalopod || /snail|scallop/.test(name)) && !micro,
		faced: vert,
		tongue: ['Mammal', 'Reptile', 'Amphibian', 'Dinosaur', 'Synapsid', 'Mystery'].includes(g) && !micro && !whale && !/turtle|tadpole|larva/.test(name),
		fanged: (['Mammal', 'Reptile', 'Dinosaur', 'Pterosaur', 'Marine Reptile', 'Synapsid', 'Mystery', 'Fish'].includes(g)
			&& !/turtle|baleen|humpback|gray whale|fin whale|whale shark|manta|sturgeon|seahorse|hagfish|lamprey|alevin|smolt|herring|eulachon|platypus|anteater|sloth|armadillo|manatee/.test(name))
			|| /spider|widow|tarantula|centipede|tick/.test(name),
		jawed: (vert && !/alevin|lamprey|hagfish/.test(name)) || (ARTHROPOD.has(g) && !micro) || cephalopod,
		clawed: (['Mammal', 'Mystery'].includes(g) && ['quadruped', 'primate'].includes(fam) && !hoofed && !/seal|sea lion|walrus/.test(name))
			|| (['Reptile', 'Dinosaur', 'Pterosaur'].includes(g) && !/snake|boa|sidewinder|sea turtle|hatchling/.test(name) && fam !== 'serpentine')
			|| (g === 'Bird' && raptor) || (!sessile && /mantis|scorpion|crab|lobster|crayfish|anomalocaris|bat\b|mole|badger/.test(name)),
		pincered: !sessile && /crab|lobster|crayfish|scorpion|stag beetle|earwig|anomalocaris|horseshoe/.test(name),
		bivalve: /\b(oyster|clam|mussel|scallop|geoduck)\b/.test(name) || (g === 'Crustacean' && /crab|lobster/.test(name)),
		crustacean: g === 'Crustacean' && /crab|lobster|crayfish/.test(name),
		slow: ['Annelid', 'Echinoderm', 'Cnidarian', 'Sponge', 'Tunicate', 'Placozoan'].includes(g) || (g === 'Mollusk' && !cephalopod),
		rodent: /squirrel|\brat\b|woodrat|mouse|beaver|marmot|groundhog|porcupine|lemming|\bhare\b|pika|rabbit|chipmunk|vole|muskrat|capybara/.test(name),
		beaked: g === 'Bird' || g === 'Pterosaur' || /platypus|octopus|squid|turtle/.test(name),
		winged: fam === 'flier' || (g === 'Insect' && org.types.includes('Sky'))
			|| (g === 'Insect' && !/caterpillar|worm|nymph|larva|ant\b|termite/.test(name) && /bee|wasp|hornet|moth|butterfly|swallowtail|beetle|fly|darner|mayfly|cloak|monarch|locust|scarab|mantis/.test(name)),
		feathered: g === 'Bird',
		legged: (['quadruped', 'primate', 'dinosaur'].includes(fam) && !micro) || (g === 'Bird' && !/hummingbird|swift/.test(name)),
		kicker: hoofed || fam === 'primate' || fam === 'dinosaur'
			|| /hare|rabbit|kangaroo|locust|grasshopper|cricket|roadrunner|ostrich|emu|cassowary|sage-grouse/.test(name),
		heavy: org.weight_lb >= 30 && !micro && !sessile,
		silk: g === 'Arachnid' && !/scorpion|tick|mite/.test(name) || /caterpillar|silk|mopane worm|webworm|sphinx caterpillar/.test(name),
		stinger: /bee|wasp|hornet|ant\b|velvet ant|scorpion|jelly|man o' war|siphonophore|anemone|polyp|ephyra|nettle|thistle|urchin|ray\b|ratfish|lionfish|stonefish|caterpillar|cone snail|fireworm|platypus|lumpsucker|stickleback|spiny|cactus|devil/.test(text) || g === 'Cnidarian',
		plant: g === 'Plant' || g === 'Alga',
		flowering: g === 'Plant' && !/pine|spruce|fir\b|cedar|hemlock|sequoia|redwood|yew|fern|moss|horsetail|cycad|ginkgo/.test(name),
		spores: ['Plant', 'Fungus', 'Lichen', 'Slime Mold', 'Oomycete'].includes(g) || /moth|butterfly|swallowtail|monarch|cloak/.test(name),
		photosynth: ['Plant', 'Alga', 'Lichen'].includes(g) || /alga|cyanobacter/.test(text),
		rooted: ['Plant', 'Fungus', 'Lichen', 'Alga'].includes(g),
		glows: /glow|lumin|firefly|light organ|lantern|phosphor/.test(text),
		soft: ['Mollusk', 'Cnidarian', 'Annelid', 'Slime Mold', 'Placozoan', 'Chordate', 'Tunicate', 'Sponge', 'Nematode', 'Amphibian'].includes(g) || micro,
		breathes: vert && g !== 'Fish',
		horned: /\bhorns?\b|horned|antler|tusk|narwhal|rhino|hornworm/.test(text),
	};
}

// Body gates: a move matching a pattern needs every listed fact (all matching gates must pass).
const GATES = [
	[/^(GROWL|ROAR|HYPER_VOICE|SCREECH|SING|UPROAR|SNORE|PERISH_SONG|GRASS_WHISTLE|METAL_SOUND|SUPERSONIC|HOWL)$/, 'voiced'],
	[/_TAIL$|^TAIL_WHIP$/, 'tailed'],
	[/^(LEER|GLARE|MEAN_LOOK)$/, 'eyed'],
	[/^(SCARY_FACE|CHARM|SWEET_KISS|LOVELY_KISS)$/, 'faced'],
	[/^FAKE_TEARS$/, (b) => b.vert && !['Fish', 'Amphibian'].includes(b.g)],
	[/^LICK$/, 'tongue'],
	[/FANG/, 'fanged'],
	[/^(BITE|CRUNCH)$/, 'jawed'],
	[/^DOUBLE_SLAP$/, (b) => b.fam === 'primate' || b.cephalopod || /beaver|sea lion|seal|otter|kangaroo|bear|walrus/.test(b.name)],
	[/PUNCH|MASH|SKY_UPPERCUT/, (b) => b.fam === 'primate'],
	[/CHOP|ARM_THRUST|SUBMISSION|BRICK_BREAK|VITAL_THROW/, (b) => b.fam === 'primate' || b.crustacean],
	[/^(EXTREME_SPEED|QUICK_ATTACK|AGILITY)$/, (b) => !b.slow],
	[/^HYPER_FANG$/, 'rodent'],
	[/CLAW|SWIPES|SLASH|SCRATCH|FALSE_SWIPE|SWORDS_DANCE|CRUSH_CLAW/, 'clawed'],
	[/^VICE_GRIP$/, 'pincered'],
	[/^CRABHAMMER$/, 'crustacean'],
	[/^CLAMP$/, 'bivalve'],
	[/PECK/, 'beaked'],
	[/^(WING_ATTACK|STEEL_WING|ROOST|SILVER_WIND)$/, 'winged'],
	[/^FEATHER_DANCE$/, 'feathered'],
	[/KICK/, 'kicker'],
	[/^STOMP$/, (b) => b.heavy && (b.kicker || /bear|sasquatch|ostrich|emu|cassowary|crane|swan/.test(b.name))],
	[/^(STRING_SHOT|SPIDER_WEB)$/, 'silk'],
	[/^(POISON_STING|PIN_MISSILE|TWINEEDLE)$/, (b) => b.stinger || /porcupine|hedgehog|urchin|needle/.test(b.text)],
	[/^(VINE_WHIP|RAZOR_LEAF|LEAF_BLADE|MAGICAL_LEAF|BULLET_SEED|NEEDLE_ARM|FRENZY_PLANT|LEECH_SEED)$/, 'plant'],
	[/^(PETAL_DANCE|AROMATHERAPY)$/, 'flowering'],
	[/^(SYNTHESIS|MORNING_SUN)$/, 'photosynth'],
	[/^INGRAIN$/, 'rooted'],
	[/^(POISON_POWDER|STUN_SPORE|SLEEP_POWDER|COTTON_SPORE|SPORE)$/, 'spores'],
	[/^TAIL_GLOW$/, 'glows'],
	[/^WITHDRAW$/, (b) => /turtle|tortoise|snail|\b(oyster|clam|mussel|scallop)\b|abalone|geoduck|crab|barnacle|isopod|armadillo|horseshoe|ammonite|argonaut|tube worm|christmas tree worm/.test(b.name)],
	[/^(WRAP|BIND|CONSTRICT)$/, (b) => b.fam === 'serpentine' || b.cephalopod || b.soft || b.plant || /eel|hagfish|lamprey|python|vine|ivy/.test(b.name)],
	[/^(ROLLOUT|RAPID_SPIN|ICE_BALL)$/, (b) => /armadillo|pangolin|hedgehog|isopod|pill|millipede|scarab|dung|tardigrade|tun\b|sea urchin|porcupine/.test(b.name) || (b.micro && !b.sessile)],
	[/^FURY_ATTACK$/, (b) => b.beaked || b.horned || b.stinger],
	[/^ACID_ARMOR$/, 'soft'],
	[/^(BULK_UP|DEFENSE_CURL|HEADBUTT)$/, (b) => b.animal && (b.vert || ARTHROPOD.has(b.g))],
	[/^DRAGON_BREATH$/, 'breathes'],
	[/HORN/, 'horned'],
	[/^(DIG|SAND_TOMB)$/, (b) => b.animal || b.rooted],
	[/^(THIEF|COVET|KNOCK_OFF)$/, (b) => b.animal && (b.vert || ARTHROPOD.has(b.g) || b.cephalopod)],
];

/** Whether an organism's body could plausibly make a move (no fangs on plants, no kicks on lobsters). */
function bodyAllows(org, name) {
	const b = body(org);
	if ((b.sessile || b.micro) && HEAVY.test(name) && !(b.micro && !b.sessile && MICRO_OK.has(name))) return false;
	for (const [re, need] of GATES) {
		if (re.test(name) && !(typeof need === 'function' ? need(b) : b[need])) return false;
	}
	return true;
}

// Off-type moves for organisms left with few damaging moves (see levelUpLearnset).
const FILL = ['BITE', 'HEADBUTT', 'ACID', 'SMOG', 'SLUDGE', 'MUD_SLAP', 'WATER_PULSE', 'SHOCK_WAVE', 'SIGNAL_BEAM',
	'ANCIENT_POWER', 'MAGICAL_LEAF', 'ROCK_THROW'];

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
	const status = (t) => (STATUS[t] || []).filter((n) => moves[n] && moves[n].power === 0 && !NEVER.has(n) && bodyAllows(org, n));

	// Opener: Scratch for clawed animals, else Tackle; then the first move of its own type at 5.
	const b = body(org);
	const sessile = SESSILE.has(org.group);
	const opener = moves[sessile ? SESSILE_OPENER[org.group] || 'ABSORB'
		: b.clawed && org.group !== 'Bird' ? 'SCRATCH' : FIRST.NORMAL[0]];
	const firstStatus = sessile || b.micro ? ['GROWTH', 'HARDEN'] : status('NORMAL').slice(0, 4);
	const list = [[1, opener.name], [1, firstStatus[h % firstStatus.length]]];
	const firstOk = (n) => n && n !== 'TACKLE' && n !== opener.name && moves[n] && bodyAllows(org, n);
	const ownFirst = types.flatMap((t) => FIRST[t] || []).find(firstOk);
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
	// Organisms whose body rules out most of their types' moves get a few plain ones of other types.
	const fill = FILL.map((n) => moves[n]).filter((m) => m && !chosen.includes(m) && m.name !== opener.name && m.name !== ownFirst && bodyAllows(org, m.name));
	for (let k = 0; chosen.length < 6 && fill.length; k++) chosen.push(fill.splice((h + k) % fill.length, 1)[0]);
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

module.exports = { loadMoves, loadTMHM, loadTutors, levelUpLearnset, bodyAllows, body, hash, NEVER, SESSILE };
