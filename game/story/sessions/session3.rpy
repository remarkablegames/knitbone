label session3:
    jump session3_start


label session3_start:
    play music "music/theme4.ogg" fadein 1.5 volume 0.7
    scene bg studio with fade

    show eden thinking at right
    show ryohei neutral at left
    with dissolve

    "My hallucinations were getting worse, and being in this room wasn’t helping."
    pause 0.8
    "Was this all in my head or...?"

    if candle_success:
        ryohei "You did very well,{w=0.1} Eden."
        ryohei "I assume you’re ready for what’s next."
    else:
        ryohei "Your mind is still clouded.{w=0.2} There is noise where there should be focus."
        pause 0.5
        ryohei "Still,{w=0.2} we shall proceed."

    "Pass or fail,{w=0.1} it seemed that I was being dragged into the next session regardless."
    "I just nodded,{w=0.1} too tired to argue."

    voice "voice/ryohei/fine.ogg"
    eden bitter2 "Fine.{w=0.1} What’s next?"
    pause 1

    show ryohei look2 with dissolve

    ryohei "I have a simple question."
    ryohei serious "Tell me,{w=0.2} Eden...{w=0.4} are you easily frightened?"

    "The question was unsettling.{w=0.2} He leaned forward slightly with his eyes fixed on me."

    menu:
        "Am I easily frightened?"

        "Yes, I am.":
            eden awkward "I guess so.{w=0.2} More than I’d like to admit."
            voice "voice/ryohei/ok.ogg"
            ryohei look "Okay."

        "No, not really.":
            eden neutral "Not really.{w=0.2} I can handle myself."
            voice "voice/ryohei/mmm.ogg"
            ryohei smirk "I love your confidence.{w=0.1} We’ll see how it goes."

    pause 1
    stop music

    play sound "sfx/thud.ogg" volume 0.5

    show bg studio3 at shake
    with dissolve

    "He fell silent,{w=0.2} letting the tension build..."
    "His gaze drifted to a dark corner of the room behind me."

    ryohei serious "Don’t look now...{w=0.3} but I think someone is watching us."

    show eden bitter at slight_shake

    play sound "sfx/tension.ogg"
    "My blood ran cold."

    pause 1
    "Against my better judgment,{w=0.1} my eyes darted to the corner."

    pause 1

    play sound "sfx/thud.ogg" volume 0.3
    show bg studio at shake
    with dissolve

    pause 0.5
    show eden awkward at slight_shake
    "There was nothing there."

    show ryohei laugh with dissolve

    voice "voice/ryohei/chuckle.ogg"
    "Ryohei chuckled,{w=0.2} a low,{w=0.2} unnerving sound."

    ryohei smirk2 "Relax.{w=0.1} I’m just testing your focus."
    ryohei "Were you expecting something?"
    pause 0.5

    "{cps=5}..."

    eden bitter2 "{i}Sometimes,{w=0.1} I wonder what's wrong with this guy."

    jump session3_comfrey


label session3_comfrey:

    play music "music/theme4_nopiano.ogg" fadein 1.5 volume 0.7
    hide ryohei
    hide eden

    show cg comfrey with dissolve
    show ryohei neutral at left
    show eden neutral at right

    "He then pointed to a small,{w=0.1} potted herb on his desk."
    "It was the only living thing in the room."

    ryohei "Let’s try a different approach."
    ryohei "What do you see there?"

    menu:
        "I see..."

        "Comfrey":
            pass

    "I recognized the broad,{w=0.1} hairy leaves instantly."

    voice "voice/ryohei/oh.ogg"
    eden happy "Oh, that’s a comfrey!"

    "{cps=70}For the first time since I arrived,{w=0.2} my expression softened."
    "{cps=70}Seeing something familiar from my childhood stirred up feelings I thought I’d long buried."

    eden "My grandma used to call it by its old name...{w=0.3} {i}{cps=10}Knitbone."
 
    "Ryohei seemed surprised by my sudden shift in mood,{w=0.1} though he masked it with a smile."

    ryohei smirk2 "Knitbone...{w=0.4} An interesting name."

    eden smile "She said it could heal broken bones."

    voice "voice/ryohei/hmm.ogg"
    pause 1

    show eden neutral

    ryohei neutral "But...{w=0.5} some breaks aren’t in the bone,{w=0.1} are they,{w=0.1} Eden?"

    "I stayed quiet,{w=0.1} letting his words settle in the air between us."

    voice "voice/ryohei/uh.ogg"
    eden bitter "{cps=15}Uh...{w=0.2} well..."

    ryohei serious "Some breaks are deeper.{w=0.2} And no herb can fix them."
    ryohei smirk "The irony is,{w=0.1} in the past,{w=0.1} people thought comfrey...{w=0.3} or {i}Knitbone{/i} was safe to use in any way,{w=0.1} inside and out."
    ryohei look2 "But studies have shown that ingesting it can be toxic."

    show eden neutral
    "He was talking about the plant,{w=0.2} but his eyes told me he meant something else."
    pause 1

    hide cg comfrey with dissolve

    jump session3_trauma


label session3_trauma:

    stop music fadeout 1.5

    play sound "sfx/thud.ogg" volume 0.4

    show ryohei serious at slight_shake

    "His expression soured,{w=0.2} his voice taking on a bitter,{w=0.1} sharp edge."

    ryohei "Listen,{w=0.2} Eden."
    ryohei glare "There are people obsessed with cures like that."
    "He looked past me,{w=0.1} his eyes unfocused,{w=0.1} lost in a memory."
    ryohei serious "Just like you,{w=0.2} they were also searching for ways to heal themselves...{w=0.3} mentally or physically."

    eden awkward "{cps=5}...?"

    ryohei "When they’re desperate enough,{w=0.2} they find a {i}“community”{/i} that promises something more than just a fix."
    ryohei "Their philosophy was simple...{w=0.3} at least on the surface."
    ryohei "To become {i}“enlightened”{/i},{w=0.3} you had to give something away."
    ryohei smirk "They called it an {i}“offering”{/i} to some cosmic entity..."
    pause 1

    voice "voice/ryohei/chuckle.ogg"
    "He let out a short,{w=0.2} harsh laugh that held no mirth."
    pause 1

    ryohei glare "But {i}“offering”{/i} was just a pretty word for ritualized murder."
    pause 1

    voice "voice/ryohei/uh.ogg"
    eden bitter "{cps=10}What...?"

    ryohei "They had this twisted...{w=0.3} logic."
    ryohei "They believed pain was a currency.{w=0.2} That you could only heal your own wound by taking on another’s life."

    pause 0.5
    "{i}Why is he telling me this?"
    pause 0.5

    "His voice cracked,{w=0.2} the mask of the calm therapist completely gone,{w=0.2} replaced by a raw,{w=0.1} burning anger."

    play music "music/terror.ogg" volume 0.9
    play sound "sfx/thud.ogg" volume 0.5

    show ryohei at slight_shake
    show cg ryohei scared at slight_shake
    with dissolve

    ryohei serious "They would make you believe that ending someone’s life wasn’t wrong...{w=0.3} it was {i}kindness."
    ryohei "They said you weren’t a killer.{w=0.2} You were an angel...{w=0.3} taking their pain away so they could finally rest."
    ryohei "And their death...{w=0.3} that was supposed to be your reward.{w=0.3} Your new weight to carry."
    ryohei glare "It was all a lie to control you.{w=0.2} A lie to break you down and own the pieces."

    hide cg ryohei scared with dissolve
    pause 1

    "The therapist I came to see was gone."
    "In his place was just a man,{w=0.1} terrified of his own hands."
    "Every word he spoke was coming at me too fast."
    "I couldn’t process it all."
    
    play sound "<from 0.2 to 1.6>sfx/creak.ogg"

    "He stood abruptly,{w=0.1} his chair scraping back."
    "The outburst was so sudden,{w=0.1} so violent,{w=0.1} that it made me flinch."

    ryohei "But I saw it for what it was."
    ryohei "I ended that bullshit.{w=0.2} So I took on the burden for myself."
    "He stared at his own trembling hands,{w=0.2} a flicker of something...{w=0.3} desperation...{w=0.4} in his eyes."
    ryohei "It’s supposed to be over.{w=0.2} But it...{w=0.3} it doesn’t just disappear."

    pause 1

    play sound "sfx/thud.ogg" volume 0.4
    show ryohei at slight_shake

    voice "voice/eden/inhale.ogg"
    "He stood there,{w=0.1} breathing heavily,{w=0.1} hands molded into fists so tight his knuckles turned bone white."

    "I started to realize...{w=0.1} he was talking about his past."

    show eden bitter at slight_shake

    "Wait—{w=0.5} was he...{w=0.5} in a cult?"
    "This guy wasn’t just troubled.{w=0.2} He was haunted."
    "And for a second,{w=0.2} I forgot to be scared and just felt...{w=0.3} {cps=25}a weird pang of pity."

    menu:
        "Should I say something?"

        "Ask him if he’s okay":
            eden awkward "{cps=15}Ryo...?{w=0.3} A-are you okay?"
            $ trust += 1

        "Stay quiet":
            eden bitter "You bite your tongue,{w=0.2} unsure if speaking would make things worse."

    "He sank back into his chair,{w=0.1} visibly forcing himself to be calm."

    show ryohei neutral at slight_shake
    with dissolve

    stop music fadeout 1
    jump session3_hypnosis0


label session3_hypnosis0:
    play music "music/theme4.ogg" fadein 1.5 volume 0.7

    ryohei look "Ahem...{w=0.2} I apologize.{w=0.1} That was...{w=0.3} unprofessional."
    ryohei "{cps=5}..."
    pause 1

    ryohei "Anyways."
    pause 0.5

    ryohei look2 "All of that was just an attempt to open your mind."
    ryohei laugh "Looks like it’s ready!{w=0.2} So let’s use it."

    pause 0.5
    play sound "sfx/rustle.ogg"
    "He opened a drawer and started rummaging it."

    pause 1

    "I just stood there,{w=0.1} frozen..."
    "How did his mood...{w=0.2} shift so quickly?"
    "Suddenly,{w=0.1} his words from our first session...{w=0.2} about a “guided ritual”...{w=0.3} took on a much darker meaning."
    "A cold dread washed over me."

    eden bitter "{i}What if this isn’t therapy?{w=0.3} He’s not even trying to fix my insomnia... "
    eden bitter "{i}Instead,{w=0.1} he’s trying to do something else,{w=0.2} with me as his test subject...?"

    pause 0.5

    voice "voice/ryohei/oh.ogg"
    ryohei smirk "I found it."

    "He then took out a pendulum,{w=0.2} a pointed crystal on a silver chain."
    "It looked less like a therapist’s tool and more like a ritual object."

    play sound "<from 0 to 1>sfx/footsteps.ogg"
    show ryohei at center
    with moveinright

    "He stepped closer to me."

    pause 0.5
    show eden bitter at slight_shake

    "Doubt wrapped around my mind like chains,{w=0.1} choking me with every thought."
    eden awkward "{i}What is he going to do to me...?"

    "Ryohei edged closer behind me,{w=0.1} the heat of his body pressing against mine."
    "Panic surged and I realized I was trapped."

    play sound "sfx/heartbeat.ogg"
    "My hands shook violently,{w=0.1} my pulse racing,{w=0.1} and a deep, primal fear screamed at me to turn back."

    "But even knowing that,{w=0.1} I couldn’t make myself move away."
    "As he moved closer to my ear,{w=0.1} his composure slipped for a fraction of a second."

    voice "voice/eden/exhale.ogg"
    ryohei look "{i}{cps=20}Shhh...{w=0.3} It’s okay,{w=0.1} Eden..."

    pause 1

    "Then his eyes cleared and he smiled at me,{w=0.1} his focus absolute."

    hide ryohei
    hide eden
    with dissolve

    jump session3_hypnosis1


label session3_hypnosis1:

    stop music fadeout 1

    show cg hypnosis with fade

    play music "sfx/ticking.ogg"

    ryohei "This will help quiet the noise in your head."
    ryohei "Just watch the crystal.{w=0.1} And listen to my voice."
    ryohei "Can you do that for me?"

    menu:
        "Listen to his instructions?"

        "Yes":
            eden "I can do that."
            ryohei "Good."

        "...":
            "{cps=10}..."
            "{cps=10}......"
            ryohei "Let’s continue."

    voice "voice/eden/inhale.ogg"
    ryohei "Breathe in..."

    voice "voice/eden/exhale.ogg"
    ryohei "... and out."

    ryohei "Match my breathing."

    $ slider.start(speed=10, win="hypnosis_minigame_win1", lose="hypnosis_minigame_lose")


label hypnosis_minigame_win1:
    $ trust += 1
    voice "voice/ryohei/nice.ogg"
    ryohei "Great,{w=0.2} let’s go faster."
    $ slider.start(speed=15, win="hypnosis_minigame_win2", lose="hypnosis_minigame_lose")


label hypnosis_minigame_win2:
    $ trust += 1
    voice "voice/ryohei/yes.ogg"
    ryohei "Excellent,{w=0.2} continue to focus and don’t get distracted."
    $ slider.start(speed=20, win="hypnosis_minigame_win3", lose="hypnosis_minigame_lose")


label hypnosis_minigame_win3:
    $ trust += 1
    eden "I matched each inhale with an exhale,{w=0.2} regaining control over my breath."
    jump session3_hypnosis2


label hypnosis_minigame_lose:
    $ trust -= 1
    voice "voice/eden/exhale.ogg"
    eden "My breathing faltered.{w=0.2} The steady pattern I’d relied on slipped away."
    jump session3_hypnosis2


label session3_hypnosis2:

    voice "voice/eden/inhale.ogg"
    "I found myself breathing in sync with him."
    "It felt strangely intimate,{w=0.3} as if we were sharing the same air."

    ryohei "{i}Now,{w=0.2} watch."

    play sound "sfx/chime.ogg" volume 0.8
    "The world vanished in an instant."
    "Everything else disappeared,{w=0.1} leaving only the pendulum swinging before my eyes."

    ryohei "{i}You’re so tired,{w=0.1} Eden."
    ryohei "{i}It’s time to let go."
    ryohei "{i}Let me hold the weight for you."

    "His voice was a promise of rest,{w=0.1} and I wanted it more than anything."

    ryohei "Breathe in,{w=0.1} Eden."

    menu:
        "Breathe":
            voice "voice/eden/inhale.ogg"

    ryohei "{i}Deeper now."
    ryohei "{i}Down into the quiet."
    ryohei "{i}The walls are gone."
    ryohei "{i}There is only the path."
    ryohei "{i}Follow it."

    voice "voice/eden/exhale.ogg"
    pause 1
    stop music fadeout 1

    jump session3_entity


label session3_entity:

    scene black with Dissolve(2)

    pause 1

    "My vision went dark."
    "I was falling,{w=0.1} not through air,{w=0.1} but through myself."

    pause 1
    "And then I saw it."
    pause 1

    play sfx "sfx/tension.ogg"
    show entity 1 at center

    "{cps=5}..."
    "Am I hallucinating again?"

    play music "sfx/static.ogg" volume 0.8

    play sound "sfx/thud.ogg" volume 0.7
    show entity 2 at center, zoomin
    with vpunch

    pause 0.3

    play sound "sfx/bone_snap.ogg"
    show entity 3 at center, zoomin
    with vpunch
    pause 0.5
    hide entity
    pause 1

    "A presence.{w=0.2} Huge, cold, and utterly indifferent."
    show cg eyes at zoomin
    with dissolve

    "It felt like a web of black veins,{w=0.1} pulsing slowly in the darkness behind my eyes."

    "The pressure grew{w=0.1}, the thick air pressing against my ribcage and stealing my breath."
    "The sensation was too much.{w=0.2} A scream built in my chest,{w=0.1} and my eyes flew open."

    hide cg eyes
    stop music

    jump session3_escape


label session3_escape:

    play sound "sfx/heartbeat.ogg"

    scene bg studio2 at hpunch
    with dissolve

    "I was back in the studio,{w=0.1} gasping,{w=0.1} my heart thrashing against my ribs."
    "Ryohei was staring at me."

    pause 1

    "His face was pale,{w=0.1} his eyes wide with a horrifying mixture of fear and excitement."

    ryohei "{cps=30}{size=-4}You saw it...{w=0.1} didn’t you?"

    "His words barely registered."
    "All I could think of was the image burned into my mind."
    "The feeling of that...{w=0.3} {cps=20}{i}thing."
    
    pause 1

    play sound "sfx/thud.ogg" volume 0.7
    show cg eden scared at hpunch
    with dissolve

    "It was wrong.{w=0.1} All of this was wrong."
    "Adrenaline surged through me,{w=0.1} overpowering my exhaustion."

    play sound "<from 0.2 to 1.6>sfx/creak.ogg"

    "I scrambled to my feet,{w=0.1} my seat kicking back onto the floor."

    "I stood up,{w=0.1} my legs unsteady."

    voice "voice/entity/eden.ogg"
    "My mind was a chaotic mess of pulsating veins and the echoes of his frantic whispers."

    "All I wanted at that moment was to get out of this room,{w=0.1} away from his suffocating presence."

    play sound "sfx/footsteps.ogg"
    "I turned towards the door,{w=0.1} my hand reaching for the handle."

    "I have to get out.{w=0.1} {i}Now."

    eden "{i}I’m leaving."
    hide cg eden scared with dissolve

    "My voice was shaky,{w=0.1} but firm."

    play sound "<from 0 to 0.5>sfx/footsteps.ogg"
    "I took a step forward,{w=0.1} towards the door."

    "Panic flashed across Ryohei’s face."

    play sound "sfx/chime.ogg" volume 0.8
    "He dropped the pendulum,{w=0.1} the crystal clattering against the table."

    #show ryohei panic at center (will add this soon if possible)
    show ryohei serious at center

    voice "voice/ryohei/hey.ogg"
    ryohei "{i}No—wait.{w=0.1} I shouldn’t have—"

    "He looked genuinely terrified,{w=0.1} as if he’d revealed a secret he could never take back."

    pause 1

    "But his panic lasted only a moment."
    "As I reached for the door,{w=0.1} his expression hardened into something desperate and resolute."

    jump pre_ending
