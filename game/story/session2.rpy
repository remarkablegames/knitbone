# This label is intended to be jumped to from the end of session1.rpy
# e.g. after the player agrees to proceed.

label session2:

    jump session2_start

label session2_start:

    pause 1.0

    ryohei "Good."
    "Ryohei’s smile deepened, like the answer had been inevitable."

    pause 1.5
    ryohei look "Hold on a sec...."
    hide ryohei with dissolve

    pause 1
    #play sound "sfx/rustles.ogg"
    "He stood and began rummaging through the shelves, his movements smooth and deliberate."
    "Suddenly, the air felt thick and still. The faint, pleasant scent of lemon oil and herbs now seemed synthetic, like a cheap air freshener."

    pause 2
    show ryohei neutral at center
    with dissolve

    "When he returned, he was holding a small, ornate box."
    pause 1
    ryohei "Then let's begin Session Two."
    "His voice was lower now, a deep sound that seemed to make the room feel quiet."

    "..."
    "The feeling of being in a safe place was starting to fade."
    pause 0.5

    hide eden
    hide ryohei 
    with dissolve

    jump session2_devotion

label session2_devotion:

    show ryohei seated neutral at center
    with fade
    pause 1.0

    "He moved to the table and sat directly across from me. A subtle shift that made him the focal point of the entire room."

    pause 0.5
    ryohei "Before we begin the exercise, I want to ask you something, Eden."
    pause 0.5
    ryohei seated "What is your opinion... on devotion?"

    pause 0.5
    eden "Devotion?{w=0.5} To what?"
    "The question was so out of left field I could only blink. "

    ryohei seated smile "To...anything!{w=0.5} Whether it's a person, an idea, or a god."
    pause 0.5
    "...Huh."
    "I hesitated. It felt like a trick question."

    menu:

        "It sounds dangerous.":
            eden "It depends on what you're devoted to. Blind devotion can be dangerous."
            ryohei seated look "I see. You're careful. That's understandable."
            "He filed it that away but his expression was unreadable."
            $ trust -= 1

        "It's a form of trust.":
            eden "I guess it's a form of absolute trust. Devotion is like an anchor. Something to hold onto when you're lost."
            ryohei seated look "An anchor... Yes. A worthy cause requires unwavering trust."
            "He looked satisfied, as if I'd given the correct answer."
            $ trust += 1


    pause 1.2

    show ryohei seated serious
    "He paused, his expression shifting into something that looked unnervingly like a confession."
    
    pause 1
    ryohei "I used to know people who were part of ... group."
    pause 0.5
    ryohei "They were devoted to a singular idea."
    ryohei "They believed that to truly change—"
    ryohei "To become more than what they were...they had to give up a part of themselves."
    "...?"
    "My skepticism must have been obvious. This had nothing to do with insomnia."
    "This was about something else entirely."
    ryohei "They saw it as a... transcendence. To an outsider, their methods might have seemed extreme. Cruel, even."
    "He continued, his eyes searching mine, gauging my reaction."
    ryohei "But they believed true enlightenment required sacrifice. That you couldn't become whole until a piece of you was given away."

    pause 0.5
    "It sounded an awful lot like he was talking about a cult."
    "And it sounded an awful lot like this guy believed it."
    eden "Uh-huh...."

    show ryohei seated neutral with dissolve
    ryohei "My apologies. I didn’t mean to bring that up."
    "He waved a hand dismissively, the philosophical conversation ending as abruptly as it began."
    
    stop music fadeout 5.0
    ryohei "Now, let's move on..."
    jump session2_candle

label session2_candle:

    play music "music/theme4.ogg" fadein 1.5

    #play sound "sfx/rustles.ogg"
    pause 0.5
    "He opened the velvet-lined box. Inside, nestled in black satin, were six unlit candles of varying heights."

    ryohei seated smile "Let's play a game, Eden."
    ryohei seated neutral "This is a 'focusing exercise.'"
    "He lit the candles and set them on the table in a chaotic line."
    pause 0.5
    ryohei "The objective is simple. Arrange these candles from {b}Shortest to tallest. Left to right."

    pause 0.5
    eden "Oh...{w=0.5} that sounds easy."
    "Without thinking, I reached for the nearest one."

    show ryohei seated serious at slight_shake
    "His hand shot out, not touching mine, but hovering just above it."

    ryohei seated smile "Nuh-Uh."
    ryohei seated crazy "There are rules."
    "His tone was now flat, sharp, and cold."
    ryohei "Discipline is paramount. You have {b}exactly four moves.{/b} A 'move' is the swapping of any candles."
    ryohei seated look "Exceed {b}four{/b}, and the pattern is irrevocably broken. Do you understand?"

    "I nodded. My mouth is suddenly dry."
    "I looked at the candles...."
    
    $ candle = Candle(moves=4, candles=6)
    jump candle_minigame


label session2_success:
    pause 1
    $ trust += 1

    "A perfect, ascending line. All in less than four moves."
    show ryohei seated crazy with dissolve
    "Ryohei was smiling."
    "It wasn't his usual, practiced smile..."
    "This was wide, genuine, and utterly terrifying."
    ryohei "{i}Hmm...Excellent.{/i}"
    "He whispered the word, savoring it like a fine wine."

    show bg studio2 at shake
    ryohei "I like you, you’re sharp."
    ryohei "You act without hesitation and you're decisive."
    ryohei "That's exactly why I need you."
    eden "Ryo..? What do you mea-"

    #----very short-jumpscare, to make players wonder---
    stop music
    scene black with dissolve
    show entity 3 at slight_shake, center
    play sound "sfx/tension.ogg"
    pause 0.3
    hide entity
    stop sound
    #---

    play music "music/theme3.ogg" fadein 1.5

    show bg studio
    show ryohei seated neutral
    ryohei "That is all for now. You've demonstrated remarkable potential."
    ryohei "You should prepare yourself for our next session."

    scene black with fade
    stop music fadeout 2.0

    #jump session3
    jump ending

label session2_fail:
    $ trust -= 1

    #---very short-jumpscare, to make players wonder---
    pause 
    stop music
    scene black
    show entity 3 at slight_shake, center
    play sound "sfx/tension.ogg"
    pause 0.3
    hide entity
    stop sound
    #---

    show bg studio
    show ryohei seated serious
    
    "My hand froze in mid-air."
    ryohei "That's five. The pattern is now lost."
    "Although there was no anger in his voice. There was a flat disappointment that scraped against my nerves."

    "Before I could apologize, he reached over."
    "His hands moved in a blur of three graceful, precise swaps. The candles snapped into a perfect, ascending line."
    "The sheer ease of it was a quiet.... brutal humiliation."

    show ryohei seated neutral with dissolve
    ryohei "Do not be discouraged."
    "The placating words were a stark contrast to the cold calculation in his eyes. He was observing me, taking notes on my failure."
    ryohei "It indicates your mind is still... noisy."
    ryohei "Do not worry, we can still move on to the next session"

    ryohei seated serious "Our next session will require a more...{w=0.3} direct methodology. To help you focus."
    ryohei seated look "That will be all."

    "The dismissal was absolute. He turned from me before I had even processed it."
    ryohei "Heads up, Eden. We must quiet the static in your mind."

    scene black with fade
    stop music fadeout 2.0

    "I was left with the bitter taste of failure in my mouth."

    #jump session3
    jump ending
