OldaleTown_House2_MapScripts::
	.byte 0

OldaleTown_House2_EventScript_Woman::
	msgbox OldaleTown_House2_Text_PokemonLevelUp, MSGBOX_NPC
	end

OldaleTown_House2_EventScript_Man::
	msgbox OldaleTown_House2_Text_YoullGoFurtherWithStrongPokemon, MSGBOX_NPC
	end

OldaleTown_House2_Text_PokemonLevelUp:
	.string "When battle, they eventually level up\n"
	.string "and become stronger.$"

OldaleTown_House2_Text_YoullGoFurtherWithStrongPokemon:
	.string "If the organisms with you become\n"
	.string "stronger, you'll be able to go farther\l"
	.string "away from here.$"

