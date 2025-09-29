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
    ryohei "Pick whatever feels most like you.{w=0.1} Don’t overthink it,{w=0.1} just go with your gut."

    jump personality_test1


label personality_test1:
    ryohei "First question..."

    menu:
        "When you can’t sleep, what do you usually do?"
        "Analyze random deep thoughts":
            $ logic_score += 1
        "Replaying past cringe interactions in my head":
            $ ethics_score += 1
        "Getting up to “be productive” even if it’s 2 AM":
            $ will_score += 1
        "I grab a snack, or adjust my bed":
            $ physics_score += 1

    ryohei seated look "Gotcha."
    pause 0.5

    ryohei "Insomnia sounds exhausting.{w=0.1} That must be rough."
    ryohei "Moving on..."

    jump personality_test2


label personality_test2:
    menu:
        "How do you usually recharge after a long stressful day?"

        "Maybe read a book":
            $ logic_score += 1
        "I journal or cope with my feelings for a bit":
            $ ethics_score += 1
        "I do something active or take decisive action to reset my energy":
            $ will_score += 1
        "I shower, change into comfy clothes, then chill in a cozy spot":
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
        "Their body gives it away. Like gestures, posture, or fidgeting":
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
        "You hear a weird noise upstair in an empty house. What is the first thing you’ll do?"

        "Peek around and figure out what’s going on":
            $ logic_score += 1
        "Pause and notice how it makes you feel":
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

    stop character fadeout 0.2
    stop music

    scene bg studio4
    with dissolve

    voice "voice/entity/eden.ogg"
    pause 1

    play sound "sfx/tension.ogg"
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
    pause 0.3
    ryohei "Well,{w=0.1} would your reaction align with the choice you made earlier?"
    pause 1

    ryohei seated neutral "Let’s continue.{w=0.2} No need to dwell on it."

    play music "music/theme4.ogg" fadein 1 volume 0.4
    show bg studio with dissolve

    jump personality_test8


label personality_test8:
    ryohei "Okay,{w=0.1} roleplay’s over!{w=0.2} Let’s get back to the test."
    pause 0.3

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
            jump personality_result
        "Ethics":
            $ ethics_score += 1
            jump personality_result
        "Volition":
            $ will_score += 1
            jump personality_result
        "Physics":
            $ physics_score += 1
            jump personality_result

    pause 0.5
    ryohei "Congratulations! You’ve completed the questionnaire. I will review and present your results now."


label personality_result:
    $ scores = {
        "logic": logic_score,
        "ethics": ethics_score,
        "will": will_score,
        "physics": physics_score
    }
    $ max_score = max(scores.values())
    $ winners = [k for k,v in scores.items() if v == max_score]

    # note: if two-way tie, tiebreaker. If 3+ tie, unreadable.
    if len(winners) == 1:
        $ session1_result = winners[0]
        jump reveal_result

    elif len(winners) == 2:
        # tiebreaker: pick the one that reached the score first
        if scores[winners[0]] >= scores[winners[1]]:
            $ session1_result = winners[0]
        else:
            $ session1_result = winners[1]
            jump reveal_result

    else:
        jump unreadable_result


label unreadable_result:
    # "nothing at all" outcome
    $ session1_result = "unreadable"

    pause 0.5
    ryohei "{cps=10}...{w=0.2} Huh."
    ryohei "{cps=20}You’re not...{w=0.2} anything,{w=0.1} are you?"

    "He smiles,{w=0.1} but it doesn’t reach his eyes."
    "The silence that follows feels like a test."
    pause 0.5

    ryohei "You don’t fit any box.{w=0.1} That’s interesting."
    ryohei "I thought I liked predictable people.{w=0.1} Maybe I like this more."

    $ unreadable = True

    jump personality_test_end


label reveal_result:
    # Show the chosen type reveal. Ryohei reads it conversationally.
    if session1_result == "logic":
        ryohei seated neutral "It seems like you are {b}Logic-First"
        ryohei "You’re good at cutting through confusion."
        ryohei "When things don’t make sense, you’re the one who figures it out and puts the pieces back together."
        ryohei "But there’s a cost, isn’t there?"
        ryohei "You wonder if people see you as too cold or distant—"
        ryohei "Like you care more about facts than feelings. And you worry what happens if your logic stops working one day."

        $ persistent.session1_reading = "logic"

        jump personality_test_end

    elif session1_result == "ethics":
        ryohei seated neutral "It seems like you are {b}Ethics-First"
        ryohei "You feel people deeply. You can walk into a room and pick up on what others are holding back — the hurt, the hope, the need."
        ryohei "That sensitivity makes people feel seen in ways they rarely do. Being around you feels safe, because you don’t just notice, you care."
        ryohei "But it’s heavy sometimes, isn’t it?"
        ryohei "Being that open can be heavy. You worry you’re too much sometimes, or that people won’t handle the depth of what you feel."

        $ persistent.session1_reading = "ethics"

        jump personality_test_end

    elif session1_result == "will":
        ryohei seated neutral "It seems like you are you are {b}Will-First."
        ryohei "You don’t wait, you act. When others stall, you move forward; when doors close, you push them open."
        ryohei " Your drive creates paths where none exist, and that force keeps not just you alive, but often others too."
        ryohei "But there’s a cost, isn’t there?"
        ryohei "Force comes with risk. You fear people see you as reckless or intimidating, and worse... your own hands might one day destroy what you most wanted to protect."

        $ persistent.session1_reading = "will"

        jump personality_test_end

    elif session1_result == "physics":
        ryohei seated neutral "It seems like you are you are {b}Physics-First."
        ryohei "You trust what’s real. The solid things, such as routines, touch, and breath."
        ryohei "You’re good at keeping yourself steady when the world tilts, and that steadiness spills over to the people around you."
        ryohei "But there’s a cost, isn’t there?"
        ryohei "You wonder if it makes you small. That people will think you’re clinging to little comforts, too simple to handle the big picture."

        $ persistent.session1_reading = "physics"

        jump personality_test_end


label personality_test_end:
    stop music fadeout 1

    ryohei seated smile "Thanks for that.{w=0.2} I learned a lot about you today."
    ryohei seated neutral "I’ve actually wanted to be closer to you since college...{w=0.2} and it means a lot to finally be here with you now."

    pause 1
    ryohei seated look "Shall we move on?"
    ryohei seated neutral "Remember,{w=0.1} this is all just for fun.{w=0.2} Don’t take the results too seriously."

    show ryohei seated look
    "His tone stays gentle,{w=0.1} though there’s a weight behind it."

    jump session1_end
