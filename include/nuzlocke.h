#ifndef GUARD_NUZLOCKE_H
#define GUARD_NUZLOCKE_H

// Living Atlas: native Nuzlocke rules, chosen once at the start of a new game.
//  - Only the first wild encounter in each area can be caught (once the player carries a jar).
//  - Dupes clause: a species already caught doesn't use up the area. Shiny clause: shinies are always catchable.
//  - Partners that faint (in battle or from field poison) are released once the player has control again.
//    If the whole party falls, the run is over: the save file is erased.
//  - Every catch is nicknamed.

extern bool8 gNuzlockeNewGameChoice;
extern const u8 gText_Birch_Nuzlocke[];
extern const u8 gText_NuzlockeNoCatch[];
extern const u8 gText_NuzlockeReleased[];
extern const u8 gText_NuzlockeRunOver[];

bool8 Nuzlocke_IsEnabled(void);
void Nuzlocke_ApplyNewGameChoice(void);
void Nuzlocke_OnWildBattleStart(void);
bool8 Nuzlocke_CanCatch(void);
void Nuzlocke_OnBattleEnd(void);
bool8 Nuzlocke_IsMonFainted(struct Pokemon *mon);
bool8 Nuzlocke_IsBoxMonFainted(const struct BoxPokemon *mon);
void Nuzlocke_OnFieldPoisonFaint(struct Pokemon *mon);
bool8 Nuzlocke_TryStartRelease(void);
void Nuzlocke_ReleaseNextFallen(void);
void Nuzlocke_GameOver(void);

#endif // GUARD_NUZLOCKE_H
