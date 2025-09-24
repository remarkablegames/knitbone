label bar:
    play music "music/bar.ogg" fadein 1.5 volume 0.8
    pause 1

    "Hmm..."
    "Seems like the ice in my glass had succumbed to the warmth..."
    "...it looks just like my life."

    show cg bar
    with dissolve
    pause 0.7

    "Hi, I’m Eden."
    "I’m a psychology major."
    " I got good grades{w=0.2} and was considered to have {i}so much potential."
    eden "...{cps=15}"

    pause 0.5

    eden "{i}But that was years ago...{w=0.2} When I had directions in my life."

    eden "{i}Now? I’m surviving on coffee and three hours of sleep."
    eden "{i}I changed three jobs in just twelve months.{w=0.2} What a record."
    eden "{i}Every “fresh start” only left me more tangled in doubt.{w=0.1} And yeah, I just ended up more lost."
    eden "{i}I don’t even recognize who I am anymore."

    show cg bar at shake
    stop music
    play sound "sfx/chime.ogg"
    "*chimes*"

    pause 0.5
    play sound "sfx/door.ogg"
    "The door opened, but at first, I barely registered it."

    scene black with fade
    pause 0.7
    hide cg bar with dissolve

    "It seems like the vibe shifted, as if someone flipped a switch."
    "So I can’t help but to look..."
    pause 0.1

    play music "music/theme2.ogg" fadein 1 volume 0.4

    scene bg lounge at slow_zoom
    with fade
    pause 0.5

    jump bar_ryohei_entrance


label bar_ryohei_entrance:
    # scene lounge_door_open with fade
    # Ryohei’s entrance

    play sound "sfx/footsteps.ogg"
    show ryohei look at slow_zoom, center
    with dissolve

    "A guy had walked in with an easy confidence, and everyone eyed on him."
    "He smiled at the bartender, waved at someone like they were old friends."
    show ryohei look2 at center

    eden "..."
    eden "{i}So, he’s that kind of guy huh."
    eden "{i}He looked... so put together—assertive and relaxed."
    eden "{i}And his shirt—that probably cost more than my rent, yet he wore it so casually."
    eden "{i}Everything about him was the opposite of me..."

    show ryohei look at flip, center
    with dissolve
    "He paused at the entrance, scanning the lounge like he was deciding where to sit."

    show ryohei look at unflip, center
    with dissolve
    "I should have looked away, but I didn’t."
    pause 0.5

    show ryohei serious
    eden "!!"
    "And then he saw me, surprised as his eyes locked onto mine."
    pause 0.3

    ryohei laugh "..."
    "He smiled."
    pause 0.4
    hide ryohei

    show eden awkward with dissolve
    "That got me holding my breath."
    "I quickly forced a polite smile even with my heart racing."
    "There was something oddly familiar about him... but I couldn’t figure it out."

    pause 0.5
    hide eden with fade

    play sound "sfx/footsteps.ogg"
    "I heard footsteps approaching me slowly."

    pause 0.2
    show ryohei neutral at left with dissolve
    show eden neutral at right with dissolve

    eden "{i}Why is he standing right here?"
    pause 0.2

    ryohei "Hey... Eden?"
    eden awkward "!!"
    pause 0.2

    eden "You know my name?"
    show ryohei smirk2 with dissolve
    "My confusion must’ve shown on my face because he chuckled."

    ryohei neutral "It’s me, Ryohei Damien. Haha, sorry. You might not remember me."

    pause 0.5
    eden "{i}Oh."
    pause 0.5

    scene bg lounge at slight_shake
    eden "{i}It’s you."
    pause 1

    jump bar_flashback


label bar_flashback:
    # Flashback voiceover
    scene black with fade
    pause 0.5

    pause 1.0
    eden "That hit me."

    eden "Ryohei..."
    eden "The Ryohei Damien."

    eden "We were in the same department back in college."
    eden "We were both psychology majors although our paths never crossed deeply."
    eden "He was popular. He was effortlessly charming."
    eden "The kind of guy who made everyone feel seen, even when he probably didn’t know half of their names."
    eden "I never expected to be on his radar."
    eden "We shared a few lectures, maybe a group project once, but I was always the quiet one. I was the guy people tend to forget."

    eden "{i}But I remembered him."
    eden "{i}Goddamn, I think I remembered him more than I should."

    eden "People wouldn’t shut up about him."
    eden "The rumors that he got scouted by some research lab."
    eden "The times he stood in front of the class with that calm presence. He’s always sure of himself."

    pause 0.7

    jump bar_talk


label bar_talk:
    scene cg bar talk
    with dissolve

    "And yet, here he is."
    "Sitting across from me in this nearly empty lounge, grinning like we were old friends."
    "He even did it without asking like it was the most natural thing."
    "Like I wasn’t just another forgotten face from his past."
    "...{w=0.2} He’s probably only talking to me out of pity."

    pause 0.3
    eden "Of course I remember you. You were basically famous, Ryohei."

    # Add some pause or animation if needed here to show warmth or irony.

    "It made him laugh and he didn’t even try to deny it."

    ryohei "I’m really glad we ran into each other again."
    ryohei "Hey, do you remember that time you made Professor Sam trip over his own lecture notes? Still one of the funniest moments ever."
    eden "You...{w=0.2} remembered that?"
    ryohei "Honestly, that’s one of my favorite memories from back in college."

    pause 0.3
    "And for the first time in a long while...{w=0.2} I didn’t feel like a total failure."
    "Maybe this is what I needed after all."

    pause 0.5

    "I just need a reminder that I hadn’t vanished completely."

    jump timer_example


label timer_example:
    $ countdown.start(seconds=5, jump="end")

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
