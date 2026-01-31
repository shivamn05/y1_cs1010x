#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi
import time

##########
# Task 1 #
##########

def tree(n, pic):
    # Fill in code here
    if n == 1:
        return pic
    else:
        picture = overlay_frac((n-1)/n, tree(n-1, scale((n-1)/n, pic)), \
                               pic)
    return picture

# Test
#show(tree(4, circle_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def helix(pic, n):
    # Fill in code here
    radius = 1/2 - 1/n
    angle = (2 *pi) /n
    pic = scale(2/n, pic)
    pic = flip_vert(quarter_turn_left(pic))
    picture = blank_bb
    for i in range(n):
        j = i + 1
        current = j * angle
        icon = pic
        #fraction = (n-i-1)/(n-i)
        fraction = 1/j
        if 0 < current <= pi/2 and j==1: # first pic needs to take over blank
            icon = translate(radius * cos(current), -radius * sin(current),\
                             icon)
            picture = icon
        elif 0 < current <= pi/2:
            icon = translate(radius * cos(current), -radius * sin(current),\
                             icon)
            picture = overlay_frac(fraction, icon, picture)
        elif pi/2 < current <= pi:
            icon = translate(-radius * cos(pi-current), - radius * \
                             sin(pi-current), icon)
            picture = overlay_frac(fraction, icon, picture)
        elif pi < current <= (3 * pi) / 2:
            icon = translate(-radius * cos(current - pi), radius * \
                             sin(current - pi), icon)
            picture = overlay_frac(fraction, icon, picture)
        elif (3 * pi)/2 < current <= 2 * pi:
            icon = translate (radius * cos(2* pi - current), radius * \
                              sin(2 * pi - current), icon)
            picture = overlay_frac(fraction, icon, picture)
    picture = quarter_turn_left(picture)
    picture = flip_vert(picture)
    return picture

# Test
#show(helix(make_cross(rcross_bb), 9))
#show(helix(circle_bb, 9))
show(helix(corner_bb, 9))
