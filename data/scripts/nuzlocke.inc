@ Living Atlas: release partners that fell under Nuzlocke rules (started from Nuzlocke_TryStartRelease).
EventScript_NuzlockeRelease::
	lockall
EventScript_NuzlockeReleaseLoop:
	special Nuzlocke_ReleaseNextFallen
	goto_if_eq VAR_RESULT, 2, EventScript_NuzlockeRunOver
	goto_if_eq VAR_RESULT, 0, EventScript_NuzlockeReleaseDone
	msgbox gText_NuzlockeReleased, MSGBOX_DEFAULT
	goto EventScript_NuzlockeReleaseLoop
EventScript_NuzlockeReleaseDone:
	releaseall
	end

EventScript_NuzlockeRunOver:
	msgbox gText_NuzlockeRunOver, MSGBOX_DEFAULT
	special Nuzlocke_GameOver
	releaseall
	end
