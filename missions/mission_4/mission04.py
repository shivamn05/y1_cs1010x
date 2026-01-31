#
# CS1010X --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from missions.mission_4.hi_graph import *

##########
# Task 1 #
##########

# (a)
# unit_line_at_y: (int|float) -> Function

# (b)
# line_a: (int|float) -> Line

# (c)
def vertical_line(point, length):
    return translate(0,y_of(point))(scale_xy(1,length)(lambda t: make_point(x_of(point), t)))

# draw_connected(200, vertical_line(make_point(0.1, 0.1), 0.4))

# (d)
# vertical_line: (Point, int|float) -> Line

# (e)
# print(points_for_curve(5, vertical_line(make_point(0.5, 0.25), 0.5)))
# draw_connected(200, vertical_line(make_point(0.5, 0.25), 0.5))

##########
# Task 2 #
##########

# (a)
# There is a function points_for_curve(n, curve) that outputs n points of the curve and reflected curve. For a small n, add the respective x_of the points from 1 to n. If the function works as expected, the addition should be 1 for all the points.

# (b)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        "your answer here"
        point = curve(t)
        return make_point(-x_of(point), y_of(point))
    return reflected_curve
	
# draw_connected_scaled(200, arc)
# draw_connected_scaled(200, reflect_through_y_axis(arc))
# draw_connected(200, vertical_line(make_point(0.1, 0.1), 0.4))
# draw_connected(200, reflect_through_y_axis(vertical_line(make_point(0.1, 0.1), 0.4)))

# print(points_for_curve(5, arc))
# print(points_for_curve(5, reflect_through_y_axis(arc)))