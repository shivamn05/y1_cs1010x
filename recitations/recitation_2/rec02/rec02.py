#--- QUESTION 1 ---#

# CONSTANTS
PRICE_NORMAL = 2
PRICE_COMBO = 4

def biggie_size(meal):
    return meal + 4

def unbiggie_size(meal):
    return meal - 4

def is_biggie_size(meal):
    if 4 < meal <= 8:
        return True
    return False 

def combo_price(meal):
    if is_biggie_size(meal):
        return (meal-4) * PRICE_COMBO
    else:
        return (meal) * PRICE_NORMAL

def empty_order():
    return 0

def add_to_order(old_order, meal):
    return str(old_order) + str(meal)


"""
(a) Write a recursive function called order_size which takes an order and returns
the number of combos in the order
"""
def order_size(order):
    if len(str(order)) == 1:
        return 1
    else:
        return 1 + order_size(order//10)
    
# Time complexity: O(k)
# Space complexity: O(k)

# print(order_size(127566))

"""
(b) Write an iterative version of order_size.
"""
def order_size_iter(order):
    num = 0
    while order >= 1:
        order = order // 10
        num += 1
    return num

# Time complexity: O(k)
# Space complexity: O(1)

# print(order_size_iter(1275))

"""
(c) Write a recursive function called order_cost which takes an order and returns
the total cost of all the combos.
"""
def order_cost(order):
    order = str(order)
    if len(str(order)) == 0:
        return 0
    else:
        first = combo_price(int(order[0])) 
        order = order[1:]
        if len(order) == 0:
            return 0
        return first + order_cost(int(order))

print(order_cost(12345))

"""
(d) Write an iterative version of order_cost.
"""
def order_cost_iter(order):
    cost = 0
    for i in range(len(str(order))):
        cost += combo_price(int(str(order)[i]))
    return cost
    
# print(order_cost_iter(12346))

"""
(e) Write a function called add_orders which takes two orders and returns a new
order that is the combination of the two. For example, add_orders (123,234) ->
123234. Note that the order of the combos in the new order is not important
as long as the new order contains the correct combos. add_orders(123,234) ->
122334 would also be acceptable.
"""
def add_orders(order1, order2):
    return str(order1) + str(order2)

# print(add_orders(123,234))

#--- QUESTION 2 ---#
# (a) O(n^2)
# (b) O(n)
# (c) O(3^n * n^2)

#--- QUESTION 3 ---#
# Running time: O(n)
# Space: O(n)

#--- QUESTION 4 ---#
def fact_iter(n):
    total = 1
    for i in range(n):
        i += 1
        total *= i
    return total

# Running time: O(n)
# Space: O(1)
# print(fact_iter(4))

#--- QUESTION 5 ---#
# Running time: O(n^2)
# Space: O(n)

#--- QUESTION 6 ---#
"""
(a) Assume you have a function is_divisible(n, x) which returns True if n is divisible
by x. It runs in O(n) time and O(1) space. Write a function is_prime which takes a
number and returns True if it's prime and False otherwise.
"""
def is_divisible(n,x):
    return not n%x

def is_prime(n):
    for i in range(2, n):    
        if is_divisible(n,i):
            return False
    return True

# Running time: O(n^2)
# Space: O(1)

#--- QUESTION 7 ---#
def find_e_iter(n):
    final = 0
    for i in range(n+1):
        final += 1 / fact_iter(i)
    return final

# print(find_e_iter(50))