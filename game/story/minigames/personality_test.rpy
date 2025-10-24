# Session 1 — PSYCHOSOPHY TEST

default logic_score = 0
default ethics_score = 0
default will_score = 0
default physics_score = 0
default session1_result = ""  # logic/ethics/will/physics/unreadable


label personality_test:

    scene bg studio with fade

    play music "music/theme4.ogg" fadein 1 volume 0.4
    #our composer made this :)

    show ryohei seated neutral with dissolve

    ryohei "Alright!{w=0.4} Rules are simple."
    ryohei "Pick whatever feels most like you."
    ryohei "Don’t overthink it,{w=0.1} just go with your gut."

    jump personality_test1


label personality_test1:

    ryohei "First question..."

    menu:
        "When you can’t sleep, what do you usually do?"

        "Analyze random deep thoughts":
            $ logic_score += 1

        "Replay past cringe interactions in my head":
            $ ethics_score += 1

        "Get up to “be productive” even if it’s 2 AM":
            $ will_score += 1

        "Grab a snack or adjust my bed":
            $ physics_score += 1

    ryohei seated look "Gotcha."
    pause 0.5

    ryohei "Insomnia sounds exhausting.{w=0.1} That must be rough."
    ryohei "Moving on..."

    jump personality_test2


label personality_test2:

    menu:
        "How do you usually recharge after a long stressful day?"

        "Read a book":
            $ logic_score += 1

        "Journal or cope with my feelings for a bit":
            $ ethics_score += 1

        "Do something active or take decisive action to reset my energy":
            $ will_score += 1

        "Shower, change into comfy clothes, then chill in a cozy spot":
            $ physics_score += 1

    ryohei seated neutral "I see."
    pause 0.5

    jump personality_test3


label personality_test3:

    menu:
        "How do you usually tell when someone’s lying to you?"

        "When their story makes zero sense":
            $ logic_score += 1

        "I don’t know, I just feel it":
            $ ethics_score += 1

        "If they hesitate or act unsure of themselves":
            $ will_score += 1

        "Their body gives it away; like gestures, posture, or fidgeting":
            $ physics_score += 1

    ryohei "Hmm,{w=0.1} interesting."
    pause 0.5
    ryohei "Okay,{w=0.1} next one."

    jump personality_test4


label personality_test4:

    menu:
        "What motivates you the most?"

        "Figuring things out or understanding the world":
            $ logic_score += 1

        "Living in a way that feels authentic to me":
            $ ethics_score += 1

        "Proving I can do or achieve something":
            $ will_score += 1

        "Feeling comfortable, safe, or in control physically":
            $ physics_score += 1

    ryohei "Noted."
    pause 0.5

    ryohei seated smile "Alright,{w=0.1} time for a little roleplay."
    ryohei "Imagine the following scenario..."

    jump personality_test5


label personality_test5:

    menu:
        "You’re on a forest path and it splits three ways. What do you do?"

        "Look for clues to pick the smartest path":
            $ logic_score += 1

        "Reflect and go with the path that feels right to me":
            $ ethics_score += 1

        "Pick one fast and move, no hesitation":
            $ will_score += 1

        "Test each path physically to see which is more safe and “comfortable”":
            $ physics_score += 1

    ryohei "Nice...{w=0.2} That’s an interesting take."
    pause 0.5

    jump personality_test6


label personality_test6:

    menu:
        "You hear a weird noise upstairs in an empty house. What’s the first thing you do?"

        "Peek around and figure out what’s going on":
            $ logic_score += 1

        "Pause and notice how it makes me feel":
            $ ethics_score += 1

        "Run upstairs like a boss":
            $ will_score += 1

        "Grab something nearby just to feel safer":
            $ physics_score += 1

    ryohei "I see.{w=0.3} Okay."
    pause 0.5
    ryohei "Let’s proceed."

    jump personality_test7


label personality_test7:

    menu:
        "A strange creature suddenly appears and stares at you. How do you react?"

        "Quickly look away":
            $ logic_score += 1

        "Scream or shout out of fear":
            $ ethics_score += 1

        "Instinctively raise my hands or get ready to defend":
            $ will_score += 1

        "Run away":
            $ physics_score += 1

    jump personality_test7_jumpscare


label personality_test7_jumpscare:

    stop dialogue fadeout 0.2
    stop music

    scene bg studio4
    with dissolve

    voice "voice/entity/eden.ogg"
    pause 1

    play sound tension
    show entity 1 at center, opacity(0.8), scale(1.1)
    with moveinbottom
    with vpunch

    pause 1

    play sfx "sfx/bone_snap.ogg"

    show entity 2
    pause 1.5

    hide entity
    with dissolve

    show ryohei seated crazy

    "{cps=5}..."
    ryohei "{sc}:)"
    ryohei "What’s wrong?"
    ryohei "Did something catch you off guard?"
    pause 0.5

    ryohei "{cps=15}Well,{/cps}{w=0.2} would your reaction align with the choice you made earlier?"
    pause 1

    ryohei seated neutral "Let’s continue.{w=0.3} No need to dwell on it."

    play music "music/theme4.ogg" fadein 1 volume 0.4
    show bg studio with dissolve

    jump personality_test8


label personality_test8:

    ryohei "Okay,{w=0.1} roleplay’s over!{w=0.3} Let’s get back to the test."
    pause 0.5

    menu:
        "Which compliment do you like the most?"

        "“You’re so sharp and smart”":
            $ logic_score += 1

        "“You’re authentic and honest”":
            $ ethics_score += 1

        "“You’re brave and bold”":
            $ will_score += 1

        "“You seem steady and chill”":
            $ physics_score += 1

    ryohei "We’re nearing the end!"

    jump personality_test9


label personality_test9:

    menu:
        "Which word resonates with you the most?"

        "Luminous":
            $ logic_score += 1

        "Pulse":
            $ ethics_score += 1

        "Flame":
            $ will_score += 1

        "Balance":
            $ physics_score += 1

    ryohei "One final question."

    jump personality_test10


label personality_test10:

    menu:
        "Which word resonates with you the most?"

        "Logic":
            $ logic_score += 1

        "Ethics":
            $ ethics_score += 1

        "Volition":
            $ will_score += 1

        "Physics":
            $ physics_score += 1

    pause 0.5
    ryohei "Congratulations,{w=0.1} you’ve completed the test!"
    ryohei "I’ll go over your results now."

    jump personality_result


label personality_result:

    $ scores = {
        "logic": logic_score,
        "ethics": ethics_score,
        "will": will_score,
        "physics": physics_score,
    }
    $ max_score = max(scores.values())
    $ winners = [k for k,v in scores.items() if v == max_score]

    # note: if two-way tie, tiebreaker. If 3+ tie, unreadable.
    if len(winners) == 1:
        $ session1_result = winners[0]

    elif len(winners) == 2:
        # tiebreaker: pick the one that reached the score first
        if scores[winners[0]] >= scores[winners[1]]:
            $ session1_result = winners[0]
        else:
            $ session1_result = winners[1]

    else:
        # "nothing at all" outcome
        $ session1_result = "unreadable"

    jump personality_reveal


label personality_reveal:

    # Show the chosen type reveal. Ryohei reads it conversationally.
    if session1_result == "logic":
        jump personality_logic

    elif session1_result == "ethics":
        jump personality_ethics

    elif session1_result == "will":
        jump personality_will

    elif session1_result == "physics":
        jump personality_physics

    elif session1_result == "unreadable":
        jump personality_unreadable

    else:
        jump personality_unreadable


label personality_unreadable:

    pause 0.5
    ryohei "{cps=10}...{w=0.2} Huh."
    ryohei "{cps=20}You’re not...{w=0.2} anything,{w=0.1} are you?"

    "He smiled,{w=0.1} but it didn’t reach his eyes."
    "The silence that follows feels like a test."
    pause 0.5

    ryohei "You don’t fit any box.{w=0.1} That’s interesting."
    ryohei "I thought I liked predictable people.{w=0.1} Maybe I like this more."

    jump personality_test_end


label personality_logic:

    ryohei seated neutral "It seems like you’re {i}Logic-First{/i}."
    ryohei "You’re good at cutting through confusion."
    ryohei "When things don’t make sense,{w=0.1} you’re the one who figures it out and puts the pieces back together."
    ryohei "But there’s a cost,{w=0.2} isn’t there?"
    ryohei "You wonder if people see you as too cold or distant—"
    ryohei "Like you care more about facts than feelings."
    ryohei "And you worry what happens if your logic stops working one day."

    jump personality_test_end


label personality_ethics:

    ryohei seated neutral "It seems like you’re {i}Ethics-First{/i}."
    ryohei "You feel people deeply."
    ryohei "You can walk into a room and pick up on what others are holding back —{w=0.3} the hurt,{w=0.1} the hope,{w=0.1} the need."
    ryohei "That sensitivity makes people feel seen in ways they rarely do."
    ryohei "Being around you feels safe,{w=0.1} because you don’t just notice,{w=0.1} you care."
    ryohei "But it’s heavy sometimes,{w=0.2} isn’t it?"
    ryohei "Being that open can be heavy."
    ryohei "You worry you’re too much sometimes,{w=0.1} or that people won’t handle the depth of what you feel."

    jump personality_test_end


label personality_will:

    ryohei seated neutral "It seems like you’re {i}Will-First{/i}."
    ryohei "You don’t wait,{w=0.1} you act."
    ryohei "When others stall,{w=0.1} you move forward;{w=0.1} when doors close,{w=0.1} you push them open."
    ryohei "Your drive creates paths where none exist,{w=0.1} and that force keeps not just you alive,{w=0.1} but often others too."
    ryohei "But there’s a cost,{w=0.2} isn’t there?"
    ryohei "Force comes with risk."
    ryohei "You fear that others see you as reckless or intimidating,{w=0.1} and worse..."
    ryohei "You may one day destroy the very thing that you wish to protect."

    jump personality_test_end


label personality_physics:

    ryohei seated neutral "It seems like you’re {i}Physics-First{/i}."
    ryohei "You trust what’s real.{w=0.2} The solid things,{w=0.1} such as routines,{w=0.1} touch,{w=0.1} and breath."
    ryohei "You’re good at keeping yourself steady when the world tilts,{w=0.1} and that steadiness spills over to the people around you."
    ryohei "But there’s a cost,{w=0.2} isn’t there?"
    ryohei "You wonder if it makes you small.{w=0.2} That people will think you’re clinging to little comforts,{w=0.1} too simple to handle the big picture."

    jump personality_test_end


label personality_test_end:

    stop music fadeout 1

    ryohei seated smile "Thank you for that."
    ryohei "I learned a lot about you today."
    ryohei seated neutral "I’ve actually wanted to be closer to you since {cps=15}college...{/cps}{w=0.4} and it means a lot to finally be here with you now."

    pause 1
    ryohei seated look "Shall we move on?"
    ryohei seated neutral "Remember,{w=0.1} this is all just for fun.{w=0.2} Don’t take the results too seriously."

    show ryohei seated look
    "His tone stayed gentle,{w=0.1} though there was a weight behind it."

    jump session1_end
