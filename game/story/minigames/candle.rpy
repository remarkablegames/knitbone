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
        drag:
            child "candle/candle1.png"
            drag_name "1"
            draggable True
            dragged ondrag
            droppable True
            xpos .1
            ypos .5

        drag:
            child "candle/candle2.png"
            drag_name "2"
            draggable True
            dragged ondrag
            droppable True
            xpos .2
            ypos .5

        drag:
            child "candle/candle3.png"
            drag_name "3"
            draggable True
            dragged ondrag
            droppable True
            xpos .3
            ypos .5

        drag:
            child "candle/candle4.png"
            drag_name "4"
            draggable True
            dragged ondrag
            droppable True
            xpos .4
            ypos .5

        drag:
            child "candle/candle5.png"
            drag_name "5"
            draggable True
            dragged ondrag
            droppable True
            xpos .5
            ypos .5
