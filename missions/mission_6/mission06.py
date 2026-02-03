#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        scaled_curve = scale(sin(theta))(curve_fn)
        left_curve = rotate(theta)(scaled_curve)
        right_curve = translate(0.5, 0.5)(rotate(-theta)(scaled_curve))
        return put_in_standard_position(connect_ends(left_curve, right_curve))
    return inner_gosperize

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def average_5(a, b, c, d, e):
    return (a+b+c+d+e)/5
# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(1000)(0.1), 500)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

#for i in range(5):
    #print(profile_fn(lambda: gosper_curve(200)(0.1), 200))

# Time measurements
#######################################
# Test number   ##      Time (ms)     #
#######################################
#      1        ## 118.43758300528862 #
#######################################
#      2        ## 117.16283299756469 #
#######################################
#      3        ## 115.38345800363459 #
#######################################
#      4        ## 116.77141700056382 #
#######################################
#      5        ## 115.65279099886538 #
#######################################
# Average time: 116.68161640118342

# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

#for i in range(5):
    #print(profile_fn(lambda: gosper_curve_with_angle(200, lambda lvl:pi/4)(0.1), 200))

#######################################
# Test number   ##      Time (ms)     #
#######################################
#      1        ## 112.34925000462681 #
#######################################
#      2        ## 114.16483300126856 #
#######################################
#      3        ## 109.94504099653568 #
#######################################
#      4        ## 110.263082999154   #
#######################################
#      5        ## 107.42900000332156 #
#######################################
# Average time: 110.83024140098132

# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

#for i in range(5):
    #print(profile_fn(lambda: your_gosper_curve_with_angle(200, lambda lvl:pi/(2+lvl))(0.1), 200))

#######################################
# Test number   ##      Time (ms)     #
#######################################
#      1        ## 43146.29933299875  #
#######################################
#      2        ## 42598.86820799875  #
#######################################
#      3        ## 42395.01758299593  #
#######################################
#      4        ## 42564.14179199783  #
#######################################
#      5        ## 42357.68991700024  #
#######################################
# Average time: 42612.4033665983

# Conclusion:
# From the result, gosper_curve_with_angle (more customisable) is faster than gosper_curve (most customized) but slower than your_gosper_curve_with_angle (most customisable). This might be because gosper_curve calls repeated which calls compose, which adds more time compared to gosper_curve_with_angle, which does not stack the previous outputs. However, comparing gosper_curve_with_angle to your_gosper_curve_with_angle, it makes sense that the most customisable function takes a slower time since your_gosper_curve_with_angle calls slightly more functions for the custom angles.

##########
# Task 2 #
##########

#  1) Yes it does

#  2) For joe_rotate, curve(t) is evaluated twice everytime joe_rotate is called. Since gosper curve is recursive, it works bottom up. So when evaluating curve(t) twice, the number of evaluations for level n is 2^n. However, if pt is used, curve(t) only has to be called once for each n.

##########
# Task 3 #
##########
# draw_connected_scaled(500, gosper_curve(5))
original_rotate = rotate
replace_fn(rotate,joe_rotate)
trace(x_of)
gosper_curve(5)(0.5)
untrace(x_of)
gosper_curve(5)(0.5)

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1           3             4
#                      2           5             10
#                      3           7             22
#                      4           9             46
#                      5           11            94
#
#  Evidence of exponential growth in joe_rotate.
