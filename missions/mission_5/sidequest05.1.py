#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *
from math import pi
from mission05 import connect_ends

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

def spiral_opp(t):
    return make_point(sin(2*pi*t)*-t, cos(2*pi*t)*t)

# draw_connected_scaled(1000, spiral)
# draw_connected_scaled(1000, spiral_opp)

# (b)
def heart(t):
    return connect_rigidly(spiral, spiral_opp)(t)

draw_connected_scaled(200, heart)
