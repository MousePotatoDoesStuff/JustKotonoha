screen tell_koto():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Conversation options"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                box_wrap True
                for i in range(cols):
                    vbox:
                        for j in range(10):
                            textbutton _(3.14*i+j)
                            
    text "v[config.version]":
                xalign 1.0 yalign 1.0
                xoffset -10 yoffset -10
                style "main_menu_version"

screen ask_koto():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Conversation options"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                box_wrap True
                for i in range(cols):
                    vbox:
                        for j in range(10):
                            textbutton _(3.14*i+j)
                            
    text "v[config.version]":
                xalign 1.0 yalign 1.0
                xoffset -10 yoffset -10
                style "main_menu_version"