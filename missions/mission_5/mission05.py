#
# CS1010X --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

def connect_ends(curve1, curve2):
    connect_at_pt1 = curve1(1)
    connect_at_pt2 = curve2(0)
    endx1 = x_of(connect_at_pt1)
    endy1 = y_of(connect_at_pt1)
    endx2 = x_of(connect_at_pt2)
    endy2 = y_of(connect_at_pt2)
    curve2 = translate(endx1-endx2, endy1-endy2)(curve2)
    return connect_rigidly(curve1, curve2)

# draw_connected_scaled(200, connect_ends(arc, unit_line))
# draw_connected_scaled(200, connect_ends(translate(5,5)(arc), translate(1,1)(unit_line)))

##########
# Task 2 #
##########
def gosperize ( curve ):
    scaled_curve = scale ( sqrt ( 2 )/ 2 )( curve )
    left_curve = rotate ( pi / 4 )( scaled_curve )
    right_curve = translate(0.5, 0.5)(rotate ( - pi / 4 )( scaled_curve ))
    return connect_rigidly ( left_curve , right_curve )

def gosper_curve ( level ):
    return repeated ( gosperize , level )( unit_line )

def show_connected_gosper ( level ):
    squeezed_curve = squeeze_curve_to_rect (-0.5, -0.5, 1.5, 1.5 )( gosper_curve ( level ))
    draw_connected ( 200 , squeezed_curve )


def show_points_gosper(level, num_points, initial_curve):
    squeezed_curve = squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5)(repeated(gosperize, level)(initial_curve))
    draw_points(num_points,squeezed_curve)

# show_points_gosper(7, 1000, arc)

##########
# Task 3 #
##########

from math import sqrt

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        scaled_curve = scale(sin(theta))(curve_fn)
        left_curve = rotate(theta)(scaled_curve)
        right_curve = translate(0.5, 0.5)(rotate(-theta)(scaled_curve))
        return put_in_standard_position(connect_ends(left_curve, right_curve))
    return inner_gosperize

# draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
# draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
