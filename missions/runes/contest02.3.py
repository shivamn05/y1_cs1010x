#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.
def half_face(eyes, ears):
    eyes = layer(scale(0.5, eyes))
    eyes = quarter_turn_left(eyes)
    ears = scale(0.9, ears)
    ears = quarter_turn_left(ears)
    final = quarter_turn_right(stack_frac(0.75, ears, eyes))
    return final

def mouth(corner_bb):
    right_half = flip_horiz(corner_bb)
    return layer(beside(corner_bb, right_half))

def layer(pic):
    pic1 = pic
    pic2 = scale(0.5, pic)
    final = overlay(pic2, pic1)
    return final

right_side = half_face(spiral_bb, corner_bb)
left_side = flip_horiz(right_side)
top_face = beside(left_side, right_side)
bottom_face = mouth(corner_bb)
final = stack_frac(0.6, top_face, bottom_face)

anaglyph(final)

# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
