from time import strftime


def color_clock():
    t = strftime("%H:%M:%S")
    red = 0
    green = 0
    blue = 0
    hour = int(t.split(':')[0])
    min = int(t.split(':')[1])
    sec = int(t.split(':')[2])
    if hour % 3 == 0:
        if min < 30:
            red = 255
            green = 4.25 * min + .07083 * sec
        else:
            red = 255 - 4.25 * min + .07083 * sec
            green = 255
    elif hour % 3 == 1:
        if min < 30:
            green = 255
            blue = 4.25 * min + .07083 * sec
        else:
            green = 255 - 4.25 * min + .07083 * sec
            blue = 255
    elif hour % 3 == 2:
        if min < 30:
            blue = 255
            red = 4.25 * min + .07083 * sec
        else:
            blue = 255 - 4.25 * min + .07083 * sec
            red = 255
    return '%02x%02x%02x' % (red, green, blue)
