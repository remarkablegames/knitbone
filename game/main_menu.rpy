init python:
    class TrackCursor(renpy.Displayable):
        def __init__(self, child, move_range=50, invert=False):
            super(TrackCursor, self).__init__()
            self.child = renpy.displayable(child)
            self.x = None
            self.y = None
            self.move_range = move_range
            self.invert = invert

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)

            cr = renpy.render(
                self.child,
                width + self.move_range * 2,
                height + self.move_range * 2,
                st,
                at
            )
            cw, ch = cr.get_size()

            x = self.x if self.x is not None else width / 2
            y = self.y if self.y is not None else height / 2

            offset_x = ((x - width / 2) / (width / 2)) * self.move_range
            offset_y = ((y - height / 2) / (height / 2)) * self.move_range

            if self.invert:
                offset_x *= -2
                offset_y *= -2

            offset_x = max(-self.move_range, min(self.move_range, offset_x))
            offset_y = max(-self.move_range, min(self.move_range, offset_y))

            pos_x = -(cw - width) / 2 + offset_x
            pos_y = -(ch - height) / 2 + offset_y

            rv.blit(cr, (pos_x, pos_y))
            return rv

        def event(self, ev, x, y, st):
            if (x != self.x) or (y != self.y):
                self.x = x
                self.y = y
                renpy.redraw(self, 0)

screen main_menu():

    tag menu

    on "show" action Play(0.05, "music", "music/theme1.ogg", loop=True)
    on "hide" action Stop("music", fadeout=1.0)

    add gui.main_menu_background
    add TrackCursor("gui/main_menu.png", move_range=50, invert=True)
    add TrackCursor(Transform("gui/vignette.png", zoom=1.1), move_range=20)

    # Title
    text "KNITBONE":
        xalign 0.5
        yalign 0.45
        size 70
        font "gui/font/pressstart.ttf"
        color "#FFFFFF"
        outlines [(2, "#000000")]

    hbox:
        spacing 200
        xalign 0.5
        yalign 0.75

        textbutton "PLAY":
            action Start()
            style "menu_button"
            activate_sound "ui/click.ogg"

        textbutton "LOAD":
            action ShowMenu("load")
            style "menu_button"
            activate_sound "ui/click.ogg"

    # TODO: Settings button in corner
    # imagebutton:
    #     idle "gui/settings.png"
    #     hover "gui/settings_hover.png"
    #     action ShowMenu('preferences')
    #     xalign 0.98
    #     yalign 0.95
    #     xsize 80
    #     ysize 80

style menu_button is default:
    size 30
    color "#FFFFFF"
    hover_color "#000000"
    xpadding 20
    ypadding 10
    background None
