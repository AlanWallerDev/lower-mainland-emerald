SealedChamber_InnerRoom_MapScripts::
	.byte 0

SealedChamber_InnerRoom_EventScript_BrailleBackWall::
	lockall
	msgbox SealedChamber_InnerRoom_Braille_FirstWailordLastRelicanth_Note, MSGBOX_DEFAULT @ Living Atlas: survey note instead of braille
	goto_if_set FLAG_REGI_DOORS_OPENED, SealedChamber_InnerRoom_EventScript_NoEffect
	specialvar VAR_RESULT, CheckRelicanthWailord
	goto_if_eq VAR_RESULT, FALSE, SealedChamber_InnerRoom_EventScript_NoEffect
	fadeoutbgm 0
	playse SE_TRUCK_MOVE
	special DoSealedChamberShakingEffect_Long
	delay 40
	special DoSealedChamberShakingEffect_Short
	playse SE_DOOR
	delay 40
	special DoSealedChamberShakingEffect_Short
	playse SE_DOOR
	delay 40
	special DoSealedChamberShakingEffect_Short
	playse SE_DOOR
	delay 40
	msgbox gText_DoorOpenedFarAway, MSGBOX_DEFAULT
	closemessage
	fadeinbgm 0
	setflag FLAG_REGI_DOORS_OPENED
	releaseall
	end

SealedChamber_InnerRoom_EventScript_NoEffect::
	releaseall
	end

SealedChamber_InnerRoom_EventScript_BrailleStoryPart1::
	lockall
	msgbox SealedChamber_InnerRoom_Braille_InThisCaveWeHaveLived_Note, MSGBOX_DEFAULT @ Living Atlas: survey note instead of braille
	releaseall
	end

SealedChamber_InnerRoom_EventScript_BrailleStoryPart2::
	lockall
	msgbox SealedChamber_InnerRoom_Braille_WeOweAllToThePokemon_Note, MSGBOX_DEFAULT @ Living Atlas: survey note instead of braille
	releaseall
	end

SealedChamber_InnerRoom_EventScript_BrailleStoryPart3::
	lockall
	msgbox SealedChamber_InnerRoom_Braille_ButWeSealedThePokemonAway_Note, MSGBOX_DEFAULT @ Living Atlas: survey note instead of braille
	releaseall
	end

SealedChamber_InnerRoom_EventScript_BrailleStoryPart4::
	lockall
	msgbox SealedChamber_InnerRoom_Braille_WeFearedIt_Note, MSGBOX_DEFAULT @ Living Atlas: survey note instead of braille
	releaseall
	end

SealedChamber_InnerRoom_EventScript_BrailleStoryPart5::
	lockall
	msgbox SealedChamber_InnerRoom_Braille_ThoseWithCourageHope_Note, MSGBOX_DEFAULT @ Living Atlas: survey note instead of braille
	releaseall
	end

SealedChamber_InnerRoom_EventScript_BrailleStoryPart6::
	lockall
	msgbox SealedChamber_InnerRoom_Braille_OpenDoorEternalPokemonWaits_Note, MSGBOX_DEFAULT @ Living Atlas: survey note instead of braille
	releaseall
	end

