@ NOTE: The brailleformat macro in this file is leftover from RS.
@       The numbers are simply skipped over. If you'd like to omit
@       this macro you must also stop it from skipping over this
@       section by editing ScrCmd_braillemessage.
Underwater_SealedChamber_Braille_GoUpHere:
	brailleformat 4, 6, 26, 13, 7, 9
	.braille "GO UP HERE.$"

SealedChamber_OuterRoom_Braille_ABC:
	brailleformat 7, 6, 21, 13, 10, 9
	.braille "ABC$"

SealedChamber_OuterRoom_Braille_GHI:
	brailleformat 7, 6, 21, 13, 10, 9
	.braille "GHI$"

SealedChamber_OuterRoom_Braille_MNO:
	brailleformat 7, 6, 21, 13, 10, 9
	.braille "MNO$"

SealedChamber_OuterRoom_Braille_TUV:
	brailleformat 7, 6, 21, 13, 10, 9
	.braille "TUV$"

SealedChamber_OuterRoom_Braille_DEF:
	brailleformat 7, 6, 21, 13, 10, 9
	.braille "DEF$"

SealedChamber_OuterRoom_Braille_JKL:
	brailleformat 7, 6, 21, 13, 10, 9
	.braille "JKL$"

SealedChamber_OuterRoom_Braille_PQRS:
	brailleformat 7, 6, 21, 13, 10, 9
	.braille "PQRS$"

SealedChamber_OuterRoom_Braille_Period:
	brailleformat 9, 6, 19, 13, 12, 9
	.braille ".$"

SealedChamber_OuterRoom_Braille_WXYZ:
	brailleformat 7, 6, 21, 13, 10, 9
	.braille "WXYZ$"

SealedChamber_OuterRoom_Braille_Comma:
	brailleformat 9, 6, 19, 13, 12, 9
	.braille ",$"

SealedChamber_OuterRoom_Braille_DigHere:
	brailleformat 7, 4, 23, 15, 10, 7
	.braille "DIG HERE.$"

SealedChamber_InnerRoom_Braille_FirstWailordLastRelicanth:
	brailleformat 0, 0, 29, 19, 3, 3
	.braille "FIRST COMES\n"
	.braille "GRAY WHALE.\n"
	.braille "LAST COMES\n"
	.braille "DOLPHIN.$"

SealedChamber_InnerRoom_Braille_InThisCaveWeHaveLived:
	brailleformat 2, 0, 26, 19, 5, 3
	.braille "IN THIS\n"
	.braille "CAVE WE\n"
	.braille "HAVE\n"
	.braille "LIVED.$"

SealedChamber_InnerRoom_Braille_WeOweAllToThePokemon:
	brailleformat 7, 2, 23, 17, 10, 5
	.braille "WE OWE ALL\n"
	.braille "TO THE\n"
	.braille "POKEMON.$"

SealedChamber_InnerRoom_Braille_ButWeSealedThePokemonAway:
	brailleformat 3, 0, 25, 19, 6, 3
	.braille "BUT, WE\n"
	.braille "SEALED THE\n"
	.braille "POKEMON\n"
	.braille "AWAY.$"

SealedChamber_InnerRoom_Braille_WeFearedIt:
	brailleformat 5, 6, 25, 13, 8, 9
	.braille "WE FEARED IT.$"

SealedChamber_InnerRoom_Braille_ThoseWithCourageHope:
	brailleformat 6, 0, 24, 19, 9, 3
	.braille "THOSE WITH\n"
	.braille "COURAGE,\n"
	.braille "THOSE WITH\n"
	.braille "HOPE.$"

SealedChamber_InnerRoom_Braille_OpenDoorEternalPokemonWaits:
	brailleformat 3, 2, 27, 17, 6, 5
	.braille "OPEN A DOOR.\n"
	.braille "AN ETERNAL\n"
	.braille "POKEMON\n"
	.braille "WAITS.$"

DesertRuins_Braille_UseRockSmash:
	brailleformat 1, 0, 27, 19, 4, 3
	.braille "LEFT, LEFT,\n"
	.braille "DOWN, DOWN.\n"
	.braille "THEN, USE\n"
	.braille "ROCK SMASH.$"

IslandCave_Braille_RunLapAroundWall:
	brailleformat 5, 0, 25, 19, 8, 3
	.braille "STAY CLOSE\n"
	.braille "TO THE WALL.\n"
	.braille "RUN AROUND\n"
	.braille "ONE LAP.$"

AncientTomb_Braille_ShineInTheMiddle:
	brailleformat 3, 0, 25, 19, 6, 3
	.braille "THOSE WHO\n"
	.braille "INHERIT OUR\n"
	.braille "WILL, SHINE\n"
	.braille "IN THE MIDDLE.$"

@ Living Atlas: [Stand-in] Burgess Shale survey notes shown instead of the braille inscriptions
@ (the braille alphabet panels in the outer room stay as wall decoration).
Underwater_SealedChamber_Braille_GoUpHere_Note::
	.string "Survey note, scratched into the rock:\n"
	.string "“Surface here.”$"

SealedChamber_OuterRoom_Braille_DigHere_Note::
	.string "Survey note, scratched into the rock:\n"
	.string "“Dig here.”$"

SealedChamber_InnerRoom_Braille_FirstWailordLastRelicanth_Note::
	.string "Survey note: “Lead your party with a\n"
	.string "GRAY WHALE. Bring a DOLPHIN last.”$"

SealedChamber_InnerRoom_Braille_InThisCaveWeHaveLived_Note::
	.string "Survey note: “Our party camped in this\n"
	.string "cave for three summers.”$"

SealedChamber_InnerRoom_Braille_WeOweAllToThePokemon_Note::
	.string "Survey note: “Everything we learned\n"
	.string "here, we owe to the shale.”$"

SealedChamber_InnerRoom_Braille_ButWeSealedThePokemonAway_Note::
	.string "Survey note: “But we sealed our\n"
	.string "strangest finds away behind the walls.”$"

SealedChamber_InnerRoom_Braille_WeFearedIt_Note::
	.string "Survey note: “No one back home would\n"
	.string "have believed them.”$"

SealedChamber_InnerRoom_Braille_ThoseWithCourageHope_Note::
	.string "Survey note: “Whoever reads this, come\n"
	.string "with patience and care.”$"

SealedChamber_InnerRoom_Braille_OpenDoorEternalPokemonWaits_Note::
	.string "Survey note: “Open the doors. Life from\n"
	.string "half a billion years ago is waiting.”$"

DesertRuins_Braille_UseRockSmash_Note::
	.string "Survey note: “Two paces left, two paces\n"
	.string "down. Then break the rock with ROCK\l"
	.string "SMASH.”$"

IslandCave_Braille_RunLapAroundWall_Note::
	.string "Survey note: “Keep close to the wall\n"
	.string "and walk one full lap.”$"

AncientTomb_Braille_ShineInTheMiddle_Note::
	.string "Survey note: “Whoever follows us: let a\n"
	.string "light shine in the middle of the room.”$"

