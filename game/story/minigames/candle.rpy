label candle_minigame:
    call screen candle_minigame


init python:
    class Candle:
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


        def get_snap(self, index: int) -> dict:
            return {
                "x": index / 10 * 1.5,
                "y": 0.5,
                "delay": 0.2,
            }


        def stringify_drag_name(self, index: int, value: int) -> str:
            return f"{index},{value}"


        def parse_drag_name(self, name: str) -> dict:
            [index, value] = name.split(",")
            return [int(index), int(value)]


    candle = Candle()


screen candle_minigame():
    draggroup:
        for index, value in enumerate([2, 3, 4, 5, 1], start=1):
            drag:
                child f"candle/candle {value}.png"
                hover_child f"candle/candle {value} hover.png"
                selected_child f"candle/candle {value} hover.png"
                drag_name candle.stringify_drag_name(index, value)
                draggable True
                dragged candle.ondrag
                droppable True
                xpos candle.get_snap(index)["x"]
                ypos candle.get_snap(index)["y"]
