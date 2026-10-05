#include "global.h"
#include "nuzlocke.h"
#include "battle.h"
#include "item.h"
#include "pokedex.h"
#include "pokemon.h"
#include "event_data.h"
#include "mail.h"
#include "main.h"
#include "pokemon_storage_system.h"
#include "save.h"
#include "script.h"
#include "string_util.h"
#include "constants/battle.h"
#include "constants/items.h"

// Battles that never count: tutorials, the opening rescue, links, trainers and the Battle Frontier.
#define NUZLOCKE_IGNORED_BATTLES (BATTLE_TYPE_LINK | BATTLE_TYPE_RECORDED_LINK | BATTLE_TYPE_TRAINER \
                                | BATTLE_TYPE_FIRST_BATTLE | BATTLE_TYPE_WALLY_TUTORIAL \
                                | BATTLE_TYPE_EREADER_TRAINER | BATTLE_TYPE_FRONTIER)

EWRAM_DATA bool8 gNuzlockeNewGameChoice = FALSE;
static EWRAM_DATA bool8 sCanCatchThisBattle = TRUE;

const u8 gText_Birch_Nuzlocke[] = _(
    "One last thing. Some TRAINERS\n"
    "follow the NUZLOCKE code.\p"
    "You may only catch the first organism\n"
    "you meet in each area.\p"
    "Partners that faint are gone for good,\n"
    "and every catch gets a nickname.\p"
    "Will you follow the NUZLOCKE code?");

const u8 gText_NuzlockeReleased[] = _(
    "{STR_VAR_1} has fallen.\n"
    "It leaves your party for good…");

const u8 gText_NuzlockeRunOver[] = _(
    "Every partner in your party has\n"
    "fallen…\p"
    "Your NUZLOCKE run is over.\p"
    "Your save file has been erased.");

const u8 gText_NuzlockeNoCatch[] = _(
    "NUZLOCKE: You already met your\n"
    "organism for this area!{PAUSE_UNTIL_PRESS}");

bool8 Nuzlocke_IsEnabled(void)
{
    return gSaveBlock1Ptr->nuzlockeEnabled;
}

// Called at the end of NewGameInitData, after the save block has been cleared.
void Nuzlocke_ApplyNewGameChoice(void)
{
    gSaveBlock1Ptr->nuzlockeEnabled = gNuzlockeNewGameChoice;
    memset(gSaveBlock1Ptr->nuzlockeEncounters, 0, sizeof(gSaveBlock1Ptr->nuzlockeEncounters));
}

static bool8 IsEncounterUsed(u8 mapsec)
{
    return (gSaveBlock1Ptr->nuzlockeEncounters[mapsec / 8] >> (mapsec % 8)) & 1;
}

static void UseEncounter(u8 mapsec)
{
    gSaveBlock1Ptr->nuzlockeEncounters[mapsec / 8] |= 1 << (mapsec % 8);
}

static bool8 PlayerHasJar(void)
{
    u16 item;

    for (item = FIRST_BALL; item <= LAST_BALL; item++)
    {
        if (CheckBagHasItem(item, 1))
            return TRUE;
    }
    return FALSE;
}

// Called as every battle starts; decides whether this wild organism may be caught.
void Nuzlocke_OnWildBattleStart(void)
{
    u8 mapsec = gMapHeader.regionMapSectionId;
    u16 species;

    sCanCatchThisBattle = TRUE;
    if (!Nuzlocke_IsEnabled() || (gBattleTypeFlags & NUZLOCKE_IGNORED_BATTLES))
        return;

    if (IsMonShiny(&gEnemyParty[0]))
        return; // shiny clause

    if (IsEncounterUsed(mapsec))
    {
        sCanCatchThisBattle = FALSE;
        return;
    }

    if (!PlayerHasJar())
        return; // encounters before the first jar don't count

    species = GetMonData(&gEnemyParty[0], MON_DATA_SPECIES);
    if (GetSetPokedexFlag(SpeciesToNationalPokedexNum(species), FLAG_GET_CAUGHT))
    {
        sCanCatchThisBattle = FALSE; // dupes clause: keep looking
        return;
    }

    UseEncounter(mapsec);
}

bool8 Nuzlocke_CanCatch(void)
{
    return !Nuzlocke_IsEnabled() || sCanCatchThisBattle;
}

// Called as every battle finishes: partners at 0 HP are gone for good.
void Nuzlocke_OnBattleEnd(void)
{
    s32 i;

    if (!Nuzlocke_IsEnabled() || (gBattleTypeFlags & (NUZLOCKE_IGNORED_BATTLES & ~BATTLE_TYPE_TRAINER)))
        return;

    for (i = 0; i < PARTY_SIZE; i++)
    {
        struct Pokemon *mon = &gPlayerParty[i];

        if (GetMonData(mon, MON_DATA_SPECIES) != SPECIES_NONE
         && !GetMonData(mon, MON_DATA_IS_EGG)
         && GetMonData(mon, MON_DATA_HP) == 0)
            mon->box.nuzlockeFainted = TRUE;
    }
}

bool8 Nuzlocke_IsBoxMonFainted(const struct BoxPokemon *mon)
{
    return mon->nuzlockeFainted;
}

bool8 Nuzlocke_IsMonFainted(struct Pokemon *mon)
{
    return mon->box.nuzlockeFainted;
}

// Field poison: a partner that faints on the overworld is lost too.
void Nuzlocke_OnFieldPoisonFaint(struct Pokemon *mon)
{
    if (Nuzlocke_IsEnabled())
        mon->box.nuzlockeFainted = TRUE;
}

static bool8 PartyHasFallen(void)
{
    s32 i;

    for (i = 0; i < PARTY_SIZE; i++)
    {
        if (gPlayerParty[i].box.nuzlockeFainted && GetMonData(&gPlayerParty[i], MON_DATA_SPECIES) != SPECIES_NONE)
            return TRUE;
    }
    return FALSE;
}

// Called from the overworld input loop, once the player has control again after a battle (and any
// post-battle script). Starts the script that releases fallen partners.
bool8 Nuzlocke_TryStartRelease(void)
{
    extern const u8 EventScript_NuzlockeRelease[];

    if (!Nuzlocke_IsEnabled() || !PartyHasFallen())
        return FALSE;
    ScriptContext_SetupScript(EventScript_NuzlockeRelease);
    return TRUE;
}

// special: releases one fallen partner (party first, then any left in the PC from older saves).
// VAR_RESULT: 0 none left, 1 released one (name in STR_VAR_1), 2 every party member has fallen.
void Nuzlocke_ReleaseNextFallen(void)
{
    s32 i, fallen = -1, alive = 0;
    u8 box, pos;

    gSpecialVar_Result = 0;
    for (i = 0; i < PARTY_SIZE; i++)
    {
        struct Pokemon *mon = &gPlayerParty[i];

        if (GetMonData(mon, MON_DATA_SPECIES) == SPECIES_NONE)
            continue;
        if (!mon->box.nuzlockeFainted)
            alive++;
        else if (fallen < 0)
            fallen = i;
    }
    if (fallen >= 0)
    {
        struct Pokemon *mon = &gPlayerParty[fallen];

        if (alive == 0)
        {
            gSpecialVar_Result = 2;
            return;
        }
        GetMonData(mon, MON_DATA_NICKNAME, gStringVar1);
        StringGet_Nickname(gStringVar1);
        if (ItemIsMail(GetMonData(mon, MON_DATA_HELD_ITEM)))
            TakeMailFromMon(mon);
        ZeroMonData(mon);
        CompactPartySlots();
        CalculatePlayerPartyCount();
        gSpecialVar_Result = 1;
        return;
    }
    for (box = 0; box < TOTAL_BOXES_COUNT; box++)
    {
        for (pos = 0; pos < IN_BOX_COUNT; pos++)
        {
            struct BoxPokemon *mon = GetBoxedMonPtr(box, pos);

            if (mon->nuzlockeFainted && GetBoxMonData(mon, MON_DATA_SPECIES) != SPECIES_NONE)
            {
                GetBoxMonData(mon, MON_DATA_NICKNAME, gStringVar1);
                StringGet_Nickname(gStringVar1);
                ZeroBoxMonData(mon);
                gSpecialVar_Result = 1;
                return;
            }
        }
    }
}

// special: the whole party has fallen. The run ends for good: the save file is erased (so an older
// save can't be reloaded) and the game returns to the title screen.
void Nuzlocke_GameOver(void)
{
    ClearSaveData();
    DoSoftReset();
}
