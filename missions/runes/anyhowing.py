from runes import *


def create_conc_circle_zf ( radius1 , depth1 , radius2 , depth2 ):
    def square ( x ):
        return x * x
    
    a1_sq = square ( radius1 )
    a2_sq = square ( radius2 )

    def helper (x , y ):
        d_sq = square ( x - 300) + square ( y - 300)
        if d_sq < a1_sq :
            return depth1
        elif d_sq < a2_sq :
            return depth2
        else :
            return 1
    return helper

show ( function_to_painter ( create_conc_circle_zf (90 , 1/3 , 270 , 2/3)))
