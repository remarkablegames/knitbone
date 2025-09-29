label bar:
    play music "music/bar.ogg" fadein 3 volume 0.7
    pause 1

    eden "{cps=10}Hmm..."
    play sound "sfx/ice.ogg" volume 0.5
    eden "Seems like the ice in my glass had succumbed to the warmth..."
    eden "...looks just like my life."

    show cg bar
    with dissolve

    pause 0.5

    "My name’s Eden.{w=0.5} A Psychology major."
    "Voted as “Most Likely to Succeed”."
    eden "{cps=5}..."

    pause 0.5

    eden "{i}But that was years ago..."
    eden "{i}When I had direction in my life."
    eden "{i}Now?{w=0.3} I’m barely surviving on cheap coffee and no sleep."
    eden "{i}I changed three jobs in just twelve months."
    eden "{i}Every “fresh start” only left me more tangled in doubt."
    eden "{i}And yeah, I ended up even more lost."

    "{cps=5}..."
    pause 1

    eden "{i}I don’t even recognize who I am anymore."

    show cg bar at shake
    stop music
    play sound "sfx/chime.ogg" volume 0.8
    "{i}*chimes*"

    pause 0.5
    play sound "sfx/door.ogg" volume 1.1
    "The door opened, but at first,{w=0.1} I hardly registered it."

    scene black with fade
    pause 0.5

    hide cg bar with dissolve

    "The vibe suddenly seemed to shift,{w=0.1} as if someone flipped a switch."
    "I couldn’t help but look..."
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

    "A man walked in,{w=0.1} with the sort of effortless confidence that drew everyone’s eyes to him."
    "He smiled at the bartender,{w=0.1} waved at someone like they were old friends."
    show ryohei look2 at center

    eden "{cps=5}..."
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
    "And then he saw me,{w=0.1} eyes widening as they locked onto mine."
    pause 0.5

    voice "voice/ryohei/chuckle.ogg"
    ryohei laugh "..."
    "He smiled."
    pause 0.5
    hide ryohei

    show eden awkward with dissolve
    "That got me holding my breath."
    "I forced a polite smile, despite my racing heart."
    "There was something oddly familiar about him...{w=0.3} but I couldn’t figure it out."

    pause 0.5
    hide eden with fade

    play sound "sfx/footsteps.ogg"
    "I heard footsteps approaching me slowly."
    pause 0.5

    jump bar_encounter


label bar_encounter:
    play sfx "sfx/woosh.ogg" volume 0.5
    show ryohei neutral at left with moveinleft

    play sound "sfx/woosh.ogg" volume 0.5
    show eden neutral at right with moveinright

    eden "{i}Why is he standing right here?"
    pause 0.5

    menu:
        "What should I say?"

        "Hey...?":
            eden "{cps=15}Hey there...?"
            ryohei "Eden Cross?{w=0.2} No way.{w=0.1} Is that really you?"
            eden awkward "!!"
            eden "{cps=10}Uh..."

        "Who... are you?":
            eden "{cps=15}Umm...{w=0.3} do I know you?"
            show ryohei smirk2 with dissolve

    "My confusion must’ve shown on my face because he chuckled."
    ryohei neutral "It’s me,{w=0.1} Ryohei Damien.{w=0.1} Haha, sorry.{w=0.1} You might not remember me."
    ryohei "We had that psychology elective together,{w=0.1} remember?"
    pause 0.5

    eden "{cps=5}{i}Oh."
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
    eden "{i}Goddamn,{w=0.2} I think I remembered him more than I should."

    eden "People wouldn’t shut up about him."
    eden "I’ve always been envious of him,{w=0.2} even now."

    pause 0.5

    jump bar_talk


label bar_talk:
    scene cg bar talk
    with dissolve

    "And yet,{w=0.1} here he is."
    "Sitting across from me in this nearly empty lounge,{w=0.1} grinning like we were old buddies."
    "He even did it without asking like it was the most natural thing."

    pause 0.5

    eden "Of course I remember you."
    eden "You were basically famous, Ryohei."

    voice "voice/ryohei/chuckle.ogg"
    pause 1

    "It made him laugh.{w=0.1} He didn’t even try to deny it."

    ryohei "You can just call me Ryo."
    ryohei "I’m really glad we ran into each other again."

    pause 1

    ryohei "Well,{w=0.1} Eden,{w=0.2} your name really does you justice."
    ryohei "Looking splendid,{w=0.1} as always!"

    "I couldn’t help but smile back."
    "I’m not sure if I’m most amused by his outlandish teasing,{w=0.2} or by the fact that he remembered my name."

    eden "I don’t think lounging at a jazz club after an exhausting day is much of a splendid look,{w=0.2} but {cps=15}thanks...?"
    eden "You look like...{w=0.3} life’s been treating you well."

    "I leave out the “as always”."

    voice "voice/ryohei/chuckle.ogg"
    "He laughs,{w=0.1} but his eyes narrow in..."

    ryohei "I did notice you’re tired,{w=0.1} though."
    ryohei "Ah-{w=0.2} I don’t meant to offend–"
    eden "No,{w=0.1} it’s fine.{w=0.2} I know I’m living dead..."

    "I laugh,{w=0.1} trying to brush it off."

    eden "Insomnia,{w=0.1} that’s all.{w=0.1} I get used to it."
    ryohei "{cps=5}...{/cps}{w=0.3} What a shame."

    pause 0.5

    "And for the first time in what felt like forever..."
    "I didn’t feel like a complete failure."
    "We caught up and talked for a while."
    "Something about his presence...{w=0.2} felt almost too welcoming."
    "Made it easy for me to open up."
    "It felt safe,{w=0.1} or at least I convinced myself it was."
    "After all,{w=0.1} he was an old acquaintance,{w=0.1} wasn’t he?"
    "So, like an idiot,{w=0.1} I spilled everything."

    pause 0.5
    "He listened intently."

    voice "voice/ryohei/hmm.ogg"
    pause 1

    ryohei "Hmm,{w=0.1} what a...{w=0.2} coincidence?"
    "He chuckles at the last word."
    ryohei "Actually...{w=0.2} I specialize in sleep therapy,{w=0.1} as well as cognitive consultations."

    pause 1

    "Maybe I’m not that strange for feeling like I’m meant to be here with him tonight."
    "Maybe he feels it too."

    ryohei "Would you pay me a visit?"
    eden "What?"
    ryohei "I want to see you."
    "I mustered a smile,{w=0.1} hoping he didn’t notice my bewilderment."
    ryohei "It’d be a private consultation.{w=0.2} I’ve had my studio set up."
    eden "It’s okay.{w=0.2} I’ve already visited doctors."
    ryohei "I figured,{w=0.1} but...{w=0.2} maybe I can do something about it."
    ryohei "And if I can’t,{w=0.1} well,{w=0.1} it’s no wasted money."
    ryohei "I’m offering it for free."

    voice "voice/ryohei/oh.ogg"
    eden "{cps=5}Oh..."

    "It’ll probably be in vain,{w=0.2} but declining now that he seems so willing to help would make an even more pitiful sight."

    pause 0.5

    "Before I could react,{w=0.1} he produced a card between his fingers,{w=0.1} like it had been waiting there all along."
    ryohei "Come to my studio whenever you’re ready,{w=0.2} no pressure."

    "The word “studio” echoed in my head longer than it should have."

    scene black with fade
    stop music fadeout 2.0

    jump session1_prestudio
