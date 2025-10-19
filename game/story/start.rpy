default trust = 0


init python:
    renpy.music.register_channel("sfx", "sound", loop=False)


label splashscreen:

    scene bg splashscreen with Dissolve(1)
    pause 2

    scene black with fade
    pause 1

    show text "{color=#ddd}⚠️ Content Warning\n\nThis game contains content such as cult, murder, emotional manipulation, body horror, blood, flashing lights, and jumpscares." with Dissolve(1.5)
    pause 8

    scene black with Dissolve(1.5)
    pause 1

    return


label start:

    stop music fadeout 2
    queue music "music/terror.ogg" fadein 0.5 volume 0.9
    pause 1

    show text "{size=75}{color=#ccc}KnitBone" with dissolve
    pause 2

    scene black with dissolve
    pause 1

    jump prologue
