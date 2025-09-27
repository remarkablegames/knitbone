label session3:
    jump session3_start

label session3_start:
    play music "music/theme4.ogg" fadein 1.5 volume 0.8
    scene bg studio with fade
    
    show eden thinking at right
    show ryohei neutral at left
    with dissolve

    "My hallucinations felt like they were getting worse, and being in this room wasn't helping."
    pause 0.8
    "Was this all in my head or...?"

    if candle_success:
        ryohei "You did very well, Eden."
        ryohei "I assume you’re ready for what's next."
    else:
        ryohei "Your mind is still clouded. There is noise where there should be focus."
        pause 0.5
        ryohei "Still, we will proceed."

    "Pass or fail, it seemed I was being dragged into the next session regardless."
    "I just nodded, too tired to argue."

    eden bitter2 "Fine. What’s next?"
    
    pause 1.0
    show ryohei look2 with dissolve
    
    ryohei "I have a simple question."
    ryohei serious "Tell me, Eden... are you easily frightened?"

    "The question was unsettling. He leaned forward slightly with his eyes fixed on me."
    
    menu:
        "Yes, I am.":
            eden awkward "I guess so. More than I'd like to admit."
            ryohei look "Okay."

        "No, not really.":
            eden neutral "Not really. I can handle myself."
            ryohei smirk "I love your confidence. We'll see how it goes."

    pause 1
    stop music
    show bg studio3 at shake
    with dissolve
    "He fell silent, letting the tension build...."
    "His gaze drifted to a dark corner of the room behind me."
    ryohei serious "Don't look now... but I think someone is watching us."

    show eden bitter at slight_shake
    "My blood ran cold."
    pause 1
    "Against my better judgment, my eyes darted to the corner."

    pause 1.0
    show bg studio at shake
    with dissolve
    pause 0.5
    show eden awkward at slight_shake
    "There was nothing there."
    
    show ryohei laugh with dissolve
    "Ryohei chuckled, a low, unnerving sound."
    
    ryohei smirk2 "Relax. I'm just testing your focus."
    ryohei "Were you expecting something?"
    pause 0.5
    "..."
    eden bitter2 "{i}Sometimes, I wonder what is wrong with this guy."
    pause 1

    show ryohei neutral
    show eden neutral
    "He then pointed to a small, potted herb on his desk. It was the only living thing in the room."
    ryohei "Let's try a different approach. What do you see there?"

    "I recognized the broad, hairy leaves instantly."
    eden happy "Oh, that’s comfrey!"
    "{cps=70}For the first time since I arrived, my expression softened. Seeing something familiar from my childhood stirred feelings I thought I’d buried."
    
    eden "My grandmom used to call it by its old name... {i}Knitbone."
    
    "Ryohei seemed surprised by my sudden shift in mood, though he masked it with a smile."
    ryohei smirk2 "...Knitbone. An interesting name."
    
    eden smile "She said it could heal broken bones."
    
    pause 1.0
    show eden neutral
    
    ryohei neutral "But...{w=0.5} some breaks aren't in the bone, are they, Eden?"
    "I stayed quiet, letting his words settle in the air between us."
    eden bitter "Uh...well.."
    
    ryohei serious "Some breaks are deeper. And no herb can fix them."
    ryohei smirk "The irony is,  In the past, people thought comfrey..or {i}Knitbone{/i} was safe to use in any way, inside and out."
    ryohei look2 "But studies have shown that ingesting it can be toxic."

    show eden neutral
    "He was talking about the plant, but his eyes told me he was talking about something else."
    pause 1.0
    
    #ryohei trauma dumps------
    show ryohei serious at slight_shake
    "His expression soured, his voice taking on a bitter, sharp edge."
    ryohei "Listen, Eden."
    ryohei glare "There are people obsessed with cures like that."
    "He looked past me, his eyes unfocused, lost in a memory."
    ryohei serious "Just like you, they were also searching for ways to heal themselves...mentally or physically."
    
    eden awkward "...?"
    ryohei "When they're desperate enough, they find a ‘community’ that promises something more than just a fix."
    ryohei "Their philosophy was simple... at least on the surface. To ‘become enlightened,’ you had to give something away."
    ryohei smirk " They called it an ‘offering’ to some cosmic entity.."
    "He let out a short, harsh laugh that held no humor."

    ryohei glare "But 'offering' was just a pretty word for ritualized murder."
    pause 1.0

    eden bitter "What...?"

    ryohei "They had this twisted... logic,  They believed pain was a currency. That you could only heal your own wound by taking on another's life."
    
    pause 0.5
    eden "{i}Why is he telling me this?"
    pause 0.5
    "His voice cracked, the mask of the calm therapist completely gone, replaced by a raw, burning anger."
    show ryohei at slight_shake
    ryohei serious"They would make you believe that ending someone's life wasn’t wrong... it was {i}kindness."
    ryohei "They said you weren’t a killer. You were an angel... taking their pain away so they could finally rest. And their death... that was supposed to be your reward. Your new weight to carry."
    ryohei glare "It was all a lie to control you. A lie to break you down and own the pieces."

    "The therapist I came to see was gone. In his place was just a guy, terrified of his own hands."
    "Everything he’s saying is coming at me too fast. I can’t process it all."
    "He stood abruptly, his chair scraping back. The outburst was so sudden, so violent, it made me flinch."

    ryohei "But I saw it for what it was. I ended that bullshit.  so I ended it. I took the burden for myself."
    "He stared at his own trembling hands, a flicker of something... desperation... in his eyes."
    ryohei "It's supposed to be over. But it... it doesn't just disappear."

    pause 2.0
    show ryohei at slight_shake
    "He stood there, breathing heavily, his knuckles white."

    "I'm starting to realize... he was talking about his past experience."
    show eden bitter at slight_shake
    "Wait—{w=0.5} was he...{w=0.5} in a cult?"
    "This guy wasn't just troubled. He was haunted."
    "And for a second, I forgot to be scared and just felt... a weird pang of pity."
    
    menu:
        "Ask him if he's okay":
            eden awkward "Ryo...? A-are you okay?"
            $ trust += 1

        "Stay quiet.":
            eden bitter "You bite your tongue, unsure if speaking would make things worse."

    "He sank back into his chair, visibly forcing himself to be calm."
    show ryohei neutral at slight_shake
    with dissolve
    
    jump session3_hypnosis0


label session3_hypnosis0:
    play music "music/theme4.ogg" fadein 1.5 volume 0.8
    
    ryohei look "Ahem... I apologize. That was... unprofessional."
    ryohei "..."
    pause 1.0
    ryohei "Anyways."
    pause 0.3
    ryohei look2 "All of that was just an attempt to open your mind."
    ryohei laugh "Looks like it’s ready! So let’s use it."

    pause 0.5
    "He opened a drawer and started rummaging it."
    
    pause 1
    "I just stood there, frozen..... How did his mood... shift so quickly?"
    "Suddenly, his words from our first session... about a 'guided ritual'... took on a much darker meaning."
    "A cold dread washed over me."
    eden bitter "{i}What if this isn’t therapy. He's not even trying to fix my insomnia... "
    eden bitter "Instead, he's actually trying to do something else, and I'm his test subject??"

    pause 0.5
    ryohei smirk "I found it."
    "He then took out a pendulum, a pointed crystal on a silver chain. It looked less like a therapist's tool and more like a ritual object."
    
    show ryohei at center
    with moveinright
    pause 1.0
    "He stepped closer to me."

    pause 0.3
    show eden bitter at slight_shake
    "Doubt wrapped around my mind like chains, tightening with every thought."
    eden awkward "{i}Is he going to do something to me????"
    "Ryohei edged closer behind me, the heat of his body pressing near mine. Panic surged and I felt trapped."
    "My hands shook violently, my pulse racing, and a whisper of fear told me to turn back."
    "But even knowing that, I couldn’t make myself move away."
    "Just before he whisper, I saw his composure slip for a fraction of a second."
    ryohei look "{i}{cps=40}Shhh...{w=0.3} It's okay Eden..."

    pause 1.0
    "Then his eyes cleared, and he smiled at me, his focus absolute."
    hide ryohei
    hide eden
    with dissolve

    jump session3_hypnosis1


label session3_hypnosis1:
    
    show cg hypnosis with fade
    ryohei "This will help quiet the noise in your head."
    ryohei "Just watch the crystal. And listen to my voice. Can you do that for me?"

    pause 1.0
    
    "..."
    "......"
    eden "I can do that."
    
    ryohei "Good. Breathe in... and out. Match my breathing."

    $ countdown.start(seconds=5, jump="session3_hypnosis2")
    menu:

        "Breath":
            $ countdown.cancel()
            $ slider = Slider(speed=3)
            jump hypnosis_minigame

    
label session3_hypnosis2:

    "I found myself breathing in sync with him. It felt strangely intimate, as if we were sharing the same air."
    
    ryohei "{i}Now, watch.{/i}"
    
    "The world vanished in an instant. Everything else disappeared, leaving only the pendulum swinging before my eyes."
    
    ryohei "{i}You’re so tired, Eden. It’s time to let go. Let me hold the weight for you.{/i}"
    "His voice was a promise of rest, and I wanted it more than anything."

    ryohei "Breath in, Eden."

    $ countdown.start(seconds=5, jump="session3_hypnosis3")
    menu:

        "Breath":
            $ countdown.cancel()
    
    ryohei "{i}Deeper now. Down into the quiet. The walls are gone. There is only the path. Follow it.{/i}"
    pause 1.0
    stop music fadeout 1.0

    window hide
    scene black with Dissolve(2.0)
    pause 1.0

    "My vision went dark. I felt like I was falling, not through air, but through myself."
    pause 1.0
    "And then I saw it."
    pause 1.0
    show entity 1 at center
    "..."
    "... am I hallucinating again?"

    window hide
    show entity 2 at center, zoomin
    with vpunch
    pause 0.3
    show entity 3 at center, zoomin
    with vpunch
    pause 1.0
    hide entity
    pause 1.0

    "A presence. Huge, cold, and utterly indifferent." 
    show entity 2 at center, zoomin
    with dissolve
    "It feels like a web of black veins, pulsing slowly in the darkness behind my eyes."
    
    "The pressure grew, like the air was turning to lead around me."
    "The pressure was too much. A scream built in my chest, and my eyes flew open."
    
    hide entity
    scene bg studio2 at hpunch
    with dissolve

    "I was back in the studio, gasping, my heart hammering against my ribs. Ryohei was staring at me."
    pause 1.0
    "His face was pale, his eyes wide with a terrifying mix of fear and excitement."
    
    ryohei "{cps=30}{size=-4}You saw it... didn't you?{/size}"

    "His words barely registered. All I could think of was the image burned into my mind. The feeling of that... thing. It was wrong. All of this was wrong."
    "Adrenaline surged through me, overpowering my exhaustion. I scrambled to my feet, my chair scraping loudly on the floor."
    
    "I stood up, my legs unsteady. My mind was a chaotic mess of pulsating veins and the echo of his frantic whispers."
    "Rest felt impossible. All I wanted was to get out of this room, away from his suffocating presence."
    "I turned towards the door, my hand reaching for the handle."
    
    #show eden panicked at left
    
    "I have to get out. Now."
    eden "I'm leaving."
    "My voice was shaky, but firm. I took a step back, towards the door."
    
    "Panic flashed across Ryohei's face. He dropped the pendulum, the crystal clattering against the table."
    
    #show ryohei panic at center (will add this soon if possible)
    show ryohei serious at center
    ryohei "{i}No—wait. I shouldn’t have—{/i}"
    "He looked genuinely terrified, as if he'd revealed a secret he could never take back."
    
    pause 1.0
    "But his panic lasted only a moment. As I reached for the door, his expression hardened into something desperate and resolute."
    show bg studio3 with hpunch
    "He moved faster than I thought possible, blocking my path."
    
    jump pre_ending
    return

