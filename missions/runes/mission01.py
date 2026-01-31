#
# CS1010X --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

def mosaic(pic1, pic2, pic3, pic4):
    # Fill in code here
    right_side = stack(pic4, pic3)
    left_side = stack(pic1, pic2)
    final = beside(right_side, left_side)
    return final


# Test
show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))

##########
# Task 2 #
##########

def simple_fractal(pic1):
    # Fill in code here
    left_side = stack(pic1, pic1)
    final = beside(pic1, left_side)
    return final

# Test
#show(simple_fractal(make_cross(rcross_bb)))


