init python:
    class Countdown:
        DECREMENT = 0.01

        def set(self, seconds: int, jump: str) -> None:
            self.current = seconds
            self.length = seconds
            self.jump = jump

        def decrement(self) -> None:
            self.current -= self.DECREMENT

        def end(self) -> None:
            renpy.hide_screen("countdown")
            renpy.jump(self.jump)

    countdown = Countdown()


screen countdown:
    timer countdown.DECREMENT:
        repeat True
        action If(
            countdown.current > 0,
            true=Function(countdown.decrement),
            false=Function(countdown.end),
        ) 

    bar value AnimatedValue(countdown.current, countdown.length):
        xalign 0.5
        yalign 0.6
        xmaximum 300
