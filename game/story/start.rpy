default trust = 0
default karmic = 0
default karmic_awareness = 0

screen prestart_screen:
    timer 1.0 action Start()

label prestart_label:
    scene menu_image_blur
    $ renpy.call_screen("prestart_screen")
    return

label splashscreen:
    #play music the_end
    scene bg logo with Dissolve(1)
    $ renpy.pause(1.0)
    scene black with fade

    stop music
    window hide(None)
    pause 1.0
    show SplashInfo __("Content Warning") with Dissolve(1.0)
    pause 6
    hide SplashInfo with Dissolve(1.0)
    pause 1.0

    return
