#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *
from math import pi

##########
# Task 1 #
##########
# your answer here
# unit_circle is a smoother curve than alternative_unit_circle. alt uses t*t while unit_circle just uses t. for small t, t*t is approximately equal thus the points are almost on a horizontal as the y values are approx equal. hence the start of the curve has steps. 

##########
# Task 2 #
##########

# (a)
def spiral(t):
    return make_point(sin(2*pi*t)*t, cos(2*pi*t)*t)

# draw_connected_scaled(1000, spiral)

# (b)
def heart(t):
    curve1 = scale(0.5)(spiral)(t)
    curve2 = spiral(t)
    curve2 = (revert(curve2))(t)
    curve2 = rotate(pi/2)(curve2)(t)
    combined = connect_rigidly(curve1, curve2)
    return curve2

draw_connected_scaled(1000, heart)
