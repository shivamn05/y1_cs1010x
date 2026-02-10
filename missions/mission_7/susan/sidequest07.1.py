#
# CS1010X --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    flip_coins(table, get_table_state(table))
    return check_solved(table)

# test:
# t2_1 = create_table(2)
# solve_trivial_2(t2_1)
# print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_1_run = create_table(2)
# run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_1_susan = create_table(2)
# Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    state = get_table_state(table)
    flip_coins(table, state)
    return check_solved(table)

# test:
# t4_2 = create_table(4)
# solve_trivial_4(t4_2)
# print(check_solved(t4_2))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t4_2_run = create_table(4)
# run(t4_2_run, solve_trivial_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_2_susan = create_table(4)
# Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    if check_solved(table) == False:
        flip_coins(table, (1,0))
    return check_solved(table)

# test:
# t2_3 = create_table(2)
# solve_2(t2_3)
# print(check_solved(t2_3))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_3_run = create_table(2)
# run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):
    A = (1,0,1,0)
    B = (1,1,0,0)
    C = (1,0,0,0)
    moves = [A,B,A,C,A,B,A]
    for move in moves:
        flip_coins(table, move)
        if check_solved(table) == True:
            break
    return check_solved(table)

# test:
# t4_4 = create_table(4)
# solve_4(t4_4)
# print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t4_4_run = create_table(4)
# run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_4_susan = create_table(4)
# Susan(t4_4_susan)

########################################################





##########
# Task 5 #
##########

def pattern(lis):
    length = len(lis)
    for i in range(length):
        lis += [tuple(list(lis[i]) + [0]*length)] #duplicate the "1" down and forms "0" beside it
        lis[i] = tuple(lis[i]*2) #duplicate original "1" to its right
    return lis

def diff_pat(lis, n):
    if n == 1:
        return [lis[n]]
    return diff_pat(lis, n-1) + [lis[n]] + diff_pat(lis, n-1)

def solve(table):
    size = get_table_size(table)
    n = int(log10(size) / log10(2))
    A = (1,1)
    B = (1,0)
    if n == 1:
        if check_solved(table) == False:
            flip_coins(table, B)
        return check_solved(table)
    moves = [A, B]
    for _ in range(n-1):
        moves = pattern(moves)
    #use the other pattern
    #for curr in moves:
        #print(str(curr) + "\n")
    order = diff_pat(moves,len(moves)-1)
    for move in order:
        flip_coins(table, move)
        if check_solved(table) == True:
            break
    return check_solved(table)


# test:
# t4_5 = create_table(4)
# solve(t4_5)
# print(check_solved(t4_5))

# t8_5 = create_table(8)
# solve(t8_5)
# print(check_solved(t8_5))

t16_5 = create_table(16)
solve(t16_5)
print(check_solved(t16_5))

# Note: It is not advisable to execute run() if the table is large.
