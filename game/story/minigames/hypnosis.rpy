label hypnosis_minigame:
    play music "sfx/ticking.ogg"
    show cg hypnosis with dissolve
    call screen hypnosis_minigame


label hypnosis_minigame_win:
    $ trust += 1
    eden "I matched each inhale with an exhale, regaining control over my breath."
    jump session3_hypnosis2


label hypnosis_minigame_lose:
    $ trust -= 1
    eden "My breathing faltered. The steady pattern I’d relied on slipped away."
    jump session3_hypnosis2


screen hypnosis_minigame():
    timer 0.001:
        repeat True
        action Function(slider.update)

    button:
        action Function(slider.stop)
        xalign 0.5
        yalign 0.75

        frame:
            background "#00000099"
            xsize slider.xsize_max
            ysize 50

            bar:
                xsize slider.xsize
                xpos slider.xpos_target

            bar:
                value 1
                xsize slider.xsize
                xpos slider.xpos_current

    textbutton "Stop":
        action Function(slider.stop)
        xalign 0.5
        yalign 0.85


init python:
    class Slider:
        PADDING = 10

        def __init__(self, speed=5, width=100, width_max=1000) -> None:
            self.xsize = width
            self.xsize_max = width_max
            self.xpos_target = renpy.random.randint(0, width_max - width - self.PADDING)
            self.speed = speed
            self.xpos_current = 0
            self.direction = 1

        def update(self) -> None:
            if self.xpos_current <= 0:
                self.direction = 1
            elif self.xpos_current + self.xsize >= self.xsize_max - self.PADDING:
                self.direction = -1
            self.xpos_current += self.speed * self.direction

        def stop(self) -> None:
            xpos_current = self.xpos_current
            xpos_target = self.xpos_target
            xsize = self.xsize

            collision = (
                # left intersection
                (xpos_current >= xpos_target and xpos_current <= xpos_target + xsize) or
                # right intersection
                (xpos_current + xsize >= xpos_target and xpos_current + xsize <= xpos_target + xsize)
            )

            if collision:
                renpy.jump("hypnosis_minigame_win")
            else:
                renpy.jump("hypnosis_minigame_lose")

    slider = Slider()
