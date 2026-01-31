def common(lst1, lst2):
    result = []
    if len(lst1) > len(lst2):
        lst1, lst2 = lst2, lst1
    for i in range(len(lst2)):
        if lst2[i] in lst1:
            result.append(lst2[i])
    return result



# Do not modify the following lines        
print(common(['1010s', 'is', 'cool'], ['it', 'is', 'also', 'torturing']))
print(common(['love', 'makes', 'world', 'better'], ['hello', 'world']))
print(common([], ['happy', 'holiday']))
print(common(['happy', 'holiday'], []))
print(common(['cheese', 'steak', 'sandwich'], ['chicken', 'tikka', 'pizza']))
      



#---- TEST CASES ----#


"""#--- TUPLES ---#
def change_value_at_index(tpl, index, value):
    # Your code here
    if index >= len(tpl) or index < -len(tpl):
        return tpl
    my_list = []
    for i in range(len(tpl)):
        my_list.append(tpl[i])
    my_list[index] = value
    return tuple(my_list)

print(change_value_at_index((1, 2, 3), 1, -1))
print(change_value_at_index((1, 2, 3), -3, 'huh'))
print(change_value_at_index((1, 2, 3), 10, -1))
print(change_value_at_index((1, 2, 3), -10, -1))
"""
""" #--- p-ary to q-ary ---#
def compose(f, g):
    return lambda x: f(g(x))

def make_p_ary_to_q_ary_converter(p, q):
    return compose(make_decimal_to_n_ary_converter(q), make_n_ary_to_decimal_converter(p))
"""
""" #--- n-ary to DECIMAL ---#
def make_n_ary_to_decimal_converter(n):
    def decimal(number):
        if number == 0:
            return '0'
        dec_num = 0
        bases = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        count = len(number) -1
        for digit in str(number):
            dec_num += bases[digit] * (n ** count)
            count -= 1
        return dec_num
    return decimal
"""
""" #--- Hexadecimal to Decimal ---#
def hexadecimal_to_decimal(hex_number):
    # base-16 to base-10
    bases = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    dec_num = 0
    count = len(hex_number) -1
    for digit in str(hex_number):
        dec_num += bases[digit] * (16 ** count)
        count -= 1
    return dec_num

"""
""" #--- DECIMAL TO n-ary CONVERTER for 1<n<17 ---#
def make_decimal_to_n_ary_converter(n):
    # return a number converter that takes a decimal number and returns its string representation in base n
    def decimal(number):
        if number == 0:
            return '0'
        n_ary_num = ''
    
        bases = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        bases = bases[:n]
        while number > 0:
            n_ary_num = bases[number%n] + n_ary_num
            number = number // n
        return n_ary_num
    return decimal

"""
""" #--- DEC to Binary number ---#

def decimal_to_binary(number):
    if number == 0:
        return '0'
    
    bin_num = ''
    while number > 0:
        bin_num = str(number % 2) + bin_num
        number = number // 2
    
    return bin_num

"""
""" #--- for tutorial 4: q5 ---#

def accumulate(combiner, base, term, a, next, b):
    if a > b:
        return base
    return combiner(term(a), accumulate(combiner, base, term, next(a), next, b))

def sum(term, a, next, b):
    return accumulate(lambda x, y: x+y, 0, term, a, next, b)

def accumulate_iter(combiner, null_value, term, a, next, b):
    count = null_value
    list_of_values = []
    while a <= b:
        list_of_values = [term(a)] + list_of_values
        a = next(a)
    for i in list_of_values:
        count = combiner(i, count)
    return count

def accumulate_iter1(combiner, null_value, term, a, next, b):
    count = null_value
    while a <= b:
        count = combiner(term(a), count)
        a = next(a)
    return count

def accumulate_iter2(combiner, null_value, term, a, next, b):
    count = null_value
    while a <= b:
        count = combiner(count, term(a))
        a = next(a)
    return count

print(accumulate_iter(lambda x,y: x*y, 1, lambda x: x*x, 1, lambda x: x+1, 5))
print(accumulate_iter(lambda x,y: x+y, 1, lambda x: x*x, 1, lambda x: x+1, 5))
print(accumulate_iter(lambda x,y: x+y, 0, lambda x: x*x, 1, lambda x: x+1, 5))

print(accumulate_iter(lambda x,y: x-y, 0, lambda x: x*x, 1, lambda x: x+1, 6))
print(accumulate_iter1(lambda x,y: x-y, 0, lambda x: x*x, 1, lambda x: x+1, 6))
print(accumulate_iter2(lambda x,y: x-y, 0, lambda x: x*x, 1, lambda x: x+1, 5))

#print(sum(lambda x: x*2, 1, lambda x: x+1, 5))
#print(sum(lambda x: x*2, 0, lambda x: x+2, 10))
#print(sum(lambda x: x**2, 1, lambda x: x+1, 5))

#print(accumulate(lambda x, y: x*y, 1, lambda x: x**2 + 1, 0, lambda x: x+2, 5)==85)
#print(accumulate(lambda x, y: x+y, 1, lambda x: x**2 + 1, 0, lambda x: x+2, 5)==24)
#print(accumulate(lambda x, y: x+y, 1, lambda x: x**2 + 1, 1, lambda x: x+2, 5)==39)

"""
""" #--- NEW FIB USING COMBINE ---#
def combine (f , op ,n ):
    result = f ( 0 )
    for i in range ( n ):
        result = op ( result , f ( i ))
    return result


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

def newer_fib(n):

    fib = []

    def f(x):
        if x == 0:
            return 0
        elif x in [1]:
            return 1
        else:
            return fib[0]+fib[1]
    
    def op(x,y):
        fib.append(y)
        if len(fib)>2:
            fib.pop(0)
        return y
    
    return combine(f,op,n+1)
"""
#---- TEST CASES ----#
