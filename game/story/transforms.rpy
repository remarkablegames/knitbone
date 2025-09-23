transform cover_screen:
    size (1920, 1080)
    fit "cover"


transform flip:
    xzoom -1.0


transform shake:
    linear 0.05 xoffset -12
    linear 0.05 xoffset 12
    linear 0.05 xoffset -6
    linear 0.05 xoffset 6
    linear 0.05 xoffset 0


transform slight_shake:
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -3
    linear 0.05 xoffset 3
    linear 0.05 xoffset 0


transform slow_zoom:
    truecenter
    zoom 1.1
    linear 3.0 zoom 1.0


transform unflip:
    xzoom 1.0
