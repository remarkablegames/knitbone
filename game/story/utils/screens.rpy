#########

# :) forum interface
#-------------------------------------------------------------

#-------------------------------------------------------------

style input_username:
    color "#FFFFFF80" 
    size 28
    italic True

init:
    style forum_frame is frame:
        background Frame("gui/textbox.png", 10, 10)
        padding (30, 30)
        xmargin 0
        ymargin 0

    style forum_username:
        size 40
        color "#222222"
        bold False

    style forum_tags:
        size 24
        color "#666666"
        italic True

    style forum_notes:
        size 22
        color "#444444"

    style forum_like:
        size 24
        color "#E05555"

    style forum_dialogue:
        size 30
        color "#000000"
        line_spacing 8
        kerning 1
        layout "subtitle"
        text_align 0.0
        slow_cps 20

#-------------------------------------------------------------
screen forum_post():
    tag forum_post
    zorder 1

    $ sw = config.screen_width
    $ sh = config.screen_height

    add FORUM_BG
    add Solid("00000022")

    # Message list container
    viewport:
        xpos 0.05
        ypos 0.05
        xsize 0.9 * sw
        ysize 0.9 * sh
        scrollbars "vertical"
        mousewheel True
        draggable True

        vbox:
            spacing 40
            for msg in message_history:
                hbox:
                    spacing 20

                    add msg.avatar:
                        zoom 0.1
                        ypos 0.0

                    vbox:
                        spacing 8

                        text msg.username style "forum_username"

                        frame:
                            style "forum_frame"
                            xsize 1400
                            has vbox
                            text msg.text style "forum_dialogue"

                        hbox:
                            spacing 20
                            text msg.tags style "forum_tags"
                            text "· %d notes" % msg.notes style "forum_notes"
