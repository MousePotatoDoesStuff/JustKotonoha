image spaceroom = "images/cg/monika/monika_room.png"
default persistent.data=dict()

init -10 python:
    koto_random_conversation=list()
    def retrieve_data(k,d):
        if persistent.data is None:
            persistent.data=dict()
        if k not in persistent.data:
            return d
        return persistent.data[k]
    def assign_data(k,d,onlyDefault=False):
        if persistent.data is None:
            persistent.data=dict()
        if onlyDefault and k in persistent.data:
            return
        persistent.data[k]=d
        return




label start:
    python:
        # Traits are on a scale from 0 to 100.
        traits=[
            ['ener',100],   # Energy level
            ['extr',0],     # Extroversion (default is 0 - introverted)
            ['dere',0],     # Similar to an affection level
            ['tsun',0],     # How much of a Natsuki is this character
            ['yand',0],     # Guess what this does...
            ['meta',50]     # Epiphany level
        ]
        for (k,d) in traits:
            assign_data('trait_'+k,d,True)

    # This label configures the anticheat number for the game after Act 1.
    # It is recommended to leave this as-is and use the following in your script:
    #   $ persistent.anticheat = renpy.random.randint(X, Y) 
    #   X - The minimum number | Y - The maximum number
    $ anticheat = persistent.anticheat

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    ## Names of the Characters
    # These variables set up the names of the characters in the game.
    # To add a character, use the following example below: 
    #   $ mi_name = "Mike". 
    # Don't forget to add the character to 'definitions.rpy'!
    $ s_name = retrieve_data('s_name','Sayori')
    $ m_name = retrieve_data('m_name','Monika')
    $ n_name = retrieve_data('m_name','Natsuki')
    $ y_name = retrieve_data('y_name','Yuri')
    $ koto_name = retrieve_data('koto_name','Kotonoha')

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    # This variable c ontrols whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # This variable controls whether Sayori is dead. It is recommended to leave
    # this as-is.
    $ in_sayori_kill = None
    
    # These variables controls whether the player can skip dialogue or transitions.
    $ allow_skipping = True
    $ config.allow_skipping = True
    scene black
    if retrieve_data('started', False):
        call on_restart
    else:
        call on_first_start
    call before_main_menu
label koto_mainloop:
    $ renpy.pause(10)
    call random_choice
    jump koto_mainloop

# This label is where the game 'ends' during Act 1.
label endgame(pause_length=4.0):
    $ renpy.utter_restart()
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
