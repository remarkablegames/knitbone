init python:
    def narrator_callback(event, interact=True, **kwargs):
        if event == "show":
            renpy.music.play("narrator.ogg", channel="sound", loop=True)
            renpy.music.set_volume(0.3, delay=0, channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=0.2)

    def ryohei_callback(event, interact=True, **kwargs):
        if event == "begin":
            apply_zoom("ryohei", speak_zoom)
        elif event == "end":
            apply_zoom("ryohei", idle_zoom)
        if event == "show":
            renpy.music.play("narrator.ogg", channel="sound", loop=True)
            renpy.music.set_volume(0.3, delay=0, channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=0.2)

    def eden_callback(event, interact=True, **kwargs):
        if event == "begin":
            apply_zoom("eden", speak_zoom)
        elif event == "end":
            apply_zoom("eden", idle_zoom)
        if event == "show":
            renpy.music.play("narrator.ogg", channel="sound", loop=True)
            renpy.music.set_volume(0.3, delay=0, channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=0.2)

    def nurse_callback(event, interact=True, **kwargs):
        if event == "begin":
            apply_zoom("nurse", speak_zoom)
        elif event == "end":
            apply_zoom("nurse", idle_zoom)

    def dismiss_callback():
        renpy.play("click.ogg")
        return True

    config.say_allow_dismiss = dismiss_callback


define narrator = Character(None, callback=narrator_callback)
define e = Character("Eden", callback=eden_callback, what_color="#293728")
define ei = Character("Eden", callback=eden_callback, what_color="#293728", what_prefix="{i}", what_suffix="{/i}")
define r = Character("Ryohei", callback=ryohei_callback, what_color="#272e3f")
define idk = Character("???", what_color="#FF3E96", what_italic=True)
define unknown = Character("???")
define m = Character("{i}[uname]{/i}")
