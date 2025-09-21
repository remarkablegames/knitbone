default trust = 0
default karmic = 0
default karmic_awareness = 0


init python:
    renpy.music.register_channel("sfx", "sound", loop=False)


label splashscreen:

    scene bg splashscreen with Dissolve(1)
    pause 2

    scene black with fade
    pause 1

    show text "{color=#ccc}⚠️ Content Warning\n\nThis game contains content such as cult, murder, emotional manipulation, body horror, blood, consuming non-edible objects (worms), and alcohol." with Dissolve(1)
    pause 5

    scene black with Dissolve(1)
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
