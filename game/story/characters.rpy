init python:
    renpy.music.register_channel("character", "voice", loop=True, file_prefix="voice/", file_suffix=".ogg")

    def narrator_callback(event, interact=True, **kwargs) -> None:
        if event == "show_done":
            renpy.music.play("narrator", channel="character", relative_volume=0.3)
        elif event == "slow_done":
            renpy.music.stop(channel="character", fadeout=0.2)

    def ryohei_callback(event, interact=True, **kwargs) -> None:
        if event == "begin":
            apply_zoom("ryohei", speak_zoom)
        elif event == "end":
            apply_zoom("ryohei", idle_zoom)
        if event == "show_done":
            renpy.music.play("narrator", channel="character", relative_volume=0.3)
        elif event == "slow_done":
            renpy.music.stop(channel="character", fadeout=0.2)

    def eden_callback(event, interact=True, **kwargs) -> None:
        if event == "begin":
            apply_zoom("eden", speak_zoom)
        elif event == "end":
            apply_zoom("eden", idle_zoom)
        if event == "show_done":
            renpy.music.play("narrator", channel="character", relative_volume=0.3)
        elif event == "slow_done":
            renpy.music.stop(channel="character", fadeout=0.2)

    def nurse_callback(event, interact=True, **kwargs) -> None:
        if event == "begin":
            apply_zoom("nurse", speak_zoom)
        elif event == "end":
            apply_zoom("nurse", idle_zoom)

    def dismiss_callback() -> bool:
        renpy.play("ui/click.ogg")
        return True

    config.say_allow_dismiss = dismiss_callback


define narrator = Character(None, callback=narrator_callback)
define eden = Character("Eden", callback=eden_callback, what_color="#293728", image="eden")
define _eden_ = Character("Eden", callback=eden_callback, what_color="#293728", what_prefix="{i}", what_suffix="{/i}", image="eden")
define ryohei = Character("Ryohei", callback=ryohei_callback, what_color="#272e3f", image="ryohei")
define idk = Character("???", what_color="#FF3E96", what_italic=True)
define unknown = Character("???")
define m = Character("{i}[uname]{/i}")
