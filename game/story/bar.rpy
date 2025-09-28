label bar:
    play music "music/bar.ogg" fadein 3 volume 0.7
    pause 1

    eden "{cps=10}Hmm..."
    play sound "sfx/ice.ogg" volume 0.6
    eden "Seems like the ice in my glass had succumbed to the warmth..."
    eden "...it looks just like my life."

    show cg bar
    with dissolve
    pause 0.7

    "My name’s Eden.{w=0.5} I’m a Psychology major."
    "Voted as “Most Likely to Succeed”."
    eden "{cps=10}..."

    pause 0.5

    eden "{i}But that was years ago...{w=0.2} When I had directions in my life."

    eden "{i}Now?{w=0.3} I’m surviving on coffee with no sleep."
    eden "{i}I changed three jobs in just twelve months."
    eden "{i}Every “fresh start” only left me more tangled in doubt.{w=0.2} And yeah, I just ended up more lost."

    "{cps=10}..."
    pause 1

    eden "{i}I don’t even recognize who I am anymore."

    show cg bar at shake
    stop music
    play sound "sfx/chime.ogg" volume 0.8
    "{i}*chimes*"

    pause 0.5
    play sound "sfx/door.ogg" volume 1.1
    "The door opened, but at first, I barely registered it."

    scene black with fade
    pause 0.7
    hide cg bar with dissolve

    "It seems like the vibe shifted, as if someone flipped a switch."
    "So I can’t help but to look..."
    pause 0.1

    play music "music/theme2.ogg" fadein 1 volume 0.4

    scene bg lounge at zoomout
    with fade
    pause 0.5

    jump bar_ryohei_entrance


label bar_ryohei_entrance:
    # scene lounge_door_open with fade
    # Ryohei’s entrance

    play sound "sfx/footsteps.ogg"
    show ryohei look at zoomout, center
    with dissolve

    "A guy had walked in with an easy confidence,{w=0.1} and everyone eyed on him."
    "He smiled at the bartender,{w=0.1} waved at someone like they were old friends."
    show ryohei look2 at center

    eden "{cps=10}..."
    eden "{i}So,{w=0.1} he’s that kind of guy huh."
    eden "{i}He looked...{w=0.3} so put together — assertive and relaxed."
    eden "{i}And his shirt —{w=0.3} that probably cost more than my rent,{w=0.1} yet he wore it so casually."
    eden "{i}Everything about him was the opposite of me..."

    show ryohei look at flip, center
    with dissolve
    "He paused at the entrance,{w=0.1} scanning the lounge like he was deciding where to sit."

    show ryohei look at unflip, center
    with dissolve
    "I should have looked away,{w=0.1} but I didn’t."
    pause 0.5

    show ryohei serious
    eden "!!"
    "And then he saw me,{w=0.1} surprised as his eyes locked onto mine."
    pause 0.3

    ryohei laugh "..."
    "He smiled."
    pause 0.4
    hide ryohei

    show eden awkward with dissolve
    "That got me holding my breath."
    "I quickly forced a polite smile even with my heart racing."
    "There was something oddly familiar about him...{w=0.3} but I couldn’t figure it out."

    pause 0.5
    hide eden with fade

    play sound "sfx/footsteps.ogg"
    "I heard footsteps approaching me slowly."
    pause 0.2

    jump bar_encounter


label bar_encounter:
    play sfx "sfx/woosh.ogg" volume 0.5
    show ryohei neutral at left with moveinleft

    play sound "sfx/woosh.ogg" volume 0.5
    show eden neutral at right with moveinright

    eden "{i}Why is he standing right here?"
    pause 0.2

    ryohei "Eden Cross?{w=0.2} No way.{w=0.1} Is that really you?"
    eden awkward "!!"

    menu:
        "{i}How should I respond?"

        "Hey...?":
            eden "{cps=15}Hey there...?"
            eden "{cps=15}Uh..."

        "Who... are you?":
            eden "{cps=15}Umm...{w=0.3} who are you?"
            eden "How do you know my name?"
            show ryohei smirk2 with dissolve

    "My confusion must’ve shown on my face because he chuckled."
    ryohei neutral "It’s me,{w=0.1} Ryohei Damien.{w=0.1} Haha, sorry.{w=0.1} You might not remember me."
    ryohei "We had that philosophy elective together,{w=0.1} remember?"

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
    pause 1

    eden "That hit me."
    eden "{cps=15}Ryohei..."
    eden "The Ryohei Damien."

    eden "We were in the same department back in college."
    eden "He was popular.{w=0.2} He was effortlessly charming."
    eden "The kind of guy who made everyone feel seen,{w=0.1} even when he probably didn’t know half of their names."
    eden "I never expected to be on his radar."
    eden "We shared a few lectures,{w=0.1} maybe a group project once,{w=0.1} but I was always the quiet one."
    eden "I was the guy people tend to forget."

    eden "{i}But I remembered him."
    eden "{i}Goddamn,{w=0.1} I think I remembered him more than I should."

    eden "People wouldn’t shut up about him."
    eden "The rumors that he got scouted by some research lab."
    eden "The times he stood in front of the class with that calm demeanor."
    eden "As if he’s always sure of himself."

    pause 0.7

    jump bar_talk


label bar_talk:
    scene cg bar talk
    with dissolve

    "And yet,{w=0.1} here he is."
    "Sitting across from me in this nearly empty lounge,{w=0.1} grinning like we were old friends."
    "He even did it without asking like it was the most natural thing."

    pause 0.3
    eden "Of course I remember you.{w=0.2} You were basically famous, Ryohei."

    pause 1
    "It made him laugh and he didn’t even try to deny it."
    ryohei "Anyway, you can just call me Ryo."


    ryohei "I’m really glad we ran into each other again."
    ryohei "Hey, do you remember that time you made Professor Sam trip over his own lecture notes?"
    ryohei "Still one of the funniest moments ever."
    eden "You...{w=0.2} you remembered that?"
    ryohei "Honestly, that’s one of my favorite memories from back in college."

    pause 0.3
    "And for the first time in what felt like forever...{w=0.2} I didn’t feel like a complete failure."
    "We talked for a while.{w=0.2} Something about his presence...{w=0.2} Felt almost too welcoming."
    "Made it easy for me to open up."
    "It felt safe, or at least I convinced myself it was.{w=0.2}  After all, he was an old acquaintance,{w=0.2}  wasn’t he?"
    "So, like an idiot, I spilled everything.{w=0.2} The insomnia.{w=0.2} The restless nights.{w=0.2} The hollow feeling of being a stranger inside my own skin."

    pause 0.5
    "He listened intently."
    pause 0.5
    "Then, almost casually, he suggested a private consultation."

    pause 0.3
    ryohei "Oh, actually...{w=0.2} I offer sleep therapy. And cognitive consultations as well."
   
    "Before I could react, he produced a card between his fingers, like it had been waiting there all along."
    ryohei "I can definitely help you with that.{w=0.1} Just come to my studio."

    "His word “studio” echoed in my head longer than it should have."

    scene black with fade
    stop music fadeout 2.0

    jump session1_prestudio
