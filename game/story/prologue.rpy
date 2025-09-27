label prologue:
    "{cps=35}Where did it all go wrong?"
    "{cps=35}Right.{w=0.2}  I shouldn't have had insomnia in the first place."
    pause 0.5
    "You see..."
    "{cps=35}After a few days with no sleep and no direction,{w=0.2}  you get desperate."

    pause 1.5

    scene cg prologue 1 at zoomout
    with fade

    "If I could turn back time..."

    play sound "sfx/tension.ogg"

    scene cg prologue 2
    with dissolve

    pause 0.5

    play sfx "sfx/glass.ogg" volume 0.8

    scene cg prologue 3

    pause 1.5

    "I never would’ve stepped through that door."

    scene black with fade

    jump session1


label timer_example:
    $ countdown.start(seconds=5, jump="ending")

    menu:
        "Play the minigame?"

        "5 candles":
            $ countdown.cancel()
            $ candle = Candle(moves=4, candles=5)
            jump candle_minigame

        "6 candles":
            $ countdown.cancel()
            $ candle = Candle(moves=5, candles=6)
            jump candle_minigame

        "Hypnosis":
            $ countdown.cancel()
            $ slider = Slider(speed=5)
            jump hypnosis_minigame

        "Personality test":
            $ countdown.cancel()
            jump personality_test
