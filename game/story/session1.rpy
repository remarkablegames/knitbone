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

    ryohei "Please, have a seat. Try to get comfortable."
    "I sat on the couch...."
    "..."
    "{w=0.5}It was actually pretty comfortable.."
    "He sat in his big chair and just watched me."
    ryohei "So..{cps=10}.Eden Cross..."
    ryohei serious "You know why you’re here. Is that right?"

    "He got straight to the point."
    eden "{cps=10}...Yeah."
    eden awkward "{cps=20}I guess so...??"
    ryohei neutral "So. Tell me... What's in your mind?"
    ryohei "What brought you here tonight?"
    pause 1

    "My mouth went dry, as I finally said the line I practiced."
    pause 0.5
    eden neutral "Last night... you mentioned you could help."
    eden neutral "You said you help people with sleep issues."
    "I told him how I couldn’t sleep, and how I felt like I didn’t know who I was when the lights went off."
    "He listened without rushing. No interruption and no pity. Just that steady, practiced attention."

    pause 1
    ryohei look "I see."
    pause 1
    show ryohei glare
    show eden neutral
    "He pauses, weighing his words before going on."
    "His expression had turned serious., like he knows something that I don’t."
    ryohei serious "Insomnia and identity crisis. That’s a reasonable set to bring in together. Sleep and sense of self are closer than most people think."
    ryohei serious "You're not sleeping because your mind refuse to let you be vulnerable."
    pause 0.5
    ryohei "And that's why your mind won't shut down."

    pause 0.5
    "That... hit closer to home than I expected."
    show ryohei laugh
    "The smile creeps back onto his face."

    pause 0.5
    ryohei neutral "Before we go deeper, I have a simple personality test."
    ryohei "To help me understand the shape of this... weight you're carrying..."
    
    pause 1
    ryohei "It requires a bit of trust, I know. But it would help me understand."
    ryohei "....I really think you should take it."

    jump session1_test

label session1_test:
    menu:
        "Do you want to take the personality test?"

        "Yes":
            eden awkward "Okay...Ryo.. let’s do it."
            ryohei laugh "Good. Don’t worry, it’s simple and not invasive. Just answer honestly."

            jump personality_test

        "No":
            eden awkward "{cps=30}I...{w=0.3} I don’t think I’m ready yet."

            stop music
            ryohei glare "{cps=15}Hmm...{w=0.3} Is that so?"
            ryohei neutral "Thank you for being honest with me. That, in itself, is a very important step."
            ryohei serious "But...."
            show bg studio2 with dissolve
            ryohei serious "You came to me for help, but you're saying no to the first step."
            eden "Wh-...{w=0.3} What do you mean?"

            "He leaned forward, his voice low."
            ryohei "Eden."
            ryohei smirk "{cps=250}Refusing only reveals what you’re afraid of. It shows me exactly what you're afraid of."

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

    ryohei "Thank you. You’ve given me quite a clear impression."
    eden "...Y{w=0.3}..Yeah."

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
    "An awkward silence settled between us."

    pause 1
    "His eyes flicked up to mine"
    ryohei "What you’ve shown me earlier tells me enough. More than enough."
    ryohei glare "Your sleepless nights..."
    "He paused. It felt like he was studying me like I was some kind of bug."
    pause 1
    ryohei serious "Your insomnia isn't a mistake. It's a pattern."
    ryohei "Your mind is stuck on a loop."
    ryohei "Regular therapy won't work for you. What your mind need is a 'key' to... redistribute the weight."
    ryohei neutral "What I want to propose isn’t therapy at all. Think of it more as a... guided ritual."
    pause 1.2
    "'Ritual.'"
    pause 0.3
    "..."
    show eden awkward with dissolve
    "That's... an Interesting choice of word."
    pause 0.5
    ryohei "I will give you small, specific tasks to complete."
    ryohei "Though they require precision and focus."
    ryohei look "The goal is to give the burden a new place to rest, so your mind can finally find peace."
    ryohei "It is an unconventional path and it requires absolute trust."
    ryohei neutral "Not just in me, but in yourself."

    "He was quiet for a moment and stared at me."
    pause 1
    ryohei neutral "I can't force you to do it. This only works if you choose it."
    ryohei "You can leave now and go back to your sleepless nights."
    pause 0.3
    ryohei smirk "Or... you can agree to Session Two...! That's where we really begin."

    "..."
    "{cps=30}That felt like a challenge."
    ryohei neutral "So, Eden. What do you think?"

    show eden neutral

    jump session1_choice


label session1_choice:
    menu:
        "Proceed to Session Two?"

        "Agree":
            show ryohei laugh with dissolve
            jump session2

        "Refuse":
            ryohei look "Ryohei inclined his head slightly. Surprisingly with no hint of disappointment."
            ryohei neutral "I understand..."
            eden "I'm sorry, Ryo..."
            ryohei laugh "It's okay. You can take your time. The offer still stands if you change your mind."
            ryohei "Here, you can keep my number. Don't hesitate to reach out, even if you just need to talk."

            show black with dissolve
            ryohei smirk "...I'm sure that....{w=0.3} {cps=30}Your sleepless nights will bring you back to me anyway."

            # ENDING 0 - AVOIDANCE
            jump end






