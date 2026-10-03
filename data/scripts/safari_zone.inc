SafariZone_EventScript_OutOfBallsMidBattle::
	setvar VAR_SAFARI_ZONE_STATE, 1
	special ExitSafariMode
	setwarp MAP_ROUTE121_SAFARI_ZONE_ENTRANCE, 2, 5
	end

SafariZone_EventScript_Exit::
	setvar VAR_SAFARI_ZONE_STATE, 1
	special ExitSafariMode
	warp MAP_ROUTE121_SAFARI_ZONE_ENTRANCE, 2, 5
	waitstate
	end

SafariZone_EventScript_RetirePrompt::
	lockall
	msgbox SafariZone_Text_WouldYouLikeToExit, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, SafariZone_EventScript_Retire
	releaseall
	end

SafariZone_EventScript_Retire::
	goto SafariZone_EventScript_Exit

SafariZone_EventScript_TimesUp::
	lockall
	playse SE_DING_DONG
	message SafariZone_Text_TimesUp
	waitmessage
	waitbuttonpress
	releaseall
	goto SafariZone_EventScript_Exit

SafariZone_EventScript_OutOfBalls::
	lockall
	playse SE_DING_DONG
	message SafariZone_Text_OutOfBalls
	waitmessage
	waitbuttonpress
	releaseall
	goto SafariZone_EventScript_Exit

EventScript_PokeBlockFeeder::
	lockall
	special GetPokeblockFeederInFront
	goto_if_ne VAR_RESULT, 0xFFFF, SafariZone_EventScript_PokeblockPresent
	msgbox SafariZone_Text_PlacePokeblockOnFeeder, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, SafariZone_EventScript_ChoosePokeblock
	releaseall
	end

SafariZone_EventScript_ChoosePokeblock::
	fadescreen FADE_TO_BLACK
	special OpenPokeblockCaseOnFeeder
	goto_if_ne VAR_RESULT, 0xFFFF, SafariZone_EventScript_PokeblockPlaced
#ifdef BUGFIX
	releaseall  @ Only gets called from EventScript_PokeBlockFeeder which uses lockall.
#endif
	end

SafariZone_EventScript_PokeblockPlaced::
	message SafariZone_Text_PokeblockWasPlaced
	waitmessage
	waitbuttonpress
	releaseall
	end

SafariZone_EventScript_PokeblockPresent::
	message SafariZone_Text_PokeblockStillHere
	waitmessage
	waitbuttonpress
	releaseall
	end

SafariZone_Text_WouldYouLikeToExit:
	.string "Would you like to exit the SAFARI\n"
	.string "ZONE right now?$"

SafariZone_Text_TimesUp:
	.string "Ding-dong! Time's up!\n"
	.string "Your SAFARI Game is over.$"

SafariZone_Text_OutOfBalls:
	.string "You've run out of SAFARI JARS. Your\n"
	.string "SAFARI Game is over.$"

SafariZone_Text_PlacePokeblockOnFeeder:
	.string "Would you like to place a TREAT on the\n"
	.string "TREAT FEEDER?$"

SafariZone_Text_PokeblockStillHere:
	.string "The {STR_VAR_1} you left\n"
	.string "before is still here.$"

SafariZone_Text_PokeblockWasPlaced:
	.string "The {STR_VAR_1} was placed on the TREAT\n"
	.string "FEEDER.$"

Route121_SafariZoneEntrance_Text_WelcomeToSafariZone:
	.string "Welcome to the BURNS BOG!\p"
	.string "Here, you may witness many kinds of\n"
	.string "organisms rarely seen in BC.\p"
	.string "And, you'll see them in their wild,\n"
	.string "untamed state in natural habitats.\p"
	.string "What's more, we've thrown open the\n"
	.string "gates to NATURALISTS.\p"
	.string "You're encouraged to catch organisms\n"
	.string "for keeps!\p"
	.string "Come in and enjoy the BURNS BOG!$"

Route121_SafariZoneEntrance_Text_WelcomeFirstTime:
	.string "Welcome to the BURNS BOG!\n"
	.string "Is it your first time here?$"

Route121_SafariZoneEntrance_Text_ComeInAndEnjoy:
	.string "Come in and enjoy the BURNS BOG!$"

Route121_SafariZoneEntrance_Text_FirstTimeInfo:
	.string "When you enter the BURNS BOG, you start\n"
	.string "with 30 SAFARI JARS for catching\l"
	.string "organisms.\p"
	.string "The SAFARI Game is over when you run\n"
	.string "out of SAFARI JARS, or when you've\l"
	.string "walked 500 steps.\p"
	.string "Come in and enjoy the BURNS BOG!$"

Route121_SafariZoneEntrance_Text_WouldYouLikeToPlay:
	.string "Welcome to the BURNS BOG!\p"
	.string "All you can catch for just ¥500!\n"
	.string "Would you like to play a SAFARI Game?$"

Route121_SafariZoneEntrance_Text_PlayAnotherTime:
	.string "Okay.\n"
	.string "Please play another time!$"

Route121_SafariZoneEntrance_Text_NotEnoughMoney:
	.string "You don't have enough money.\n"
	.string "Sorry.$"

Route121_SafariZoneEntrance_Text_ThatWillBe500Please:
	.string "That will be ¥500, please.$"

Route121_SafariZoneEntrance_Text_HereAreYourSafariBalls:
	.string "Here are your SAFARI JARS.$"

Route121_SafariZoneEntrance_Text_Received30SafariBalls:
	.string "{PLAYER} received 30 SAFARI JARS.$"

Route121_SafariZoneEntrance_Text_PleaseEnjoyYourself:
	.string "We'll let you know when your game\n"
	.string "is over.\p"
	.string "So, until then, enjoy yourself, please!\n"
	.string "Off you go on your wild excursion!$"

Route121_SafariZoneEntrance_Text_PCIsFull:
	.string "Excuse me!\n"
	.string "Your PC BOX is full.$"

Route121_SafariZoneEntrance_Text_YouNeedPokeblockCase:
	.string "Excuse me! You seem to be without a\n"
	.string "TREAT CASE.\p"
	.string "Your SAFARI Game will be much more\n"
	.string "fruitful if you use TREATS.\p"
	.string "Please come back with a TREAT CASE.\p"
	.string "You may obtain a TREAT CASE from the\n"
	.string "VANCOUVER CONTEST HALL.$"

SafariZone_South_Text_StillHaveTimeExit:
	.string "You still have time left. Would you like\n"
	.string "to exit the BURNS BOG now?$"

SafariZone_South_Text_EnjoyTheRestOfYourAdventure:
	.string "Please enjoy the rest of your wild\n"
	.string "adventure!$"

SafariZone_South_Text_ExitEarlyThankYouForPlaying:
	.string "Okay.\p"
	.string "I'll take back your remaining SAFARI\n"
	.string "JARS.\p"
	.string "Thank you for playing.\n"
	.string "We hope to see you again.$"

SafariZone_South_Text_GoodLuck:
	.string "Good luck!\p"
	.string "If you need anything, don't hesitate\n"
	.string "to tell me, please!$"

SafariZone_South_Text_Boy:
	.string "Did you know?\p"
	.string "If you put a TREAT in that square box,\n"
	.string "organisms gather around.$"

SafariZone_South_Text_Man:
	.string "I want to keep going deeper, but I\n"
	.string "forgot to bring a BIKE.\p"
	.string "Something tells me that rare organisms\n"
	.string "live in the outlying areas.$"

SafariZone_Southwest_Text_Woman:
	.string "Sometimes, when I toss a TREAT at an\n"
	.string "organism, it gets ignored.\p"
	.string "Do organisms have likes and dislikes\n"
	.string "about what they eat?$"

SafariZone_Northwest_Text_Man:
	.string "Gasp… Gasp…\n"
	.string "I…made it out here…but…\p"
	.string "I'm exhausted… I don't have the\n"
	.string "energy to catch organisms…$"

SafariZone_North_Text_Fisherman:
	.string "I'm on a mission to find AQUA\n"
	.string "organisms you don't see in BC.\p"
	.string "Do you have any idea where the lake is?$"

SafariZone_North_Text_Man:
	.string "I'm going to catch a lot of rare\n"
	.string "organisms here and trade them with my\l"
	.string "friends!$"

SafariZone_South_Text_Youngster:
	.string "I put a TREAT on the TREAT FEEDER. But\n"
	.string "it seems to have disappeared.\p"
	.string "I guess organisms must have eaten it\n"
	.string "without me noticing.$"

Route121_SafariZoneEntrance_Text_TrainerTip:
	.string "BURNS BOG TRAINER TIP!\p"
	.string "Throw TREATS at wild organisms to make\n"
	.string "them less likely to flee.$"

SafariZone_Southwest_Text_RestHouseSign:
	.string "“Relieve your tired feet.”\n"
	.string "REST HOUSE$"

SafariZone_RestHouse_Text_Youngster:
	.string "I don't have any TREATS, but I caught a\n"
	.string "good number of organisms.\p"
	.string "You can improve your chances of making\n"
	.string "a catch by getting closer to them\l"
	.string "before throwing a SAFARI JAR.$"

SafariZone_RestHouse_Text_PsychicM:
	.string "If you use TREATS, wild organisms won't\n"
	.string "be so quick to run away.\p"
	.string "It's not much use to give TREATS to\n"
	.string "organisms that don't flee easily.$"

SafariZone_RestHouse_Text_FatMan:
	.string "If you put a TREAT on the FEEDER,\n"
	.string "organisms are attracted to it.\p"
	.string "I think organisms with the same sort of\n"
	.string "nature are drawn by a certain TREAT.$"

SafariZone_South_Text_AreaOffLimits1:
	.string "This area is still under construction.\n"
	.string "It's off-limits, sorry!$"

SafariZone_Southeast_Text_ExpansionIsFinished:
	.string "The BURNS BOG's expansion project\n"
	.string "is finished now.\p"
	.string "We hope you will enjoy the new area.$"

SafariZone_South_Text_AreaOffLimits2:
	.string "This area is still under construction.\n"
	.string "It's off-limits, sorry!$"

SafariZone_Southeast_Text_LittleGirl:
	.string "Wow! Whee! I haven't seen any of these\n"
	.string "organisms before!$"

SafariZone_Southeast_Text_FatMan:
	.string "The organisms in this area are all new\n"
	.string "to me.\p"
	.string "And I'm allowed to catch these rare\n"
	.string "organisms! Too cool!$"

SafariZone_Southeast_Text_RichBoy:
	.string "The organisms around here seem to be\n"
	.string "from somewhere other than BC.$"

SafariZone_Northeast_Text_Boy:
	.string "I only have a couple SAFARI JARS left.\p"
	.string "I'm having a hard time trying to\n"
	.string "decide what I should catch.$"

SafariZone_Northeast_Text_Woman:
	.string "I heard that you can see MOON JELLY\n"
	.string "here. Where might one be?$"

SafariZone_Northeast_Text_Girl:
	.string "Oh, boo!\n"
	.string "I can't seem to catch anything!\p"
	.string "I'll end up wasting the admission\n"
	.string "price if I don't catch something!$"
