label prologue:
    jump prologue_cg0


label prologue_cg0:
    "{cps=35}It was supposed to be just another night.{/cps}"
    "{cps=35}Just me, and this pathetic quiet corner… in a dimly lit lounge...{/cps}"
    "...A place to vanish into my own thoughts without interruption."
    pause 1.5

    scene cg prologue 1 at slow_zoom, cover_screen
    with fade

    "I didn't know it would turn out like this."
    play sound "sfx/tension.ogg"
    scene cg prologue 2 at cover_screen
    with dissolve
    pause 0.5

    play sfx "sfx/glass.ogg" volume 0.8
    scene cg prologue 3 at cover_screen
    window hide(dissolve)
    pause 1.5

    "That night..."

    #clinkclanksfx
    play music "music/bar.ogg" fadein 1.5 volume 0.8
    scene black at slow_zoom
    with fade

    pause 1.0

    "Hmm."
    "Seems like the ice in my glass had succumbed to the warmth--"
    "...it looks just like my life."

    jump prologue_cg1


label prologue_cg1:
    show cg cafe at cover_screen
    with dissolve
    pause 0.7

    "Hi, I'm Eden."
    "I'm a psychology major."
    " I got good grades{w=0.2} and was considered to have {i}so much potential.{i}"
    _eden_ "......{cps=15}"

    pause 0.5
    
    _eden_ "But that was years ago...That was back when I had directions in my life."

    _eden_ "Now? I'm surviving on coffee and three hours of sleep."
    _eden_ "I changed three jobs in just twelve months.{w=0.2} What a record."
    _eden_ "Every 'fresh start' only left me more tangled in doubt.{w=0.1} And yeah, I just ended up more lost."
    _eden_ "I don't even recognize who I am anymore."

    show cg cafe at shake
    stop music
    play sound "sfx/chime.ogg"
    "*chimes*"

    pause 0.5
    play sound "sfx/door.ogg"
    "The door opened, but at first, I barely registered it."

    scene black with fade
    pause 0.7
    hide cg cafe with dissolve

    "But it seems like the vibe shifted, it was as if someone just flipped a switch."
    "So I can't help but to look--"
    pause 0.1

    play music "music/theme2.ogg" fadein 1.0 volume 0.4

    scene bg lounge at slow_zoom
    with fade
    pause 0.5

    jump prologue_ryohei


label prologue_ryohei:
    # scene lounge_door_open with fade
    # Ryohei’s entrance

    play sound "sfx/footsteps.ogg"
    show ryohei look at slow_zoom, center
    with dissolve

    "A guy had walked in with an easy confidence, and everyone eyed on him."
    "He smiled at the bartender, waved at someone like they were old friends."

    show ryohei look2
    _eden_ "..."
    _eden_ "So, he's that kind of guy huh."
    _eden_ "He looked... so put together-- Assertive and relaxed."
    _eden_ "And his shirt--- That probably cost more than my rent, yet he wore it so casually"
    _eden_ "Everything about him was the opposite of me.."

    show ryohei look
    "He paused at the entrance, scanning the lounge like he was deciding where to sit."
    "I should have looked away, but I didn't."
    pause 0.5

    show ryohei serious with dissolve

    eden "!!"
    "And then he saw me, surprised as his eyes were locking onto mine."
    pause 0.3
    show ryohei laugh with dissolve
    ryohei "…"
    "He smiled."
    pause 0.4
    hide ryohei

    show eden awkward with dissolve
    "That got me holding my breath."
    "I quickly forced a polite smile even with my heart racing."
    "There was something oddly familiar about him… but I couldn't figure it out."

    pause 0.5
    hide eden with fade
    # Ryohei approaches Eden

    "I heard footsteps approaching me slowly."
    
    pause 0.2
    show ryohei neutral at left with dissolve
    show eden neutral at right with dissolve

    _eden_ "Why is he standing right here…?"
    pause 0.2

    show ryohei neutral with dissolve
    ryohei "Hey... Eden?"
    show eden awkward
    eden "!!"

    pause 0.2


    eden "You know my name…?"
    show ryohei smirk2 with dissolve
    "My confusion must've shown on my face because he chuckled."

    show ryohei neutral with dissolve
    ryohei "It's me, Ryohei Damien. Haha, sorry. You might not remember me."

    pause 0.5
    _eden_ "Oh."
    pause 0.5

    scene bg lounge at slight_shake
    _eden_ "It's you."

    pause 1
    hide eden
    hide ryohei

    # Flashback voiceover
    scene black with fade
    pause 0.5

    pause 1.0
    eden "That hit me."

    eden "Ryohei...."
    eden "The Ryohei Damien."

    eden "We were in the same department back in college."
    eden "We were both psychology majors though our paths never crossed deeply."
    eden "He was popular. He was effortlessly charming."
    eden "The kind of guy who made everyone feel seen, even when he probably didn't know half of their names."
    eden "I never expected to be on his radar."
    eden "We shared a few lectures, maybe a group project once, but I was always the quiet one. I was the guy people tend to forget."

    _eden_ "But I remembered him."
    _eden_ "Goddamn, I think I remembered him more than I should."

    eden "People wouldn't shut up about him."
    eden "The rumors that he got scouted by some research lab."
    eden "The times he stood in front of the class with that calm presence. He's always sure of himself."

    pause 0.7
    hide text

    scene cg talk at cover_screen
    with dissolve

    "And yet, here he is."
    "Sitting across from me in this nearly empty lounge,"
    "grinning like we were old friends."
    "He even did it without asking like it was the most natural thing."
    "Like I wasn't just another forgotten face from his past."
    "....He's probably only talking to me out of pity."

    pause 0.3
    eden "Of course I remember you. You were basically famous, Ryohei."

    # Add some pause or animation if needed here to show warmth or irony.

    "It made him laugh and he didn't even try to deny it."

    ryohei "I'm really glad we ran into each other again."
    ryohei "Hey, do you remember that time you made Professor Sam trip over his own lecture notes? Still one of the funniest moments ever."
    eden "You...you remembered that?"
    ryohei "Honestly, that's one of my favorite memories from back in college."
    pause 0.3
    "And for the first time in a long while… I didn't feel like a total failure."

    "Maybe this is what I need after all."

    pause 0.5

    "I just need a reminder that I hadn't vanished completely."

    menu:
        "Play the candle minigame?"

        "Yes":
            jump candle_minigame

        "No":
            pass

    scene black with fade

    return
