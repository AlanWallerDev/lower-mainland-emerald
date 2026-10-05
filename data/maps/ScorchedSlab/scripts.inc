ScorchedSlab_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, ScorchedSlab_OnTransition
	.byte 0

ScorchedSlab_OnTransition:
	setflag FLAG_LANDMARK_SCORCHED_SLAB
	end


@ Living Atlas: the BURGESS SHALE dig on the bench above the tarn.
ScorchedSlab_EventScript_DigLeader::
	lock
	faceplayer
	goto_if_set FLAG_RECEIVED_SHALE_HARD_STONE, ScorchedSlab_EventScript_DigLeaderAfter
	msgbox ScorchedSlab_Text_DigLeaderWelcome, MSGBOX_DEFAULT
	giveitem ITEM_HARD_STONE
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
	setflag FLAG_RECEIVED_SHALE_HARD_STONE
	msgbox ScorchedSlab_Text_DigLeaderAfter, MSGBOX_DEFAULT
	release
	end

ScorchedSlab_EventScript_DigLeaderAfter::
	msgbox ScorchedSlab_Text_DigLeaderAfter, MSGBOX_DEFAULT
	release
	end

ScorchedSlab_EventScript_Digger::
	msgbox ScorchedSlab_Text_Digger, MSGBOX_NPC
	end

ScorchedSlab_Text_DigLeaderWelcome:
	.string "Welcome to the BURGESS SHALE!\p"
	.string "This slope was the floor of a warm\n"
	.string "sea over 500 million years ago.\p"
	.string "Mud slid off a reef wall and buried\n"
	.string "whole animals at once, soft bodies\l"
	.string "and all. That's why they're so clear.\p"
	.string "CHARLES WALCOTT found these beds\n"
	.string "in 1909, and we still turn up new\l"
	.string "animals every summer.\p"
	.string "Here, a chip of the shale for you.\n"
	.string "It's harder than it looks.$"

ScorchedSlab_Text_DigLeaderAfter:
	.string "HALLUCIGEN walked on its spines, and\n"
	.string "ANOMALO hunted with grasping arms.\p"
	.string "Three more old animals, MARRELLA,\n"
	.string "OPABINIA and PIKAIA, are said to\l"
	.string "sleep in sealed rooms around BC.\p"
	.string "The old survey notes tell how to\n"
	.string "wake them. Read them closely!$"

ScorchedSlab_Text_Digger:
	.string "Careful where you step! Any slab up\n"
	.string "here might hold an animal nobody\l"
	.string "has ever seen.\p"
	.string "The park lets us dig, but visitors\n"
	.string "only look. Every fossil stays on\l"
	.string "the mountain.\p"
	.string "PIKAIA is tiny, but it has a rod\n"
	.string "down its back. It may be one of our\l"
	.string "oldest relatives!$"
