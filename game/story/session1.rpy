label session1:
    play sound "sfx/footsteps.ogg"

    scene bg hallway at zoomin
    with fade

    pause 0.5

    "The hallway’s narrow and a little worn out, with beige walls and numbers on crooked metal... My footsteps feel too loud as I walk."

    "My thumb keeps brushing over the card in my pocket—"
    "1408, just like the card said. That’s the room I’ve been trying to track down."

    "After what feels like wandering through a small maze, I finally spot the door. The numberplate on the door ahead was small and brass."
    "I stood there a moment longer than I should have, hand hovering like I needed permission to knock."

    pause 1

    "Right. I told myself I’d actually show up."
    "Crossing over, a memory slid into place—"
    "last night in the lounge, a guy approached me."
    scene black with fade

    jump bar
    # jump to previous jazz scene prologue
    # I might change certain dialogue in the jazz scene tomorrow: e.g. “I do sleep therapy now. And also cognitive consultation, nothing scary. If you ever want to talk, text me.”

label session1_prestudio:
    "... and here am I."

    scene bg hallway with fade
    pause 1.0

    "My chest felt tight... like the way it does when I’ve been awake too many nights in a row."
    "Finally, I knocked."

    play sound "sfx/knock.ogg"
    pause 1.5

    "The door opened almost instantly, like he’d been waiting."
    play sound "sfx/creak.ogg"

    pause 1
    show ryohei neutral with dissolve
    pause 1
    ryohei "Eden!"

    "His smile was warm, disarming."
    ryohei "You made it. Come in."
    "I hesitated on the threshold."

    jump session1_studio


label session1_studio:
    play music "music/theme4.ogg"
    scene bg studio
    with fade

    "The smell was different inside. It smells like lemon oil and faint herbs."
    "It didn’t smell clinical, but it didn’t smell entirely lived-in either. He probably curated the air itself to make someone relax."

    show ryohei neutral at left with moveinleft
    show eden neutral at right with moveinright

    ryohei "You may sit. Make yourself comfortable."
    ryohei "My consultation here is not like other therapy, I try to keep the space simple."

    "I sat on a couch where the table in front of me was taller than I thought-"
    "across from it was a single ergonomic chair for Ryohei, making it feel less like a living room and more like a private discussion space."

    ryohei serious "So, you know why you’re here, right?"
    pause 1
    eden "{cps=10}... Yes."

    ryohei neutral "Alright. Let’s get straight to the point."
    ryohei "Tell me, in your own words, what brought you here tonight?"

    "My mouth went dry, as I finally said the line I practiced. I told him how I couldn’t sleep, and how I felt like I didn’t know who I was when the lights went off."
    "He listened without rushing. No interruption and no pity. Just that steady, practiced attention."

    ryohei "I see."
    pause 1
    # The corner of his mouth lifts.
    ryohei serious "Insomnia and identity crisis. That’s a reasonable set to bring in together. Sleep and sense of self are closer than most think."
    ryohei "Before we go deeper... Would you be open to a short personality test? It can help anchor things, especially if you’re struggling with your identity."
    ryohei "It’s recommended to take the test."

    jump session1_test


label session1_test:
    menu:
        "Do you want to take the personality test?"

        "Yes":
            eden awkward "Okay... let’s do it."
            ryohei laugh "Good. Don’t worry, it’s simple and not invasive. Just answer honestly."

            jump personality_test

        "No":
            eden think "{cps=15}I...{w=0.3} I don’t think I’m ready yet."

            ryohei glare "Hmm... Is that so?"
            ryohei "But even if you don’t take the test, you’re still here. And that tells me something already."
            eden neutral "... What do you mean?"

            "He folds his hands together, voice low, steady."
            ryohei smirk "Avoidance is its own kind of answer. It shows me where the edges of your fear are… and edges are useful. They tell us where to press."

    jump session1_end


label session1_end:
    play music "music/theme4.ogg"
    scene bg studio
    with fade

    show ryohei neutral at left with dissolve
    show eden neutral at right with dissolve

    ryohei "Good. You’ve given me quite a clear impression."

    "His eyes flicked up to mine, and for a second it was like being pinned under a microscope slide."
    ryohei glare "What you’ve shown me earlier tells me enough. More than enough."
    ryohei "Your sleepless nights... it’s not random. It’s a pattern your mind has been repeating for a long time."
    ryohei "There is a way to work with it—"
    ryohei neutral "What I’m going to propose may feel unfamiliar at first. A method, not exactly therapy, not exactly ritual either... Perhaps, somewhere in between."
    ryohei "I will ask you to do small things. You just have to follow my words."
    ryohei "It was just simple tasks. But they have to be done with precision. Every step matters. If you’re careless, it won’t work. And If you’re attentive... well, you may find yourself able to sleep."
    ryohei "And more importantly, you’re finally able to see who you are."
    ryohei smirk "Maybe help you see who you really are when the lights go out."

    "He watched me carefully."

    ryohei neutral "I won’t force you..."
    ryohei "This only works if you choose it. You can leave here tonight and nothing changes. Or..."
    ryohei "... you can agree to try! and I’ll guide you into Session Two. That’s where the real work begins."

    "His gaze didn’t waver."

    ryohei "So... Eden. Do you want to proceed?"

    jump session1_choice


label session1_choice:
    menu:
        "Proceed with Session Two?"

        "Agree":
            show ryohei laugh with dissolve
            "Ryohei’s smile deepened, like the answer had been inevitable."
            ryohei "Good. Let’s move on to Session 2... What happens there... will not feel like therapy. But don’t let that unsettle you. It’s exactly what you need."
            # jump session2
            jump timer_example

        "Refuse":
            "Ryohei inclined his head slightly, not disappointed, not surprised."
            ryohei "That’s fine. The  choice is yours. But the door will stay open."
            ryohei "... You’ll come back when the nights make you."

            # ENDING 0 - AVOIDANCE
            jump end

label timer_example:
    $ countdown.start(seconds=5, jump="end")

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

