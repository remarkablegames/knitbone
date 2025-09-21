default trust = 0
default karmic = 0
default karmic_awareness = 0


init python:
    renpy.music.register_channel("sfx", "sound", loop=False)


label splashscreen:

    # TODO: logo
    scene bg logo with Dissolve(1)
    pause 1

    scene black with fade
    pause 1

    # TODO: content warning
    show SplashInfo __("Content Warning") with Dissolve(1)
    pause 5

    hide SplashInfo with Dissolve(1)
    pause 1

    return


label start:

    stop music fadeout 1.5
    pause 1

    show text "{size=75}{color=#ccc}KnitBone" with dissolve
    pause 2

    scene black with dissolve
    pause 2

    jump prologue
