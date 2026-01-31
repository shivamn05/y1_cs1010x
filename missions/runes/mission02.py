#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(pic, n):
    if n == 1:
        return pic
    elif n > 1:
        pic = beside(pic, stack(fractal(pic, n-1), fractal(pic, n-1)))
        return pic

# Test
#show(fractal(make_cross(rcross_bb), 3))
#show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(pic, n):
    # right most stack
    mid = pic
    for _ in range(n-1):        # build right most column
        pic = stack(pic, pic)
    rightmost = pic
    while n > 1:
        n = n - 1
        pic = mid
        for _ in range(n-1): #  build the subsequent column
            pic = stack(pic, pic)
        rightmost = beside(pic, rightmost)
    return rightmost
        
            
            
    

# Test
#show(fractal_iter(make_cross(rcross_bb), 4))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(pic1, pic2, n):
    if n == 1:
        return pic1
    if n == 2:
        return beside(pic1, stack(pic2, pic2))
    elif n > 2:
        pic = beside(pic1, stack(dual_fractal(pic2,pic1,n-1), \
                                 dual_fractal(pic2, pic1, n-1)))
    return pic


# Test
#show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(pic1, pic2, n):
    mid1 = pic1
    mid2 = pic2
    # right most stack
    if n%2 == 0:
        for _ in range(n-1):        # build right most column
            pic2 = stack(pic2, pic2)
        rightmost = pic2
    else:
        for _ in range(n-1):
            pic1 = stack(pic1, pic1)
        rightmost = pic1
    while n > 1:
        n = n - 1
        pic1 = mid1
        pic2 = mid2
        if n%2 == 0: #  build the subsequent column
            for _ in range(n-1):
                pic2 = stack(pic2, pic2)
            rightmost = beside(pic2, rightmost)
        else:
            for _ in range(n-1):
                pic1 = stack(pic1, pic1)
            rightmost = beside(pic1, rightmost)
    return rightmost
        

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(pic1, pic2, pic3, pic4):
    # Fill in code here
    lowest = mosaic(pic1, blank_bb, blank_bb, blank_bb)
    low2 = mosaic(blank_bb, pic2, blank_bb, blank_bb)
    high2 = mosaic(blank_bb, blank_bb, pic3, blank_bb)
    highest = mosaic(blank_bb, blank_bb, blank_bb, pic4)
    low = overlay(low2, lowest)
    top = overlay(highest, high2)
    return overlay(top, low)

def mosaic(pic1, pic2, pic3, pic4):
    # Fill in code here
    right_side = stack(pic4, pic3)
    left_side = stack(pic1, pic2)
    final = beside(right_side, left_side)
    return final

# Test
show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
