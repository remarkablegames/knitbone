# KNITBONE - Session 3 & Pre-Ending
# This script continues directly from the end of the previous Session 3 script.

label pre_ending:
    jump pre_ending_start


label pre_ending_start:

    #play scary ambient
    #show ryohei desperate at center
    show ryohei glare at center
    ryohei "Wait."
    # play sound "sfx/grab_cloth.ogg"

    "His voice was sharp, cutting through my daze. I felt his hand grab my arm, his grip surprisingly strong, almost bruising."
    "I turned back. The calm facade was gone, shattered completely. In its place was raw, unfiltered desperation."

    ryohei "You can't leave. Not now."
    ryohei smirk "You saw it too. Don't you understand what that means?"
    ryohei serious "That...thing."

    "He pulled me back from the door, his eyes wide and wild. He wasn't asking me... he was pleading with me."
    "He guided me back to the couch and pushed me down gently, a strange, reverent care in his otherwise forceful actions."

    show bg studio3 with hpunch
    eden "H-hey!"
    eden "What the hell, Ryo?!"

    "He ignored my question. He moved to the table, and with a click, lit a match and then lit the candles."
    scene bg studio4 with dissolve

    "As the flames grew, the room transformed. It was no longer a studio. It was an altar. And I was the offering."
    "He sat down across from me again, the firelight carving deep shadows into his face. He looked older, burdened by a weight I couldn't comprehend."

    ryohei "What you saw... Is not just a thing. It has a name. A purpose."
    ryohei " It's one of my debt, passed down through generations in my family, all under the guise of enlightenment."
    ryohei "My uncle, Callister… he was the leader. He called their belief system 'Transcendology'."

    "The way he said the word, it was thick with disgust."

    ryohei "He groomed me. Not as a nephew, but as a successor. He said the entity was an honor, a sacred burden."
    ryohei "He taught that our bodies were temporary vessels, needing purification through 'bloodletting' to achieve a higher existence."
    ryohei "He made it sound so beautiful. The art of {i}ritual."

    # A brief, distorted CG or flashback image could flash here: a younger Ryohei looking up at a charismatic, shadowed figure (Callister).
    # show cg_callister_flash with Dissolve(0.2)
    # pause 0.5
    # hide cg_callister_flash with Dissolve(0.2)

    ryohei "But I saw what it really was. A machine for offerings. He wasn't enlightening people; he was grooming them for slaughter. To keep the {b}entity{/b} fed."
    ryohei "I couldn't let him pass it on. I couldn't let him choose another victim."
    ryohei "So… I took it from him."

    "The silence in the room was deafening, broken only by the crackle of the candle wicks."

    eden "What...{w=0.3} do you mean?"

    ryohei smirk "I killed him. I plunged his own ritual knife into his chest. I thought if the leader was gone, the curse would die with him."
    ryohei "But I was wrong. It didn't die. It just… transferred. It latched onto me. Now I carry it. I hear its whispers. I feel its hunger."

    "He buried his face in his hands, his shoulders trembling. This was it. The full, horrifying truth. The core of his madness."
    "He looked up, and his eyes were glistening with unshed tears. But beneath the pain, there was something else. A chilling, obsessive focus. It was directed at me."

    ryohei "And that’s why I needed you, Eden. I've been watching you. Even back in college."

    eden "What…?"

    ryohei "You were always so quiet. So self-contained. While everyone else was so loud, so desperate to be seen, you were just… there. You were whole. Solid."
    ryohei "I was falling apart, piece by piece, and you were a fortress. I envied you. I hated you for it. And I admired you more than anyone."
    ryohei "I knew you were the one. Strong enough to bear the weight. Quiet enough for it to rest."

    "He leaned forward, his voice dropping to an intimate, almost tender whisper. The co-dependent plea of a man drowning."

    ryohei "I was lucky to meet you again. I knew you were the only one worthy of this gift. The only one strong enough to see the truth."

    "He slid off his chair and knelt on the floor in front of me. This wasn't a plea for help. This was the final step of his plan."
    "He pulled a knife from his pocket. The handle had the same vein-like carvings I saw in my vision. He held it out to me on his open palms, like it was a key."
    "My breath caught in my throat. My heart was pounding so hard I could feel it in my ears. This was insane. Completely insane."
    "But looking at him kneeling there, offering me this... purpose... another thought crept in. A horrible, tempting thought."
    "He's not asking me to die. He's asking me to be reborn. To become something else. To trade my empty life for one filled with this terrible, powerful thing."
    "What if he's not crazy? What if this is the cure for the nothingness I feel every day?"

    #show ryohei kneeling at center with move
    hide eden
    ryohei "This gift is meant to be shared. You saw it. It saw you. It has chosen you to be my equal."
    ryohei "Your trouble sleeping, feeling lost… that's not a sickness. It's just an opening. A crack to let the light in. I'm here to open the door all the way."
    ryohei "Please, Eden....."

    "His voice was a low, convincing whisper, promising a strange and terrible secret. He was asking me to join him in his reality."

    ryohei "Will you accept this honor? Will you complete the ritual and become the new vessel?"
    ryohei "Will you do the sacrifice for me?"

    "The question hung in the air, suspended between the flames of the seven candles. My heart hammered against my ribs. This was the final ritual. The final choice."

    # This is the final choice point of the game, leading to the different endings.
    menu:
        "Take the knife.":
            jump ending_attack
        "“No.”":
            jump ending_sacrifice
        "???": # This choice would only appear if certain conditions are met (e.g., high trust stat)
            #jump ending_3
            jump end

    return
