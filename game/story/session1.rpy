label session1:
    play sound "sfx/footsteps.ogg"

    scene bg hallway at zoomin
    with fade

    pause 0.5

    "My footsteps feel too loud as I walk."
    "The hallway smelled old and dusty,"
    "while the carpet looks ugly and stained."

    "My thumb keeps brushing over the card in my pocket—"
    "1408, just like the card said. {w=0.5}That’s the room I’ve been trying to track down."

    "After a tour of what felt like the world's most depressing maze, I finally spot the door."
    pause 1
    "The little brass number on it looked shiny and new. It didn't fit with the rest of the dingy hallway."
    "I stopped, and my hand just hovered in the air...."
    "...{w=1.5}I wasn't sure if I should knock."
    "A part of me wanted to just turn around and leave."
    pause 1

    "..."
    "Right. I told myself I’d actually show up."
    "As I got ready to knock, a memory popped into my head....."
    scene black with fade
    pause 1

    "In the lounge last night, I feel like I revealed too much to someone who was practically a stranger."

    pause 1

    jump bar
    # jump to previous jazz scene prologue
    # I might change certain dialogue in the jazz scene tomorrow: e.g. “I do sleep therapy now. And also cognitive consultation, nothing scary. If you ever want to talk, text me.”

label session1_prestudio:
    "And for some reason, I actually came."
    "This was probably a bad idea..."
    "We hardly even know each other."

    scene bg hallway with fade
    pause 1.0

    "Finally,{w=0.5} I knocked on the door."

    play sound "sfx/knock.ogg"
    pause 1.5

    "The door opened right away.{w=0.5} Like he was already standing there waiting for me."
    play sound "sfx/creak.ogg"

    pause 1
    show ryohei neutral with dissolve
    pause 1
    ryohei "Eden!"

    "He had a warm practiced smile, and said my name like he knew I would come."
    ryohei "I had a feeling you'd be here. Please, come in."
    "I hesitated-"
    "But my feet started moving before I could even think about it."

    jump session1_studio

label session1_studio:
    play music "music/theme3.ogg"
    scene bg studio
    with fade

    "The smell was different inside. It smells like lemon oil and faint herbs."
    "It felt like he was trying too hard to curate it to smell relaxing."
    "And the studio was very simple. Just a couch for me, and a single, fancy chair for him. It felt like a stage."
    "There was soft jazz music playing."

    show ryohei neutral at left with moveinleft
    show eden neutral at right with moveinright

    ryohei "Have a seat. Try to get comfortable."
    "I sat on the couch...."
    "..."
    "{w=0.5}It wasn't comfortable at all."
    "He sat in his big chair and just watched me."
    ryohei "So..{cps=10}.Eden Cross..."
    ryohei serious "You know why you’re here. Is that right?"

    "He got straight to the point."
    eden "{cps=10}...Yeah."
    eden awkward "{cps=20}I guess so...??"
    ryohei neutral "So. Tell me, in your own words..."
    ryohei "What brought you here tonight?"
    pause 1
    eden "...Huh."
    pause 0.5
    eden bitter2 "Wow. Not even a welcome, huh?"
    "Guess we’re skipping small talk and jumping right into the spotlight."
    "I barely sat down...{w=0.5} and already felt like I was on a trial."
    show eden awkward 
    "Still, I didn’t complain. I opened my mouth as I force the words out."

    pause 0.5
    "My mouth went dry, as I finally said the line I practiced. I told him how I couldn’t sleep, and how I felt like I didn’t know who I was when the lights went off."
    "He listened without rushing. No interruption and no pity. Just that steady, practiced attention."

    pause 1
    ryohei look "I see."
    pause 1
    show ryohei glare
    show eden neutral
    "He pauses, weighing his words before going on."
    "His expression had turned serious., like he knows something that I don’t."
    ryohei serious "Insomnia and identity crisis. That’s a reasonable set to bring in together. Sleep and sense of self are closer than most people think."
    ryohei serious "You're not sleeping because you're scared of losing your own sanity."
    pause 0.5
    ryohei smirk "And that's why your mind won't shut down."
    "The smile creeps back onto his face."
    pause 0.5
    ryohei neutral "Before we go deeper, I have a simple personality test. It's not for a grade. It just helps me see how you think."
    pause 1
    ryohei "....I really think you should take it."

    jump session1_test

label session1_test:
    menu:
        "Do you want to take the personality test?"

        "Yes":
            eden awkward "Okay... let’s do it."
            ryohei laugh "Good. Don’t worry, it’s simple and not invasive. Just answer honestly."

            jump personality_test

        "No":
            eden awkward "{cps=30}I...{w=0.3} I don’t think I’m ready yet."

            stop music
            ryohei glare "{cps=15}Hmm...{w=0.3} Is that so?"
            show bg studio2 with dissolve
            ryohei serious "That's interesting. You came to me for help, but you're saying no to the first step."
            eden "Wh-...{w=0.3} What do you mean?"

            "He leaned forward, his voice low."
            ryohei "Eden."
            ryohei smirk "Saying 'no' tells me everything I need to know. It shows me exactly what you're afraid of."

            play sound "dialogue.ogg"
            hide ryohei
            hide eden
            show bg studio4
            show entity 2 at center, shake, 
            pause 0.5
            scene black 
            pause 3.0
            stop sound

            jump session1_end

label session1_end:
    play music "music/theme3.ogg"
    scene bg studio
    with fade

    show ryohei neutral at left with dissolve
    show eden neutral at right with dissolve

    ryohei "Good. You’ve given me quite a clear impression."

    pause 1

    "..."
    pause 1
    #show eden scared
    show eden bitter2
    "What the hell was THAT????"
    "Oh, perfect. Now I’m hallucinating in the middle of this 'therapy'."
    eden awkward"{i}{cps=30}Should..{w=0.2} I just... {w=0.2}chalk it up to sleep deprivation and call it a day?"
    show eden neutral with dissolve

    pause 1
    "His eyes flicked up to mine, and for a second it was like being pinned under a microscope slide."
    ryohei "What you’ve shown me earlier tells me enough. More than enough."
    ryohei glare "Your sleepless nights..."
    "He paused. It felt like he was studying me like I was some kind of bug."
    pause 1
    ryohei serious "Your insomnia isn't a mistake. It's a pattern."
    ryohei "Your mind is stuck on a loop."
    ryohei "Regular therapy won't work for you. What your mind need is a 'key'."
    ryohei neutral "What I want to propose isn’t therapy at all. Think of it more as a... guided ritual."
    pause 1.2
    "'Ritual.'"
    pause 0.3
    "..."
    show eden bitter2
    "That word made me feel uneasy."
    show eden awkward with dissolve
    pause 0.5
    ryohei "I will give you small tasks to do. You just have to do them exactly as I say."
    ryohei "If you do, you'll finally get some peace."
    ryohei smirk "And you'll finally meet the part of you that's been keeping you awake."

    "He was quiet for a moment, just staring at me."
    pause 1
    ryohei neutral "I can't force you to do it. This only works if you choose it"
    ryohei "You can leave now and go back to your sleepless nights."
    pause 0.3
    ryohei smirk "Or... you can agree to Session Two...! That's where we really begin."

    "..."
    "{cps=30}It felt like a challenge."
    ryohei neutral "So, Eden. Are you ready for a change?"

    jump session1_choice


label session1_choice:
    menu:
        "Proceed to Session Two?"

        "Agree":
            show ryohei laugh with dissolve
            "A slow, happy smile grew on his face. He looked like he had just won something."
            ryohei "Good. I thought so. Session Two will be... interesting. It won't feel like your usual therapy."
            "But it is exactly what you need."
            # jump session2
            jump timer_example

        "Refuse":
            "Ryohei just leaned back in his chair. He didn't look mad, just interested."
            ryohei "That's okay.{w=0.3} Being scared is normal. The choice is yours."
            ryohei "Keep my number. And well....The door is always open."

            show bg studio2 with dissolve
            ryohei smirk "...You'll be back anyway....{w=0.8} Your sleepless nights will bring you back to me."

            # ENDING 0 - AVOIDANCE
            jump ending

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





