label session1:
    play sound "sfx/footsteps.ogg"

    scene bg hallway at zoomin
    with fade

    pause 0.5

    "My footsteps felt too loud as I walked."
    "The hallway smelled old and dusty,{w=0.2} the carpet ugly and stained."

    "My thumb kept brushing over the card in my pocket—"
    "1408,{w=0.3} just like the card said.{w=0.3} That’s the room I’ve been trying to track down."

    "After a tour of what felt like the world’s most depressing maze,{w=0.2} I finally spotted the door."
    pause 1
    show cg door with dissolve

    "The little brass number on it looked shiny and new.{w=0.3} It didn’t fit with the rest of the dingy hallway."
    "I stopped,{w=0.3} my hand hovering in the air..."
    "{cps=5}..."
    "I wasn’t sure if I should knock."
    "A part of me just wanted to turn around and leave."
    pause 1

    "{cps=5}..."
    "Right.{w=0.2} I told myself I’d actually show up."
    "As I got ready to knock,{w=0.2} a memory popped into my head..."
    hide cg door with dissolve

    play sound "sfx/flash.ogg" volume 0.7
    scene black with flash
    pause 0.5

    "Last night at the lounge, I revealed too much to someone who was practically a stranger."

    jump bar
    # jump to previous jazz scene prologue
    # I might change certain dialogue in the jazz scene tomorrow: e.g. “I do sleep therapy now. And also cognitive consultation, nothing scary. If you ever want to talk, text me.”


label session1_prestudio:

    "And for some reason,{w=0.2} I actually came."
    "{cps=25}This was probably a bad idea..."
    "We hardly even know each other."

    scene bg hallway at zoomin
    with fade
    pause 2

    show cg door

    menu:
        "Knock":
            pause 0.5
            play sound "sfx/knock.ogg"
            pause 1

            "I finally knocked on the door."
            pause 0.5

        "Turn around":
            hide cg door with dissolve
            scene bg hallway at zoomout

            "I decided to skip the consultation.{w=0.3} I just didn’t feel comfortable."

            scene black
            with fade

            "{cps=35}But my insomnia worsened over time,{w=0.1} leading me to withdraw from society."
            "I heard Ryohei’s consultancy has been growing and he’s now dealing with a large number of patients."
            pause 1

            "Perhaps I should have reached out to him after all?"
            "Like how the saying goes,{w=0.1} {cps=30}“Nothing ventured, nothing gained.”"

            jump end

    play sound "sfx/creak.ogg"
    hide cg door with dissolve

    "The door opened right away."
    "As if he’d been standing there the whole time,{w=0.1} waiting for me."

    pause 1

    show ryohei neutral with dissolve

    voice "voice/ryohei/hey.ogg"
    ryohei "Eden!"

    "He had a warm practiced smile,{w=0.1} and said my name like he knew I would come."

    ryohei "I had a feeling you’d arrive.{w=0.2} Please, come in."

    "I hesitated—"
    "But my feet started moving before I could even think about it."
    play sound "sfx/footsteps.ogg" volume 0.7 fadeout 1

    jump session1_studio


label session1_studio:

    scene bg studio
    with fade

    play music "music/theme3.ogg" fadein 2 volume 0.7

    "The smell was different inside.{w=0.2} The scent of lemon oil and faint herbs filled the air."
    "It felt a bit phony,{w=0.1} like he was trying too hard to make it smell naturally relaxing."
    "The studio was quite simple."
    "Just a couch for me,{w=0.1} and a single,{w=0.1} fancy chair for him."
    "My gaze drifted past a collection of arranged objects as Ryohei led me inside the studio."
    "Soft jazz music played in the background."

    play sound "sfx/woosh.ogg" volume 0.5
    show ryohei neutral at left with moveinleft

    play sfx "sfx/woosh.ogg" volume 0.5
    show eden neutral at right with moveinright

    ryohei "Please,{w=0.1} have a seat.{w=0.2} Make yourself at home."

    "I sat on the couch..."
    "{cps=5}..."
    "It was actually pretty cozy."

    ryohei smirk2 "Comfortable?"

    "I nodded."
    "He sat on his big chair and watched me."

    ryohei "So...{w=0.3} {cps=15}Eden Cross..."

    ryohei serious "You know why you’re here.{w=0.3} Is that right?"

    "He got straight to the point."

    eden "{cps=10}..."

    voice "voice/ryohei/yea.ogg"
    eden "Yeah."

    eden awkward "{cps=20}I guess so...?"
    ryohei neutral "So.{w=0.2} Tell me...{w=0.2} What’s on your mind?"
    ryohei "What brings you here tonight?"
    pause 1

    "My mouth went dry,{w=0.2} as I finally said the line I practiced."
    pause 0.5

    eden neutral "Last night...{w=0.2} you mentioned you could help."
    eden neutral "You said you help people with sleep issues."

    "I told him how I couldn’t sleep, and how I felt like I didn’t know who I was when the lights went off."

    "He listened without rushing."

    voice "voice/ryohei/hmm.ogg"
    pause 1

    "No interruption and no pity."
    "Just that steady,{w=0.1} practiced attention."

    pause 1

    ryohei look2 "Alright then.{w=0.2} Starting with some questions."
    ryohei neutral "Do you have more trouble falling asleep{w=0.1} or staying asleep?"

    voice "voice/ryohei/um.ogg"
    eden "Umm...{w=0.2} both,{w=0.1} equally,{w=0.1} I suppose?"

    ryohei "How many times a week do you suffer from this?"
    eden "I can’t really remember."
    eden "Maybe five?"

    "He purses his lips."

    voice "voice/ryohei/ok.ogg"
    ryohei "Okay."

    ryohei "Are you taking any medications?"
    eden "None."

    voice "voice/ryohei/hmm.ogg"
    pause 1

    ryohei look "I see."

    pause 1

    show ryohei glare
    show eden neutral

    "He pauses,{w=0.4} weighing his words before going on."
    "His expression turned serious,{w=0.2} as if he knows something that I don’t."

    ryohei serious "Insomnia and identity crisis.{w=0.2} That’s a reasonable set to bring in together."
    ryohei "Sleep and sense of self are closer than most people think."
    ryohei "You’re not sleeping because your mind refuses to let you be vulnerable."

    pause 0.5
    ryohei "And that’s why your mind won’t shut down."

    voice "voice/ryohei/ah.ogg"
    pause 0.5

    "{cps=15}That...{/cps}{w=0.3} hit closer to home than I expected."

    show ryohei laugh
    "The smile crept back onto his face."

    pause 0.5
    ryohei neutral "Before we go any deeper,{w=0.2} I have a simple personality test."
    ryohei "To help me understand the shape of this...{w=0.3} {i}weight{/i} you’re carrying..."

    pause 1
    ryohei "It requires a bit of trust,{w=0.2} I know.{w=0.2} But it would help me understand."
    ryohei "...{w=0.4} I really think you should take it."

    jump session1_test


label session1_test:
    menu:
        "Do you want to take the personality test?"

        "Yes":
            eden awkward "Okay...{w=0.2} Ryo...{w=0.3} let’s do it."
            ryohei laugh "Good.{w=0.2} Don’t worry,{w=0.2} it’s simple and not invasive.{w=0.2} Just answer honestly."

            jump personality_test

        "No":
            eden awkward "{cps=30}I...{w=0.3} I don’t think I’m ready yet."

            stop music

            voice "voice/ryohei/hmm.ogg"
            ryohei glare "{cps=15}Hmm...{w=0.3} Is that so?"

            ryohei neutral "Thank you for being honest with me.{w=0.3} That,{w=0.2} in itself,{w=0.2} is a very important step."
            ryohei serious "{cps=10}But..."

            scene bg studio2 with dissolve

            ryohei serious "You came to me for help,{w=0.2} but you’re saying no to the first step."
            eden "Wh-...{w=0.3} What do you mean?"

            "He leaned forward,{w=0.2} his voice low."
            ryohei "Eden."
            ryohei smirk "{cps=100}Refusing only reveals what you’re afraid of.{w=0.2} It shows me exactly what you’re afraid of."

            stop dialogue fadeout 0.2
            hide ryohei
            hide eden

            show bg studio4

            play sound "sfx/jumpscare.ogg" volume 0.5

            show entity 2 at center, scale(1.1), shake
            with hpunch

            scene black

            pause 1

            jump session1_end


label session1_end:
    play music "music/theme3.ogg" fadein 1.5 volume 0.7

    scene bg studio
    with fade

    play sound "sfx/woosh.ogg" volume 0.5
    show ryohei neutral at left with moveinleft

    play sound "sfx/woosh.ogg" volume 0.5
    show eden neutral at right with moveinright

    ryohei "Thank you.{w=0.2} You’ve given me quite a clear impression."
    eden "{cps=15}...Y{w=0.2}... Yeah."

    pause 1

    "{cps=5}..."
    pause 1

    show eden bitter2

    "What the hell was {b}{i}THAT{/i}{/b}?"
    "Oh, perfect.{w=0.1} Now I’m hallucinating in the middle of this {i}“therapy”{/i}."

    eden awkward "{i}{cps=30}Should...{w=0.2} I just...{w=0.2} chalk it up to sleep deprivation and call it a day?"

    menu:
        "What should I do?"

        "Bring it up":
            eden "{cps=10}Um..."
            ryohei "Yes?"
            eden "{cps=20}Did you happen to see...{w=0.2} {i}that?"
            ryohei "See what?"
            eden "...Nevermind."

        "Remain silent":
            eden "{cps=5}..."

    show eden neutral
    pause 1

    "An awkward silence settled between us."
    pause 1

    "His eyes flicked up to mine."

    ryohei "What you’ve shown me earlier tells me enough.{w=0.2} More than enough."
    ryohei glare "Your sleepless nights..."

    "He paused."
    "His gaze was piercing, studying me like I was some kind of specimen."

    pause 1
    ryohei serious "Your insomnia isn’t a mistake.{w=0.2} It’s a pattern."
    ryohei "Your mind is stuck on a loop."
    ryohei "Regular therapy won’t work for you."
    ryohei "What your mind needs is a {i}“key”{/i}...{w=0.3} to redistribute the weight."
    ryohei neutral "What I want to propose isn’t therapy at all."
    ryohei "Think of it more as a sort of...{w=0.3} {cps=20}{i}guided ritual{/i}."

    pause 1
    "{i}“Ritual”"

    pause 0.5
    "{cps=5}..."

    show eden awkward with dissolve

    "That’s...{w=0.3} an {i}interesting{/i} choice of word."
    pause 0.5

    ryohei "I will give you small,{w=0.2} specific tasks to complete."
    ryohei "They'll require precision and focus."
    ryohei look "The goal is to give the burden a new place to rest,{w=0.2} so that your mind can finally find peace."
    ryohei "It’s an unconventional path and it requires absolute trust."
    ryohei neutral "Not just in me,{w=0.2} but in yourself."

    "He was quiet for a moment and stared at me."
    pause 1

    ryohei neutral "I can’t force you to do it.{w=0.2} This only works if you choose it."
    ryohei "You can leave now, but that means going back to your restless routine."
    pause 0.3

    ryohei smirk "Or...{w=0.3} you can agree to Session Two...!"
    ryohei "That’s where we really begin."

    "{cps=5}..."
    "{cps=30}That felt like a challenge."

    ryohei neutral "So,{w=0.1} Eden.{w=0.2} What do you think?"

    show eden neutral

    jump session1_choice


label session1_choice:
    menu:
        "Proceed with Session Two?"

        "Yes":
            show ryohei laugh with dissolve
            jump session2

        "No":
            ryohei look "Ryohei inclined his head slightly.{w=0.2} Surprisingly, there was no hint of disappointment."
            ryohei neutral "I understand."
            eden "I’m sorry,{w=0.2} Ryo..."
            ryohei laugh "It’s okay.{w=0.2} You can take your time.{w=0.2} The offer still stands if you change your mind."
            ryohei "Here,{w=0.2} you can keep my number.{w=0.2} Don’t hesitate to reach out,{w=0.2} even if you just need to talk."

            show black with dissolve

            ryohei smirk "...{w=0.2} I'm sure that...{w=0.3} {cps=30}your sleepless nights will bring you right back to me."

            # ENDING 0 - AVOIDANCE
            jump end
