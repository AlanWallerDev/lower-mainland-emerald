const u16 gTutorMoves[TUTOR_MOVE_COUNT] =
{
    [TUTOR_MOVE_MEGA_PUNCH] = MOVE_MEGA_PUNCH,
    [TUTOR_MOVE_SWORDS_DANCE] = MOVE_SWORDS_DANCE,
    [TUTOR_MOVE_MEGA_KICK] = MOVE_MEGA_KICK,
    [TUTOR_MOVE_BODY_SLAM] = MOVE_BODY_SLAM,
    [TUTOR_MOVE_DOUBLE_EDGE] = MOVE_DOUBLE_EDGE,
    [TUTOR_MOVE_COUNTER] = MOVE_COUNTER,
    [TUTOR_MOVE_SEISMIC_TOSS] = MOVE_SEISMIC_TOSS,
    [TUTOR_MOVE_MIMIC] = MOVE_MIMIC,
    [TUTOR_MOVE_METRONOME] = MOVE_METRONOME,
    [TUTOR_MOVE_SOFT_BOILED] = MOVE_SOFT_BOILED,
    [TUTOR_MOVE_DREAM_EATER] = MOVE_DREAM_EATER,
    [TUTOR_MOVE_THUNDER_WAVE] = MOVE_THUNDER_WAVE,
    [TUTOR_MOVE_EXPLOSION] = MOVE_EXPLOSION,
    [TUTOR_MOVE_ROCK_SLIDE] = MOVE_ROCK_SLIDE,
    [TUTOR_MOVE_SUBSTITUTE] = MOVE_SUBSTITUTE,
    [TUTOR_MOVE_DYNAMIC_PUNCH] = MOVE_DYNAMIC_PUNCH,
    [TUTOR_MOVE_ROLLOUT] = MOVE_ROLLOUT,
    [TUTOR_MOVE_PSYCH_UP] = MOVE_PSYCH_UP,
    [TUTOR_MOVE_SNORE] = MOVE_SNORE,
    [TUTOR_MOVE_ICY_WIND] = MOVE_ICY_WIND,
    [TUTOR_MOVE_ENDURE] = MOVE_ENDURE,
    [TUTOR_MOVE_MUD_SLAP] = MOVE_MUD_SLAP,
    [TUTOR_MOVE_ICE_PUNCH] = MOVE_ICE_PUNCH,
    [TUTOR_MOVE_SWAGGER] = MOVE_SWAGGER,
    [TUTOR_MOVE_SLEEP_TALK] = MOVE_SLEEP_TALK,
    [TUTOR_MOVE_SWIFT] = MOVE_SWIFT,
    [TUTOR_MOVE_DEFENSE_CURL] = MOVE_DEFENSE_CURL,
    [TUTOR_MOVE_THUNDER_PUNCH] = MOVE_THUNDER_PUNCH,
    [TUTOR_MOVE_FIRE_PUNCH] = MOVE_FIRE_PUNCH,
    [TUTOR_MOVE_FURY_CUTTER] = MOVE_FURY_CUTTER,
};

#define TUTOR(move) (1u << (TUTOR_##move))

static const u32 sTutorLearnsets[] =
{
    [SPECIES_NONE]             = (0),

    [SPECIES_BULBASAUR]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_IVYSAUR]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_VENUSAUR]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CHARMANDER]       = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CHARMELEON]       = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CHARIZARD]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SQUIRTLE]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_WARTORTLE]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_DYNAMIC_PUNCH)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_BLASTOISE]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CATERPIE]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_METAPOD]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_BUTTERFREE]       = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_WEEDLE]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_KAKUNA]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_BEEDRILL]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_PIDGEY]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_PIDGEOTTO]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_PIDGEOT]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_RATTATA]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_RATICATE]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SPEAROW]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_FEAROW]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_EKANS]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ARBOK]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_PIKACHU]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_RAICHU]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SANDSHREW]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SANDSLASH]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_NIDORAN_F]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_NIDORINA]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_NIDOQUEEN]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_NIDORAN_M]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_NIDORINO]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_NIDOKING]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CLEFAIRY]         = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_CLEFABLE]         = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_VULPIX]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_NINETALES]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_JIGGLYPUFF]       = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_WIGGLYTUFF]       = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_ZUBAT]            = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GOLBAT]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ODDISH]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GLOOM]            = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_VILEPLUME]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_PARAS]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_PARASECT]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_VENONAT]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_VENOMOTH]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_DIGLETT]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DUGTRIO]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MEOWTH]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_PERSIAN]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_PSYDUCK]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GOLDUCK]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MANKEY]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_PRIMEAPE]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GROWLITHE]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ARCANINE]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_POLIWAG]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_POLIWHIRL]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_POLIWRATH]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ABRA]             = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_KADABRA]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ALAKAZAM]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MACHOP]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_MACHOKE]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MACHAMP]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_BELLSPROUT]       = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_WEEPINBELL]       = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_VICTREEBEL]       = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_TENTACOOL]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_TENTACRUEL]       = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GEODUDE]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_GRAVELER]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GOLEM]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_PONYTA]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_RAPIDASH]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SLOWPOKE]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SLOWBRO]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MAGNEMITE]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_MAGNETON]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_FARFETCHD]        = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_DODUO]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DODRIO]           = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_SEEL]             = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DEWGONG]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GRIMER]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MUK]              = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SHELLDER]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CLOYSTER]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GASTLY]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_HAUNTER]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GENGAR]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_ONIX]             = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DROWZEE]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_HYPNO]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_KRABBY]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_KINGLER]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_VOLTORB]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ELECTRODE]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_EXEGGCUTE]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_EXEGGUTOR]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CUBONE]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MAROWAK]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_HITMONLEE]        = (TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_HITMONCHAN]       = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LICKITUNG]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_KOFFING]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_WEEZING]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_RHYHORN]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_RHYDON]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CHANSEY]          = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_TANGELA]          = (TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_KANGASKHAN]       = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_HORSEA]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SEADRA]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GOLDEEN]          = (TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SEAKING]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_STARYU]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_STARMIE]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MR_MIME]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SCYTHER]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_JYNX]             = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ELECTABUZZ]       = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MAGMAR]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_PINSIR]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_TAUROS]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_MAGIKARP]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GYARADOS]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LAPRAS]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DITTO]            = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_EEVEE]            = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_VAPOREON]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_JOLTEON]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_FLAREON]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_PORYGON]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_OMANYTE]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_OMASTAR]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_KABUTO]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_KABUTOPS]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_AERODACTYL]       = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SNORLAX]          = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_ARTICUNO]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ZAPDOS]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MOLTRES]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DRATINI]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DRAGONAIR]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_DRAGONITE]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MEWTWO]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MEW]              = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_DYNAMIC_PUNCH)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CHIKORITA]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_BAYLEEF]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MEGANIUM]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CYNDAQUIL]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_QUILAVA]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_TYPHLOSION]       = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_TOTODILE]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CROCONAW]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_FERALIGATR]       = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SENTRET]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_FURRET]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_DYNAMIC_PUNCH)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_HOOTHOOT]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_NOCTOWL]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_LEDYBA]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_LEDIAN]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_SPINARAK]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_ARIADOS]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_CROBAT]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CHINCHOU]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LANTURN]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_PICHU]            = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CLEFFA]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_IGGLYBUFF]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_TOGEPI]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_TOGETIC]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_NATU]             = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_XATU]             = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MAREEP]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_FLAAFFY]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_AMPHAROS]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_BELLOSSOM]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MARILL]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_AZUMARILL]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SUDOWOODO]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_POLITOED]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_HOPPIP]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SKIPLOOM]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_JUMPLUFF]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_AIPOM]            = (TUTOR(MOVE_MEGA_PUNCH)
                                | TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_SUNKERN]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SUNFLORA]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_YANMA]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_WOOPER]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_QUAGSIRE]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ESPEON]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_UMBREON]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MURKROW]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SLOWKING]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MISDREAVUS]       = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_UNOWN]            = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_WOBBUFFET]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GIRAFARIG]        = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_PINECO]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_FORRETRESS]       = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DUNSPARCE]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GLIGAR]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_STEELIX]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_SNUBBULL]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_GRANBULL]         = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_QWILFISH]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SCIZOR]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_SHUCKLE]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_HERACROSS]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SNEASEL]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_TEDDIURSA]        = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_URSARING]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_SLUGMA]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MAGCARGO]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SWINUB]           = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_PILOSWINE]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CORSOLA]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_REMORAID]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_OCTILLERY]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DELIBIRD]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MANTINE]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SKARMORY]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_HOUNDOUR]         = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_HOUNDOOM]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_KINGDRA]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_PHANPY]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_DONPHAN]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_PORYGON2]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_STANTLER]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_SMEARGLE]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_TYROGUE]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_HITMONTOP]        = (TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SMOOCHUM]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ELEKID]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MAGBY]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MILTANK]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_BLISSEY]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_RAIKOU]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ENTEI]            = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SUICUNE]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LARVITAR]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_PUPITAR]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_TYRANITAR]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LUGIA]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_HO_OH]            = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CELEBI]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_TREECKO]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GROVYLE]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SCEPTILE]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_TORCHIC]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_COMBUSKEN]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_BLAZIKEN]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MUDKIP]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MARSHTOMP]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SWAMPERT]         = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_POOCHYENA]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MIGHTYENA]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ZIGZAGOON]        = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_LINOONE]          = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_WURMPLE]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_SILCOON]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_BEAUTIFLY]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_CASCOON]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_DUSTOX]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_LOTAD]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LOMBRE]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LUDICOLO]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SEEDOT]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_NUZLEAF]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_SHIFTRY]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_NINCADA]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_NINJASK]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_SHEDINJA]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_TAILLOW]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SWELLOW]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SHROOMISH]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_BRELOOM]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SPINDA]           = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_WINGULL]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_PELIPPER]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SURSKIT]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_MASQUERAIN]       = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_WAILMER]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_WAILORD]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SKITTY]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DELCATTY]         = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_KECLEON]          = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_BALTOY]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CLAYDOL]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_NOSEPASS]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_TORKOAL]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SABLEYE]          = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_BARBOACH]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_WHISCASH]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LUVDISC]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CORPHISH]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CRAWDAUNT]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_FEEBAS]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MILOTIC]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CARVANHA]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_SHARPEDO]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_TRAPINCH]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_VIBRAVA]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_FLYGON]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MAKUHITA]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_HARIYAMA]         = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_ELECTRIKE]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MANECTRIC]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_NUMEL]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_CAMERUPT]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SPHEAL]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_SEALEO]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_WALREIN]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CACNEA]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CACTURNE]         = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SNORUNT]          = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_GLALIE]           = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_LUNATONE]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SOLROCK]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_AZURILL]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SPOINK]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_GRUMPIG]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_PLUSLE]           = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_MINUN]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MAWILE]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MEDITITE]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_MEDICHAM]         = (TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SWABLU]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_ALTARIA]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_WYNAUT]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DUSKULL]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_DUSCLOPS]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ROSELIA]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SLAKOTH]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_VIGOROTH]         = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_SLAKING]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_GULPIN]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_SWALOT]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ICY_WIND)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_TROPIUS]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_WHISMUR]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LOUDRED]          = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_EXPLOUD]          = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_CLAMPERL]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_MUD_SLAP)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_HUNTAIL]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GOREBYSS]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ABSOL]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SHUPPET]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_BANETTE]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SEVIPER]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ZANGOOSE]         = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_RELICANTH]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ARON]             = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LAIRON]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_AGGRON]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CASTFORM]         = (TUTOR(MOVE_MEGA_KICK)
                                | TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_VOLBEAT]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_DYNAMIC_PUNCH)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_ILLUMISE]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_LILEEP]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_CRADILY]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_ANORITH]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_ARMALDO]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_RALTS]            = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_KIRLIA]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GARDEVOIR]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_BAGON]            = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_SHELGON]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_SALAMENCE]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_BELDUM]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_METANG]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_METAGROSS]        = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_REGIROCK]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_REGICE]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_FURY_CUTTER)),

    [SPECIES_REGISTEEL]        = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_EXPLOSION)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)
                                | TUTOR(MOVE_SWIFT)),

    [SPECIES_KYOGRE]           = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_GROUDON]          = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_RAYQUAZA]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LATIAS]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_ROCK_SLIDE)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_ROLLOUT)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_LATIOS]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_JIRACHI]          = (TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_DEOXYS]           = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_DREAM_EATER)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

    [SPECIES_CHIMECHO]         = (TUTOR(MOVE_BODY_SLAM)
                                | TUTOR(MOVE_DOUBLE_EDGE)
                                | TUTOR(MOVE_COUNTER)
                                | TUTOR(MOVE_SEISMIC_TOSS)
                                | TUTOR(MOVE_MIMIC)
                                | TUTOR(MOVE_SUBSTITUTE)
                                | TUTOR(MOVE_SNORE)
                                | TUTOR(MOVE_ENDURE)
                                | TUTOR(MOVE_SWAGGER)
                                | TUTOR(MOVE_SLEEP_TALK)),

};

