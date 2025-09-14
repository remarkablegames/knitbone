# music
$ renpy.music.set_volume(0.6, channel='music')

# callbacks
init python:
    def make_fillvert(img):
        return im.FactorScale(img, 0.4)

## Scale
    def make_sprite(img):
        return make_fillvert(img)


transform speak_zoom:
    linear 0.15 zoom 1.025

transform idle_zoom:
    linear 0.15  zoom 1.0

init python:
    def apply_zoom(character_prefix, zoom_type):
        for tag in renpy.get_showing_tags():
            if tag.startswith(character_prefix):
                renpy.show(tag, at_list=[zoom_type])
