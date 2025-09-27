label bar:
    play music "music/bar.ogg" fadein 1.5 volume 0.8
    pause 1

    eden "{cps=15}Hmm..."
    eden "Seems like the ice in my glass had succumbed to the warmth..."
    eden "...it looks just like my life."

    show cg bar
    with dissolve
    pause 0.7

    "My name’s Eden.{w=0.5} I’m a Psychology major."
    "Voted as “Most Likely to Succeed”."
    eden "{cps=15}..."

    pause 0.5

    eden "{i}But that was years ago...{w=0.2} When I had directions in my life."

    eden "{i}Now? I’m surviving on coffee with no sleep."
    eden "{i}I changed three jobs in just twelve months."
    eden "{i}Every “fresh start” only left me more tangled in doubt.{w=0.2} And yeah, I just ended up more lost."
    "..."
    pause 1
    eden "{i}I don’t even recognize who I am anymore."

    show cg bar at shake
    stop music
    play sound "sfx/chime.ogg"
    "{i}*chimes*"

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

    "A guy had walked in with an easy confidence, and everyone eyed on him."
    "He smiled at the bartender, waved at someone like they were old friends."
    show ryohei look2 at center

    eden "..."
    eden "{i}So, he’s that kind of guy huh."
    eden "{i}He looked...{w=0.3} so put together— assertive and relaxed."
    eden "{i}And his shirt—{w=0.3}that probably cost more than my rent, yet he wore it so casually."
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
    "There was something oddly familiar about him...{w=0.3} but I couldn’t figure it out."

    pause 0.5
    hide eden with fade

    play sound "sfx/footsteps.ogg"
    "I heard footsteps approaching me slowly."
    pause 0.2

    show ryohei neutral at left with moveinleft
    show eden neutral at right with moveinright

    eden "{i}Why is he standing right here?"
    pause 0.2

    ryohei "Eden Cross?{w=0.2}  No way. Is that really you?"
    eden awkward "!!"

    menu:
        "{i}How should I respond?"

        "Hey...?":
            eden "{cps=15}Hey there...?"
            eden "Uh....."

        "Who... are you?":
            eden "Umm...who are you?"
            eden "How do you know my name?"
            show ryohei smirk2 with dissolve

    "My confusion must’ve shown on my face because he chuckled."
    ryohei neutral "It’s me, Ryohei Damien. Haha, sorry. You might not remember me."
    ryohei "We had that philosophy elective together, remember?"

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

    pause 0.3
    eden "Of course I remember you. You were basically famous, Ryohei."

    pause 1
    "It made him laugh and he didn’t even try to deny it."
    ryohei "Anyway, you can just call me Ryo."


    ryohei "I’m really glad we ran into each other again."
    ryohei "Hey, do you remember that time you made Professor Sam trip over his own lecture notes? Still one of the funniest moments ever."
    eden "You...{w=0.2} remembered that?"
    ryohei "Honestly, that’s one of my favorite memories from back in college."

    pause 0.3
    "And for the first time in what felt like forever...{w=0.2} I didn’t feel like a complete failure."
    "We talked for a while. Something about his presence... Felt almost too welcoming."
    "Made it easy for me to open up."
    "It felt safe, or at least I convinced myself it was.{w=0.2}  After all, he was an old acquaintance,{w=0.2}  wasn’t he?"
    "So, like an idiot, I spilled everything.{w=0.2}  The insomnia. The restless nights. The hollow feeling of being a stranger inside my own skin."

    pause 0.5
    "He listened intently."
    pause 0.5
    "Then, almost casually, he suggested a private consultation."

    pause 0.3
    ryohei "Oh, actually... I offer sleep therapy. And cognitive consultations as well."
   
    "Before I could react, he produced a card between his fingers, like it had been waiting there all along."
    ryohei "I can definitely help you with that. Just come to my studio."

    "His word “studio” echoed in my head longer than it should have."

    scene black with fade
    stop music fadeout 2.0

    jump session1_prestudio
