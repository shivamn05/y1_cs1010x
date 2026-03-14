# get hundreth place of integers a, b and c
def get_hundredth(a, b, c):
    place = ()
    for num in (a,b,c):
        if type(num) != int or num < 0:
            place += (None,)
        elif num < 100:
            place += (0,)
        else:
            idx = len(str(num)) - 3
            place += (int(str(num)[idx]),)
    return place

#--- TEST CASES ---#
test1 = get_hundredth(1234, 509, 80633)
test2 = get_hundredth(4024, 81, 2713)
test3 = get_hundredth('car', 1345, 564)
# print(test3)

# Standard deviation 
from math import sqrt

def deviation(real_numbers):
    # find mean
    n = len(real_numbers)
    mean = sum(real_numbers) / n
    # find sum of squares of difference between each num and mean
    sos = 0
    for num in real_numbers:
        sos += (num - mean) ** 2
    # divide SOS by n and sqrt result 
    return round(sqrt(sos/n), 2)

#--- TEST CASES ---#
dev1 = deviation((1, 4))
dev2 = deviation((2, 2, 2, 2))
dev3 = deviation((-2, 0, 2, 4, 6))
dev4 = deviation((-5, ))
# print(dev4)

# Elevator - manipulating elevator position
ELEVATOR_SPEED = 2
# input format (lift number, start floor, end floor)
# output format (elevator name, time taken, final floor)
def operate_elevator(t1, t2):
    # elevator 1 
    el1 = (1, 0, 1)
    time1, floor1 = el1[1],el1[2]
    # elevator 2 
    el2 = (2, 0, 1)
    time2, floor2 = el2[1], el2[2]

    for task in (t1, t2):
        to_move = task[0]
        floor_from = task[1]
        floor_to = task[2]
        if to_move == el1[0]:
            # time taken for init -> floor_from + floor_from -> floor_to
            ttime = time1 + (abs(floor1 - floor_from) + abs(floor_from - floor_to)) * ELEVATOR_SPEED
            el1 = (1, ttime, floor_to)
            time1, floor1 = el1[1],el1[2]
        elif to_move == el2[0]:
            # time taken for init -> floor_from + floor_from -> floor_to
            ttime = time2 + (abs(floor2 - floor_from) + abs(floor_from - floor_to)) * ELEVATOR_SPEED
            el2 = (2, ttime, floor_to)
            time2, floor2 = el2[1], el2[2]
    return (el1, el2)

#--- TEST CASES ---#
op1 = operate_elevator((2, 5, 8), (1, 9, 7))
op2 = operate_elevator((1, 9, 7), (1, 3, 10))
op3 = operate_elevator((1, 9, 10), (2, 12, 1))
# print(op2)

# Pascal Triangle using recursion 
# for row n, the kth term will be nCk
from math import comb
def pascal(n):
    if n == 1:
        return ((1,),)
    row = tuple(comb(n-1,k) for k in range(n))
    return pascal(n-1) + (row,)

def pascal_no(n):
    if n == 1:
        return ((1,),)

    prev_triangle = pascal_no(n-1)
    prev_row = prev_triangle[-1]   # prev row is last tuple of the prev triangle


    def build_row(i=0):
        if i == n:  
            return ()   # base case for building row when n rows are formed
        if i == 0 or i == n-1:
            return (1,) + build_row(i+1)    
        return (prev_row[i-1] + prev_row[i],) + build_row(i+1)

    return prev_triangle + (build_row(),)

#--- TEST CASES ---#
p1 = pascal(2)
p2 = pascal(5)
p3 = pascal(7)
# print(p1==((1,), (1, 1)))
# print(p2==((1,), (1, 1), (1, 2, 1), (1, 3, 3, 1), (1, 4, 6, 4, 1)))
# print(p3==((1,), (1, 1), (1, 2, 1), (1, 3, 3, 1), (1, 4, 6, 4, 1), (1, 5, 10, 10, 5, 1), (1, 6, 15, 20, 15, 6, 1)))
