label session1:
    play sound "sfx/footsteps.ogg"

    scene bg hallway at zoomin
    with fade

    pause 0.5

    "My footsteps feel too loud as I walk."
    "The hallway smelled old and dusty,{w=0.2} while the carpet looks ugly and stained."

    "My thumb keeps brushing over the card in my pocket—"
    "1408,{w=0.3} just like the card said.{w=0.3} That’s the room I’ve been trying to track down."

    "After a tour of what felt like the world’s most depressing maze,{w=0.2} I finally spot the door."
    pause 1

    "The little brass number on it looked shiny and new.{w=0.3} It didn’t fit with the rest of the dingy hallway."
    "I stopped,{w=0.3} my hand just hovering in the air..."
    "{cps=10}..."
    "I wasn’t sure if I should knock."
    "A part of me wanted to just turn around and leave."
    pause 1

    "{cps=10}..."
    "Right.{w=0.2} I told myself I’d actually show up."
    "As I got ready to knock,{w=0.2} a memory popped into my head..."

    play sound "sfx/flash.ogg" volume 0.7
    scene black with flash
    pause 0.5

    "In the lounge last night, I feel like I revealed too much to someone who was practically a stranger."

    jump bar
    # jump to previous jazz scene prologue
    # I might change certain dialogue in the jazz scene tomorrow: e.g. “I do sleep therapy now. And also cognitive consultation, nothing scary. If you ever want to talk, text me.”


label session1_prestudio:
    "And for some reason,{w=0.2} I actually came."
    "This was probably a bad idea..."
    "We hardly even know each other."

    scene bg hallway with fade
    pause 1.0

    menu:
        "Knock":
            play sound "sfx/knock.ogg"
            pause 1.5

            "I finally knocked on the door."
            pause 1

    play sound "sfx/creak.ogg"
    "The door opened right away."
    "Like he was already standing there waiting for me."
    pause 1

    show ryohei neutral with dissolve
    pause 1
    ryohei "Eden!"

    "He had a warm practiced smile, and said my name like he knew I would come."

    ryohei "I had a feeling you’d be here.{w=0.2} Please, come in."

    "I hesitated-"
    "But my feet started moving before I could even think about it."

    jump session1_studio


label session1_studio:
    play music "music/theme3.ogg" fadein 1.5 volume 0.8

    scene bg studio
    with fade

    "The smell was different inside.{w=0.2} It smells like lemon oil and faint herbs."
    "It felt like he was trying too hard to curate it to smell relaxing."
    "And the studio was very simple.{w=0.2} Just a couch for me, and a single, fancy chair for him.{w=0.2} It felt like a stage."
    "There was soft jazz music playing."

    show ryohei neutral at left with moveinleft
    show eden neutral at right with moveinright

    ryohei "Please, have a seat.{w=0.2} Try to get comfortable."
    "I sat on the couch..."
    "..."
    "{w=0.5}It was actually pretty comfortable.."
    "He sat in his big chair and just watched me."

    ryohei "So...{w=0.2}{cps=10} Eden Cross..."
    ryohei serious "You know why you’re here.{w=0.2} Is that right?"

    "He got straight to the point."

    eden "{cps=10}...{w=0.2} Yeah."
    eden awkward "{cps=20}I guess so...?"
    ryohei neutral "So.{w=0.2} Tell me...{w=0.2} What’s on your mind?"
    ryohei "What brought you here tonight?"
    pause 1

    "My mouth went dry,{w=0.2} as I finally said the line I practiced."
    pause 0.5

    eden neutral "Last night...{w=0.2} you mentioned you could help."
    eden neutral "You said you help people with sleep issues."
    "I told him how I couldn’t sleep, and how I felt like I didn’t know who I was when the lights went off."
    "He listened without rushing.{w=0.2} No interruption and no pity.{w=0.2} Just that steady, practiced attention."

    pause 1
    ryohei look "I see."

    pause 1
    show ryohei glare
    show eden neutral

    "He pauses,{w=0.3} weighing his words before going on."
    "His expression had turned serious,{w=0.2} like he knows something that I don’t."

    ryohei serious "Insomnia and identity crisis.{w=0.2} That’s a reasonable set to bring in together.{w=0.2} Sleep and sense of self are closer than most people think."
    ryohei "You’re not sleeping because your mind refuses to let you be vulnerable."

    pause 0.5
    ryohei "And that’s why your mind won’t shut down."

    pause 0.5
    "That...{w=0.3} hit closer to home than I expected."

    show ryohei laugh
    "The smile creeps back onto his face."

    pause 0.5
    ryohei neutral "Before we go any deeper,{w=0.2} I have a simple personality test."
    ryohei "To help me understand the shape of this...{w=0.3} {i}weight{/i} you’re carrying..."

    pause 1
    ryohei "It requires a bit of trust,{w=0.2} I know.{w=0.2} But it would help me understand."
    ryohei "...{w=0.3} I really think you should take it."

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

            ryohei glare "{cps=15}Hmm...{w=0.3} Is that so?"
            ryohei neutral "Thank you for being honest with me.{w=0.3} That,{w=0.2} in itself,{w=0.2} is a very important step."
            ryohei serious "{cps=10}But..."

            show bg studio2 with dissolve

            ryohei serious "You came to me for help,{w=0.2} but you’re saying no to the first step."
            eden "Wh-...{w=0.3} What do you mean?"

            "He leaned forward,{w=0.2} his voice low."
            ryohei "Eden."
            ryohei smirk "{cps=100}Refusing only reveals what you’re afraid of.{w=0.2} It shows me exactly what you’re afraid of."

            stop character fadeout 0.2
            hide ryohei
            hide eden

            show bg studio4

            play sfx "sfx/tension.ogg"

            show entity 2 at center, scale(1.1), shake
            with hpunch

            play sound "sfx/thud.ogg"
            pause 0.5
            scene black

            pause 1
            stop sound

            jump session1_end


label session1_end:
    play music "music/theme3.ogg" fadein 1.5 volume 0.8

    scene bg studio
    with fade

    show ryohei neutral at left with dissolve
    show eden neutral at right with dissolve

    ryohei "Thank you.{w=0.2} You’ve given me quite a clear impression."
    eden "{cps=10}...Y{w=0.3}... Yeah."

    pause 1

    "..."
    pause 1

    show eden bitter2

    "What the hell was {i}THAT{/i}???"
    "Oh, perfect. Now I’m hallucinating in the middle of this {i}“therapy”{/i}."

    eden awkward"{i}{cps=30}Should...{w=0.2} I just...{w=0.2} chalk it up to sleep deprivation and call it a day?"
    show eden neutral with dissolve

    pause 1
    "An awkward silence settled between us."

    pause 1
    "His eyes flicked up to mine."

    ryohei "What you’ve shown me earlier tells me enough.{w=0.2} More than enough."
    ryohei glare "Your sleepless nights..."

    "He paused."
    "It felt like he was studying me like I was some kind of bug."
    pause 1

    ryohei serious "Your insomnia isn’t a mistake.{w=0.2} It’s a pattern."
    ryohei "Your mind is stuck on a loop."
    ryohei "Regular therapy won’t work for you.{w=0.2} What your mind need is a {i}“key”{/i} to...{w=0.2} redistribute the weight."
    ryohei neutral "What I want to propose isn’t therapy at all.{w=0.2} Think of it more as a...{w=0.3} {i}guided ritual{/i}."

    pause 1.2
    "{i}“Ritual”"

    pause 0.3
    "..."

    show eden awkward with dissolve

    "That’s...{w=0.3} an {i}interesting{/i} choice of word."
    pause 0.5

    ryohei "I will give you small,{w=0.2} specific tasks to complete."
    ryohei "Though they require precision and focus."
    ryohei look "The goal is to give the burden a new place to rest,{w=0.2} so your mind can finally find peace."
    ryohei "It is an unconventional path and it requires absolute trust."
    ryohei neutral "Not just in me,{w=0.2} but in yourself."

    "He was quiet for a moment and stared at me."
    pause 1

    ryohei neutral "I can’t force you to do it.{w=0.2} This only works if you choose it."
    ryohei "You can leave now and go back to your sleepless nights."
    pause 0.3

    ryohei smirk "Or...{w=0.3} you can agree to Session Two...!{w=0.3} That’s where we really begin."

    "..."
    "{cps=30}That felt like a challenge."

    ryohei neutral "So, Eden.{w=0.2} What do you think?"

    show eden neutral

    jump session1_choice


label session1_choice:
    menu:
        "Proceed with Session Two?"

        "Agree":
            show ryohei laugh with dissolve
            jump session2

        "Refuse":
            ryohei look "Ryohei inclined his head slightly.{w=0.2} Surprisingly with no hint of disappointment."
            ryohei neutral "I understand..."
            eden "I’m sorry,{w=0.2} Ryo..."
            ryohei laugh "It’s okay.{w=0.2} You can take your time.{w=0.2} The offer still stands if you change your mind."
            ryohei "Here,{w=0.2} you can keep my number.{w=0.2} Don’t hesitate to reach out,{w=0.2} even if you just need to talk."

            show black with dissolve

            ryohei smirk "...{w=0.2} I’m sure that...{w=0.3} {cps=30}Your sleepless nights will bring you back to me anyway."

            # ENDING 0 - AVOIDANCE
            jump end
