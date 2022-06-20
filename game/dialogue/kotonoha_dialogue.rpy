init -9 python:
    koto_random_conversation+=[
        'random_chatter_1',
        'random_chatter_2',
        'random_question_1'
    ]
    if retrieve_data('religious',False):
        koto_random_conversation += ['religious']


# Starting up the game for the first time
label on_first_start:
    stop music fadeout 2.0
    play music wind fadein 1.0 volume 2.0
    window hide
    scene black with dissolve_scene_full
    window show
    # "Here I am."
    # "To be honest, I'm somewhat nervous."
    # "One week ago today, I made a big commitment."
    # "I agreed to help out a classmate of mine. Kotonoha."
    # "Truth be told, I've never really known Kotonoha that well."
    # "She's a clubmate of mine, but we hardly have much in common."
    # "At least, nothing that I know of. She never really told me what she liked to do."
    # "I take a deep breath, and look at my watch."
    # "She's late."
    # "One day, Kotonoha approached me."
    "...and here you are."
    "A week ago, you made a big commitment."
    "You agreed to help out a classmate of yours."
    "Truth be told, you've never really known her that well..."
    "She's a clubmate of yours, but you hardly have much in common."
    "At least, nothing that you know of. She never really told you what she liked to do."
    "One day, Kotonoha approached you."
    stop music fadeout 1.0
    play music t9 fadein 2.0
    scene bg corridor with open_eyes
    show kotonoha toward nerv at t11
    ko "...[player]?"
    ko ce "(Oh gosh... This is embarrassing.)"
    ko "(Brave face, Koto...)"
    ko happ oe om "[player], I was wondering, could you, um, help me out with something?"
    mc "Huh? Help you out with what?"
    ko ce "Well, to be honest, it's a little bit embarrassing."
    ko neut oe cm "You probably noticed that I..."
    show kotonoha worr at d11
    ko "Don't have very many friends."
    mc "I guess?"
    ko "Well, I was wondering if you could sort of help me to..."
    show kotonoha happ at h11
    ko "Come out of my shell, a little bit?"
    mc "How do you mean?"
    ko nerv "Well... I was wondering if maybe we could just... Hang out from time to time, y'know?"
    ko happ "At the park nearby! It's usually pretty quiet."
    mc "Sure, I don't see why not."
    mc "What's your phone number? I've gotta go, we can talk about this when I get home."
    ko "Oh, it's..."
    scene black with close_eyes
    stop music fadeout 2.0
    pause(2.0)
    play music wind fadein 1.0 volume 2.0
    "She should be here any minut--{nw}"
    ko "[player]?"
    scene bg park
    show black zorder 10
    show kotonoha toward casual nerv at tdesk
    hide black with open_eyes
    ko "Seems like you sort of... Zoned out a little bit there."
    "Kotonoha giggles softly."
    ko happ "Thanks for showing up."
    return

# Random chatter
label random_chatter_1:
    ko "You know, before I met you and the other girls, all I really had was Mori. Everything was peaceful."
    ko "But then I got bored after a while."
    ko "I wanted something new, and I couldn't just buy it either."
    ko "That feeling got stronger and stronger every day until it almost became unbearable."
    ko "It was almost too much."
    ko "Then suddenly the feeling just... stopped."
    ko "Then I realized that the feeling disappeared because I met the other girls."
    ko "But more importantly, I met you. You were the person that took all the negative feelings away from me."
    ko "I always wanted to be with you, but not in a creepy way of course."
    ko "I'm not a yandere!"
    ko "It just happened, and I can't explain it."
    return

label random_chatter_2:
    ko "I was looking on Reddit one time and saw a post on r/askreddit."
    ko "It was a question asking, \"What is one thing you have been taught that you will never/will never forget?\""
    ko "Apart from the weird wording of the question, the comments were somewhat different."
    ko "Sure there were the usual lefty-loosey, righty-tighty."
    ko "There was one detailed response on how no one in America is interested in equality."
    ko "But then the OP's comment was something really random."
    ko "It was what USB stood for. Universal Serial Bus."
    ko "I understand lefty-loosey, righty-tighty."
    ko "Yes, I can see people never forgetting that people don't care about equality."
    ko "But USB?"
    ko "It's completely random."
    ko "There is no benefit in life knowing what USB stands for."
    ko "Personally,"
    return

label random_question_1:
    ko "Have you ever heard of a \"near death experience\"?"
    ko "It's just what it sounds like. An experience where you... Nearly die."
    ko "I actually had a near death experience, when I was a kid."
    ko "I had snuck out late at night, because, y'know, I didn't know any better."
    ko "Well... When I was walking, I decided to cross the street."
    ko "Right before I stepped off of the curb, a car flew right past me."
    ko "I didn't see the guy coming, and he was definitely speeding."
    ko "And I was just standing there, thinking to myself that if I was walking just a little bit faster..."
    ko "I'd be dead."
    ko "Of course, since I was just a little girl, I screamed and ran all the way back home."
    ko "When I told my dad what happened, he was mad, of course he was."
    ko "I was grounded for a while, for sneaking out of the house."
    ko "But when I was grounded, I was thinking..."
    ko "If that car {i}had{/i} hit me..."
    ko "What would've happened?"
    hide window
    pause 2.0
    show window
    menu:
        ko "[player], are you religious?"
        "Yes":
            $ persistent.data['religious'] = True
        "No":
            $ persistent.data['religious'] = False
    ko "I wasn't really religious before that happened."
    ko "I mean, I went to meetings and all that,"
    ko "But I didn't really care. I was just a kid."
    ko "That changed, though. I cared a lot more after that, y'know?"
    if persistent.data['religious']:
        ko "I didn't know that you were religious, [player], it's nice to learn things about you."

# IF THE PLAYER HAS CHOSEN "I AM RELIGIOUS" OPTION SOMETIME BEFORE
label religious:
    ko "Monika once said to me that she had what's called an epiphany."
    ko "At the time I didn’t understand what Monika said and it stayed that way until Friday 26th of November 2021."
    ko "That day I will always remember clearly."
    ko "It was a day where apparently the God looking after us decided that I deserved a bit of punishment."
    ko "It was last period of the day, Maths, and I was just staring at my textbook. I had a thought."
    ko 'Why is life repeating itself?'
    ko "I thought about it more like how I wake up, get ready, go to school, go home, repeat."
    ko "It was then I realized that there was some weird text in the top left of my field of vision."
    ko "It said Execute action Afternoon_Bell"
    # Writer’s note, if this isn’t coding, then is it able to be changed when putting this in?
    # You want this to be formatted as code? Or shown in the console element? Or run as code? -MousePotato"
    ko "As soon as I read it, the bell went signalling the school that school was over for the day."
    ko "That’s when it hit me."
    ko "Life is repeating itself."
    ko "I understood what Monika said that day."
    ko "It was like something just snapped in my brain."
    return