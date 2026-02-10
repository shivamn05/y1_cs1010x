# QUESTION 1 # 
# a) 12
# b) 18 
# c) 4
# d) 16

# Question 2 #
def my_sum(n):
    if n == 1:
        return 2
    else:
        return (n+1)*n + my_sum(n-1)

# Question 3 #
# Recusive process 
# Time: O(n)
# Space: O(n)

# Question 4 #
def my_sum_iter(n):
    final = 0
    for i in range(n+1):
        final = final + i*(i+1)
    return final

# Iterative process
# Time: O(n)
# Space: O(1)

####################################################
####################################################
# PRE DEFINED FUNCTIONS #
def sum(term, a, next, b):
    if a > b:
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)


def fold(op, f, n):
    if n == 0:
        return f(0)
    else:
        return op(f(n), fold(op, f, n-1))
####################################################
####################################################

# Question 5 # Using sum
def my_sum_sum(n):
    return sum(lambda y: y*(y+1), 1, lambda x: x+1, n)


# Question 6 # Using fold
def my_sum_fold(n):
    return fold(lambda x,y: x+y, lambda z: z*(z+1), n)


# Question 7 #
def sum_iter(term, a, next, b):
    final = 0
    for i in range(a,b+1):
        final += term(i)
        i = next(i)
    return final


# Question 8 #
def fold_iter(op, f, n):
    final = 0
    for i in range(n+1):
        final = op(f(i), final)
    return final 

