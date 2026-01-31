#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.
def half_face(eyes, ears):
    eyes = scale(0.5, eyes)
    eyes = quarter_turn_left(eyes)
    ears = scale(0.9, ears)
    ears = quarter_turn_left(ears)
    final = quarter_turn_right(stack_frac(0.75, ears, eyes))
    return final

def mouth(corner_bb):
    right_half = flip_horiz(corner_bb)
    return beside(corner_bb, right_half)

right_side = half_face(circle_bb, corner_bb)
left_side = flip_horiz(half_face(circle_bb, corner_bb))
top_face = beside(left_side, right_side)
bottom_face = mouth(corner_bb)
final = stack_frac(0.6, top_face, bottom_face)

show(final)



