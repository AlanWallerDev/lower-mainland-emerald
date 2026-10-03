#ifndef GUARD_NUZLOCKE_H
#define GUARD_NUZLOCKE_H

// Living Atlas: native Nuzlocke rules, chosen once at the start of a new game.
//  - Only the first wild encounter in each area can be caught (once the player carries a jar).
//  - Dupes clause: a species already caught doesn't use up the area. Shiny clause: shinies are always catchable.
//  - Partners that faint are marked for good; healing, revives, items and the PC can't bring them back.
//  - Every catch is nicknamed.

extern bool8 gNuzlockeNewGameChoice;
extern const u8 gText_Birch_Nuzlocke[];
extern const u8 gText_NuzlockeNoCatch[];

bool8 Nuzlocke_IsEnabled(void);
void Nuzlocke_ApplyNewGameChoice(void);
void Nuzlocke_OnWildBattleStart(void);
bool8 Nuzlocke_CanCatch(void);
void Nuzlocke_OnBattleEnd(void);
bool8 Nuzlocke_IsMonFainted(struct Pokemon *mon);
bool8 Nuzlocke_IsBoxMonFainted(const struct BoxPokemon *mon);

#endif // GUARD_NUZLOCKE_H
