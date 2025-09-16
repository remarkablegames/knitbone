label candle_minigame:
    call screen candle_minigame


init python:
    def ondrag(drags, drop) -> None:
        drag = drags[0]
        drag_index = int(drag.drag_name)

        if not drop:
            drag.snap(drag_index/10, 0.5, 0.2)
            return

        drop_index = int(drop.drag_name)
        drag.snap(drop_index/10, 0.5, 0.2)
        drop.snap(drag_index/10, 0.5, 0.2)
        drag.drag_name = drop_index
        drop.drag_name = drag_index


screen candle_minigame():
    draggroup:
        for index in range(1, 6):
            drag:
                child f"candle/candle{index}.png"
                drag_name index
                draggable True
                dragged ondrag
                droppable True
                xpos (index / 10)
                ypos .5
