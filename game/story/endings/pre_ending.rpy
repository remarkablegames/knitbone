# KNITBONE - Session 3 & Pre-Ending
# This script continues directly from the end of the previous Session 3 script.

label pre_ending:
    jump pre_ending_start


label pre_ending_start:

    play music "music/terror.ogg" fadein 0.5 volume 0.9
    # play scary ambient
    # show ryohei desperate at center

    show ryohei glare at center
    ryohei "Wait."

    # play sound "sfx/grab_cloth.ogg"

    "His voice was sharp,{w=0.1} cutting through my daze."
    "I felt his hand grab my arm,{w=0.1} his grip surprisingly strong,{w=0.1} almost bruising."

    play sound "sfx/woosh.ogg" volume 0.5
    "I turned back."

    hide eden
    hide ryohei with dissolve
    show cg ryohei scared with dissolve
    "The calm facade was gone,{w=0.1} shattered completely."
    "In its place was raw,{w=0.1} unfiltered desperation."

    ryohei "You can’t leave. Not now."
    ryohei smirk "You saw it too. Don’t you understand what that means?"
    ryohei serious "{cps=25}That...{w=0.1} thing."  

    hide cg ryohei scared with dissolve

    pause 1

    "He pulled me back from the door,{w=0.1} his eyes wide and wild."
    "He wasn’t asking me...{w=0.1} he was pleading with me."
    "He guided me back to the couch and pushed me down gently,{w=0.1} a strange,{w=0.1} reverent care in his otherwise forceful actions."

    play sound "sfx/thud.ogg"
    show bg studio3 with hpunch

    eden "H-{w=0.1}hey!"
    eden "What the hell,{w=0.1} Ryo?!"

    "He ignored my question.{w=0.1} He moved to the table,{w=0.1} and with a click,{w=0.1} lit a match and then lit the candles."

    play sound "sfx/light.ogg"
    scene bg studio4 with dissolve
    show ryohei glare with dissolve

    "As the flames grew,{w=0.1} the room transformed.{w=0.2} It was no longer a studio.{w=0.2} It was an altar."
    "And I was the offering."
    "He sat down across from me again,{w=0.1} the firelight carving deep shadows into his face."
    "He looked older,{w=0.1} burdened by a weight I couldn’t comprehend."

    ryohei serious "What you saw...{w=0.1} Is not just a thing.{w=0.1} It has a name.{w=0.1} A purpose."
    ryohei "It’s one of my debt,{w=0.1} passed down through generations in my family,{w=0.1} all under the guise of enlightenment."
    ryohei glare "My uncle, Callister...{w=0.3} he was the leader.{w=0.2} He called their belief system {cps=25}“Transcendology”."

    "The way he said the word,{w=0.1} it was thick with disgust."

    ryohei "He groomed me.{w=0.1} Not as a nephew,{w=0.1} but as a successor.{w=0.1} He saw the entity as an honor,{w=0.1} a sacred burden."
    ryohei "He taught that our bodies were temporary vessels,{w=0.1} needing purification through “bloodletting” to achieve a higher existence."
    ryohei "He made it sound so beautiful.{w=0.1} The art of {cps=25}{i}ritual."

    # A brief, distorted CG or flashback image could flash here: a younger Ryohei looking up at a charismatic, shadowed figure (Callister).
    # show cg_callister_flash with Dissolve(0.2)
    # pause 0.5
    # hide cg_callister_flash with Dissolve(0.2)

    ryohei "But I saw what it really was.{w=0.1} A machine for offerings."
    ryohei "He wasn’t enlightening people;{w=0.1} he was grooming them for slaughter.{w=0.1} In order to keep the {i}entity{/i} fed."
    ryohei "I couldn’t let him pass it on.{w=0.1} I couldn’t let him choose another victim."
    ryohei "So...{w=0.2} I took it from him."

    play sound "sfx/fire.ogg" volume 1.2
    "The silence in the room was deafening,{w=0.1} broken only by the crackle of the candle wicks."

    eden "What...{w=0.3} do you mean?"

    "{cps=5}..."
    pause 1
    hide ryohei with dissolve
    show cg ryohei scared at slight_shake
    with dissolve

    ryohei "I killed him, Eden."
    ryohei "I killed him!{w=0.1} I plunged his own ritual knife into his chest.{w=0.1} I thought if the leader was gone,{w=0.1} the curse would die with him."

    ryohei "But I was wrong.{w=0.1} It didn’t die.{w=0.1} It just...{w=0.3} transferred.{w=0.1} It latched onto me."

    voice "voice/entity/feed_me.ogg"
    ryohei "Now I carry it.{w=0.1} I hear its whispers.{w=0.1} I feel its hunger."

    show cg ryohei scared at slight_shake
    "He buried his face in his hands,{w=0.1} his shoulders trembling."
    "This was it.{w=0.1} The full,{w=0.1} horrifying truth.{w=0.1} The core of his madness."

    hide cg ryohei scared with dissolve
    "He looked up,{w=0.1} and his eyes were glistening with unshed tears.{w=0.1} But beneath the pain,{w=0.1} there was something else."
    "A chilling,{w=0.1} obsessive focus."
    "It was directed at me."

    ryohei "And that’s why I needed you,{w=0.1} Eden.{w=0.1} I’ve been watching you."
    ryohei "Even back in college."

    eden "{cps=10}What...?"

    ryohei "You were always so quiet.{w=0.1} So self-contained."
    ryohei "While everyone else was so loud,{w=0.1} so desperate to be seen,{w=0.1} you were just...{w=0.2} there."
    ryohei "You were whole.{w=0.1} {cps=25}You were solid."
    ryohei "I was falling apart,{w=0.1} piece by piece,{w=0.1} and you were a fortress."
    ryohei "I envied you for it.{w=0.2} I hated you for it.{w=0.2} And I admired you more than anyone else."
    ryohei "I knew you were the one.{w=0.2} Strong enough to bear the weight.{w=0.2} Quiet enough for it to rest."

    "He leaned forward,{w=0.1} his voice dropping to an intimate,{w=0.1} almost tender whisper."
    "The co-dependent plea of a man drowning."

    ryohei "I was lucky to meet you again."
    ryohei "I knew you were the only one worthy of this gift."
    ryohei "The only one strong enough to see the truth."

    "He slid off his chair and knelt on the floor in front of me."
    "This wasn’t a plea for help.{w=0.1} This was the final step of his plan."

    pause 0.5
    scene cg ryohei kneel 1 with dissolve
    pause 0.5

    "He pulled a knife from his pocket.{w=0.1} The handle had the same vein-like carvings I saw in my vision."
    "He held it out to me on his open palms,{w=0.1} like it was a key."
    "My breath caught in my throat."

    play sound "sfx/heartbeat.ogg"
    "My heart was pounding so hard I could feel it in my ears."

    "This is insane.{w=0.2} Completely insane."
    "But looking at him kneeling there,{w=0.1} offering me this...{w=0.1} {cps=15}purpose...{/cps}{w=0.1} another thought crept in."
    "A horrible,{w=0.1} tempting thought."
    "He’s not asking me to die."
    "He’s asking me to bleed for him.{w=0.1} To become something else."
    "To trade my blood for one filled with this terrible,{w=0.1} powerful thing."
    "What if he’s not crazy?{w=0.1} What if this is the cure for the nothingness I feel every day?"

    ryohei "This gift is meant to be shared.{w=0.2} You saw it.{w=0.2} It saw you.{w=0.2} It has chosen you to be my equal."
    ryohei "Your trouble sleeping,{w=0.1} feeling lost...{w=0.3} that’s not a sickness."
    ryohei "It’s just an opening.{w=0.2} A crack to let the light in.{w=0.2} I’m here to open the door all the way."
    ryohei "Please,{w=0.3} {cps=10}Eden..."

    voice "voice/entity/eden.ogg"
    "His voice was a low,{w=0.1} convincing whisper,{w=0.1} promising a strange and terrible secret."
    "He was asking me to join him in his reality."

    ryohei "Will you accept this honor?"
    ryohei "Will you complete the ritual and become the new vessel?"
    ryohei "Will you sacrifice your blood for me?"

    play sound "sfx/fire.ogg"
    "The question hung in the air,{w=0.1} suspended between the flames of the seven candles."

    play sfx "sfx/heartbeat.ogg"
    "My heart hammered against my ribs."

    "This was the final ritual.{w=0.2} The final choice."

    # This is the final choice point of the game, leading to the different endings.
    menu:

        "What is my choice?"

        "Accept":
            stop music fadeout 1
            jump ending_attack

        "Refuse":
            stop music fadeout 1
            jump ending_sacrifice

        # "???" if trust > 2: # This choice would only appear if certain conditions are met (e.g., high trust stat)
            # jump ending_3
