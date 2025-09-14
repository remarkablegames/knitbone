$ renpy.music.set_volume(0.6, channel='music')

transform speak_zoom:
    linear 0.15 zoom 1.025

transform idle_zoom:
    linear 0.15 zoom 1.0

init python:
    def apply_zoom(character_prefix, zoom_type):
        for tag in renpy.get_showing_tags():
            if tag.startswith(character_prefix):
                renpy.show(tag, at_list=[zoom_type])
