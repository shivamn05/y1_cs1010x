#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def kochize(level):
    if level == 0:
        return unit_line
    else:
        base_curve = kochize(level-1)
        right_curve = (connect_ends(base_curve, rotate(pi/3)(base_curve)))
        left_curve = (connect_ends(rotate(-pi/3)(base_curve), base_curve))
        return put_in_standard_position(connect_ends(right_curve, left_curve))

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

#show_connected_koch(0, 4000)
#show_connected_koch(5, 4000)

##########
# Task 2 #
##########

def snowflake():
    base = kochize(5)
    two_third = gosperize_with_angle(pi/3)(base)
    flipped = rotate(pi)(base)
    return connect_ends(two_third, flipped)

draw_connected_scaled(10000, snowflake())
