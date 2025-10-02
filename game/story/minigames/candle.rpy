default candle = Candle()


label candle_minigame:
    if candle.won():
        show screen candle_minigame
        eden "Yes!"
        hide screen candle_minigame
        jump expression candle.win
    elif candle.lost():
        show screen candle_minigame
        eden "Oh no..."
        hide screen candle_minigame
        jump expression candle.lose

    call screen candle_minigame


screen candle_minigame():
    frame:
        background Solid((0, 0, 0, 100))
        text "{color=#ccc}Remaining Moves: [candle.moves]"
        xpos 30
        ypos 30

    draggroup:
        for index, value in enumerate(candle.values, start=1):
            drag:
                child f"candle/candle {value}.png"
                hover_child f"candle/candle {value} hover.png"
                selected_child f"candle/candle {value} hover.png"
                drag_name candle.stringify_drag_name(index, value)
                draggable not(candle.won() or candle.lost())
                dragged candle.ondrag
                droppable True
                xpos candle.get_snap(index)["x"]
                ypos candle.get_snap(index)["y"]
                hovered [Queue("sound", "ui/mouserelease1.ogg")]


init python:
    class Candle:
        def __init__(self) -> None:
            self.moves = 0
            self.values = []


        def jump(self) -> None:
            renpy.jump("candle_minigame")


        def start(self, moves: int, candles: int, win: str, lose: str) -> None:
            self.moves = moves
            self.values = []
            self.win = win
            self.lose = lose

            while self.values == sorted(self.values):
                self.values = renpy.random.sample(list(range(1, candles + 1)), candles)

            self.jump()


        def won(self) -> bool:
            return self.values == sorted(self.values)


        def lost(self) -> bool:
            return not self.moves


        def ondrag(self, drags, drop) -> None:
            drag = drags[0]
            [drag_index, drag_value] = self.parse_drag_name(drag.drag_name)

            if not drop:
                drag.snap(**self.get_snap(drag_index))
                return

            [drop_index, drop_value] = self.parse_drag_name(drop.drag_name)

            drag.snap(**self.get_snap(drop_index))
            drop.snap(**self.get_snap(drag_index))

            drag.drag_name = self.stringify_drag_name(drop_index, drag_value)
            drop.drag_name = self.stringify_drag_name(drag_index, drop_value)

            self.values[drag_index - 1] = drop_value
            self.values[drop_index - 1] = drag_value

            self.moves -= 1
            renpy.sound.queue("ui/drop_003.ogg", relative_volume=0.5)
            self.jump()


        def get_snap(self, index: int) -> dict:
            return {
                "x": (index - 1) / len(self.values),
                "y": 0.5,
                "delay": 0.2,
            }


        def stringify_drag_name(self, index: int, value: int) -> str:
            return f"{index},{value}"


        def parse_drag_name(self, name: str) -> dict:
            [index, value] = name.split(",")
            return [int(index), int(value)]
