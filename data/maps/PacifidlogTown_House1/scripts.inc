PacifidlogTown_House1_MapScripts::
	.byte 0

PacifidlogTown_House1_EventScript_Man::
	msgbox PacifidlogTown_House1_Text_RegiStory, MSGBOX_NPC
	end

PacifidlogTown_House1_EventScript_Woman::
	msgbox PacifidlogTown_House1_Text_SixDotsOpenThreeDoors, MSGBOX_NPC
	end

PacifidlogTown_House1_Text_RegiStory:
	.string "In BC, there are three organisms older\n"
	.string "than the mountains, from the age of the\l"
	.string "BURGESS SHALE.\p"
	.string "Each of them is said to hide away deep\n"
	.string "inside a sealed chamber.\p"
	.string "That's the story I heard when I was\n"
	.string "just a little kid.$"

PacifidlogTown_House1_Text_SixDotsOpenThreeDoors:
	.string "“Six dots open three doors.”\p"
	.string "Grandpa used to say that, but I don't\n"
	.string "know what he meant.$"

