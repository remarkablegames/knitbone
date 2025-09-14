default trust = 0
default karmic = 0
default karmic_awareness = 0

label splashscreen:
    scene bg logo with Dissolve(1)
    $ renpy.pause(1.0)
    scene black with fade

    window hide(None)
    pause 1.0

    show SplashInfo __("Content Warning") with Dissolve(1.0)
    pause 6

    hide SplashInfo with Dissolve(1.0)
    pause 1.0

    return

label start:
    jump prologue
