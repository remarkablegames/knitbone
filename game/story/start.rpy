default trust = 0
default karmic = 0
default karmic_awareness = 0


label splashscreen:

    # TODO: logo
    scene bg logo with Dissolve(1)
    pause 1.0

    scene black with fade
    pause 1.0

    # TODO: content warning
    show SplashInfo __("Content Warning") with Dissolve(1.0)
    pause 6

    hide SplashInfo with Dissolve(1.0)
    pause 1.0

    return


label start:

    stop music fadeout 1.0

    pause(1)
    show text "KnitBone" with dissolve

    pause(2)
    hide text with dissolve

    scene black
    pause 2.0

    jump prologue
