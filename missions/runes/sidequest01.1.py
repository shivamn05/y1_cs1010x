#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def egyptian(pic, n):
    # Fill in code here
    if n < 3:
        return pic
    else:
        # Top row
        row = besiden(n, pic)
        # Middle column of n-2
        column = stackn(n-2, pic)
        # Combining middle column of n-2 and middle picture 
        middle_left = left(n, column, pic)
        # Getting the middle sideways
        middle = stack_frac(
            (n-1)/n, middle_left, quarter_turn_left(column))
        # Middle final
        middle_final = quarter_turn_right(middle)
        # Combining middle and top and bottom rows
        middle_top = stack_frac(1/(n-1), row, middle_final)
        final = stack_frac((n-1)/n, middle_top, row)
    return final

def besiden(n, painter):
    if n==1:
        return painter
    else:
        return quarter_turn_right(
            stack_frac(
                1/n, quarter_turn_left(painter), stackn(n-1,
                quarter_turn_left(painter))))

def left(n, pic1, pic2):
    left_side = stack_frac(
        1/(n-1), quarter_turn_left(pic1), quarter_turn_left(pic2))
    return left_side
    

# Test
show(egyptian(make_cross(rcross_bb), 5))
