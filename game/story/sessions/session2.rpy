# This label is intended to be jumped to from the end of session1.rpy
# e.g. after the player agrees to proceed.

default candle_success = False


label session2:

    jump session2_start


label session2_start:

    ryohei "Good."
    "Ryohei’s smile deepened,{w=0.1} as if the answer had been inevitable."
    pause 1.5

    ryohei look "Hold on a sec..."

    hide ryohei with dissolve
    pause 1

    play sound "sfx/rustle.ogg"

    "He stood and began rummaging through the shelves,{w=0.1} his movements smooth and deliberate."
    "Suddenly,{w=0.1} the air went still, lingering thick with every breath."
    "The faint,{w=0.1} pleasant scent of lemon oil and herbs felt even more synthetic,{w=0.1} like cheap air freshener."

    pause 1
    show ryohei neutral at center
    with dissolve

    "When he returned,{w=0.1} he was holding a small, ornate box."

    voice "voice/ryohei/mmm.ogg"
    pause 1

    ryohei "Then let’s begin Session Two."
    "His voice was lower now,{w=0.1} a smooth, deep sound that silenced the room."

    "{cps=5}..."
    "The feeling of being in a safe place was starting to fade."
    pause 0.5

    hide eden
    hide ryohei
    with dissolve

    jump session2_devotion


label session2_devotion:

    show ryohei seated neutral at center
    with fade

    play sound "sfx/woosh.ogg" volume 0.5
    pause 1

    "He moved to the table and sat directly across from me."
    "A subtle shift that made him the focal point of the entire room."
    pause 0.5

    ryohei "Before we begin the exercise,{w=0.2} I want to ask you something,{w=0.2} Eden."
    pause 0.5

    ryohei seated "What is your opinion on...{w=0.3} {cps=15}{i}devotion{/i}?"

    voice "voice/ryohei/um.ogg"
    pause 1

    eden "Devotion?{w=0.5} To what?"

    "The question was so left field that I could only blink. "

    ryohei seated smile "To...{w=0.2} anything!{w=0.5} Whether it’s a person, an idea, a god..."
    pause 0.5

    "{cps=5}..."

    voice "voice/ryohei/uh.ogg"
    eden "Uh."

    "I hesitated.{w=0.3} It felt like a trick question."

    menu:

        "My opinion on devotion is..."

        "It sounds dangerous.":
            eden "It depends on what you’re devoted to."
            eden "Blind devotion can be dangerous."

            voice "voice/ryohei/oh.ogg"
            ryohei seated look "I see.{w=0.2} You’re careful.{w=0.2} That’s understandable."

            "He filed that away, his expression unreadable."

            $ trust -= 1

        "It’s a form of trust.":
            eden "I guess it’s a form of absolute trust."
            eden "Devotion is like an anchor.{w=0.2} Something to hold onto when you’re lost."

            voice "voice/ryohei/ok.ogg"
            ryohei seated look "An anchor...{w=0.3} Yes.{w=0.2} A worthy cause requires unwavering trust."

            "He looked satisfied,{w=0.1} as if I’d given the correct answer."

            $ trust += 1

    show ryohei seated serious

    voice "voice/ryohei/hmm.ogg"
    pause 1

    "He paused,{w=0.1} his expression shifting into something that looked unnervingly like a confession."
    pause 1

    ryohei "I used to know people who were part of...{w=0.4} a group."
    pause 0.5

    ryohei "They were devoted to a singular idea."
    ryohei "They believed that to truly change—"
    ryohei "To become more than what they were...{w=0.2} they had to give up a part of themselves."

    voice "voice/ryohei/uh.ogg"
    eden "{cps=5}...?"

    "My skepticism must have been obvious.{w=0.2} This had nothing to do with insomnia."
    "This was about something else entirely."

    ryohei "They thought of it as...{w=0.4} reaching a new level."
    ryohei "To an outsider,{w=0.2} their methods might have seemed extreme.{w=0.3} Maybe even cruel."

    "He continued,{w=0.1} his eyes searching mine,{w=0.1} gauging my reaction."
    ryohei "But that’s what they believed.{w=0.3} They believed {i}true enlightenment{/i} required total devotion."
    ryohei "And that you couldn’t become {i}whole{/i} until a part of you was given away."

    pause 1

    "{cps=5}..."

    "I couldn’t make sense of what he was saying..."
    "Everything he said{w=0.2} sounded like cult nonsense."
    "And he seemed completely convinced himself."
    pause 0.5

    voice "voice/ryohei/uh.ogg"
    eden "{cps=15}Uh-huh..."

    show ryohei seated neutral with dissolve
    ryohei "My apologies.{w=0.2} I didn’t mean to bring that up."
    "He waved a hand dismissively,{w=0.1} the philosophical conversation ending as abruptly as it began."

    stop music fadeout 5
    ryohei "Now,{w=0.2} let’s move on..."

    jump session2_candle_intro


label session2_candle_intro:

    play music "music/theme4.ogg" fadein 1.5 volume 0.7

    play sound "sfx/rustle.ogg"
    pause 0.5

    "He opened the velvet-lined box."
    "Inside,{w=0.2} nestled in black satin,{w=0.1} were six unlit candles of varying heights."

    ryohei seated smile "Let’s play a game,{w=0.2} Eden."
    ryohei seated neutral "This is a “focusing exercise.”"

    play sound "sfx/light.ogg"
    "He lit the candles and set them on the table in a chaotic line."
    pause 0.5

    ryohei "The objective is simple."
    "Arrange these candles from {i}shortest to tallest{/i}.{w=0.3} And {i}left to right{/i}."
    pause 0.5

    voice "voice/ryohei/oh.ogg"
    eden "Oh...{w=0.5} that sounds easy."

    "Without thinking,{w=0.1} I reached for the nearest one."

    play sound "sfx/thud.ogg" volume 0.7
    show ryohei seated serious at slight_shake
    "His hand shot out,{w=0.1} not touching mine,{w=0.1} but hovering just above it."

    voice "voice/ryohei/no.ogg"
    ryohei seated smile "Nuh-uh."

    ryohei seated crazy "There are rules."

    "His tone was now flat,{w=0.1} sharp,{w=0.1} and cold."

    ryohei "Discipline is paramount."
    ryohei "You have exactly {i}four moves."
    ryohei "A “move” is the swapping of any candles."
    ryohei seated look "Exceed {i}four{/i}, and the pattern is irrevocably broken."
    ryohei "Do you understand?"

    jump session2_candle_confirm


label session2_candle_confirm:
    menu:
        "Are the rules of the candle game clear?"

        "Yes":
            "I nodded,{w=0.2} my mouth suddenly dry."
            "I looked at the candles..."
            $ candle.start(moves=4, candles=6, win="session2_candle_win1", lose="session2_candle_lose")

        "No":
            ryohei "Let’s play a tutorial with {i}four candles{/i} and {i}three moves{/i}."
            $ candle.start(moves=3, candles=4, win="session2_candle_tutorial_win", lose="session2_candle_tutorial_lose")


label session2_candle_tutorial_win:
    voice "voice/ryohei/nice.ogg"
    ryohei "Good job.{w=0.1} You beat the tutorial."
    jump session2_candle_confirm


label session2_candle_tutorial_lose:
    ryohei "You weren’t able to complete the tutorial."
    jump session2_candle_confirm


label session2_candle_win1:
    voice "voice/ryohei/nice.ogg"
    ryohei "Great job."
    ryohei "I believe you’re ready for the next challenge."
    ryohei "Do you think you can sort {i}seven candles{/i} with {i}four moves{/i}?"

    menu:
        "Am I up to the challenge?"

        "Yes":
            eden "Let’s do it."
            ryohei "Good luck."
            $ candle.start(moves=4, candles=7, win="session2_candle_win2", lose="session2_candle_lose")


label session2_candle_win2:
    $ trust += 1
    $ candle_success = True

    eden "{cps=15}I...{w=0.3} I did it."

    "A perfect,{w=0.1} ascending line.{w=0.2} All in less than four moves."

    show ryohei seated crazy with dissolve

    voice "voice/ryohei/chuckle.ogg"
    "Ryohei was smiling."
    "It wasn’t his usual,{w=0.1} practiced smile..."
    "This was wide,{w=0.1} genuine,{w=0.1} and utterly terrifying."

    voice "voice/ryohei/hmm.ogg"
    ryohei "{i}Hmm..."

    voice "voice/ryohei/nice.ogg"
    ryohei "{i}Nice."

    "He whispered the word,{w=0.2} savoring it like a fine wine."

    play sound "sfx/thud.ogg" volume 0.5
    show bg studio2 at shake

    ryohei "I like you,{w=0.2} you’re sharp."
    ryohei "You act without hesitation and you’re decisive."
    ryohei "That’s exactly why I need you."
    eden "{cps=15}Ryo...?{w=0.3} What do you mea-"

    #----very short-jumpscare, to make players wonder---
    stop music
    scene black
    play sound "sfx/jumpscare.ogg"
    show entity 3 at slight_shake, center
    pause 0.3
    hide entity
    #---

    play music "music/theme3.ogg" fadein 1.5 volume 0.7

    show bg studio
    show ryohei seated neutral

    ryohei "That is all for now.{w=0.3} You’ve demonstrated remarkable potential."
    ryohei "You should prepare yourself for our next session."

    scene black with fade
    stop music fadeout 2

    jump session3


label session2_candle_lose:
    $ trust -= 1

    voice "voice/ryohei/no.ogg"
    ryohei seated serious "Stop."

    #---very short-jumpscare, to make players wonder---
    stop music
    scene black
    play sound "sfx/jumpscare.ogg"
    show entity 3 at slight_shake, center
    pause 0.3
    hide entity
    #---

    show bg studio
    show ryohei seated serious

    "My hand froze in mid-air."
    ryohei "You’re out of moves.{w=0.2} The pattern is now lost."
    "Although there was no anger in his voice,{w=0.2} there was a flat disappointment that scraped against my nerves."

    "Before I could apologize,{w=0.1} he reached over."
    "His hands moved in a blur of graceful,{w=0.1} precise swaps."
    "The candles snapped into a perfect,{w=0.1} ascending line."
    "The sheer ease of it was a quiet...{w=0.2} brutal humiliation."

    show ryohei seated neutral with dissolve
    ryohei "Do not be discouraged."

    "The placating words were a stark contrast to the cold calculation in his eyes."
    "He was observing me,{w=0.1} taking notes on my failure."

    ryohei "It indicates your mind is still...{w=0.3} noisy."
    ryohei "Do not worry,{w=0.1} we can still move on to the next session."

    ryohei seated serious "Our next session will require a more...{w=0.3} direct methodology."
    ryohei "To help you focus."
    ryohei seated look "That will be all."

    "The dismissal was absolute."
    "He turned from me before I had even processed it."

    scene black with fade
    stop music fadeout 2

    "I was left with the bitter taste of failure in my mouth."

    jump session3
