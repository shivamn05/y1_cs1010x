#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))

# Your answer here:
# n = 3

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

# (i) print(thrice(thrice)(add1)(6))
# Explanation: thrice first takes argument of thrice which gives 
# thrice(thrice(thrice(add1)))(6) 
# the inner thrice(add1) will output a function that does add3 
# then thrice(add3) will output a function that does add9 
# then thrice(add9) will output a function that does add27
# so the final output is 27 + 6 = 33

# (ii) print(thrice(thrice)(identity)(compose)) 
# Explanation: The output will be location in memory of the function compose
# thrice(thrice)(identity) will output a thrice(thrice(thrice(identity)))
# which does not output anything. so print will just be print(compose)
# which outputs the location in memory of the function compose

# (iii) print(thrice(thrice)(sq)(1)) 
# Explanation: thrice(thrice)(sq) will output a function that returns x**1024
# 1 ** 1024 is still 1 so answer is 1

# (iv) print(thrice(thrice)(sq)(2))
# Explanation: 2 ** 1024 is a very large number so python may not be able to handle it. if it could the outptut will be 2**1024


###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        if t == 1:
            return 1
        else:
            return 2*(t**2)

    def op(x, y):
        return x + y

    n  = t + 1

    # Do not modify this return statement
    return combine(f, op, n)

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    last_2 = [0,1]
    def f(x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            next_x = last_2[0] + last_2[1]
            last_2.pop(0)
            last_2.append(next_x)
        return next_x
    
    def op(x, y):
        return y

    return combine(f, op, n+1)

# Your answer here:
