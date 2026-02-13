
""" #--- *args notation ---#
def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,4,5))
"""
""" #--- DICT handling: increase value by one of nested dicts ---#
def increase_by_one(d):
    for key in d:
        if type(d[key]) == dict:
            increase_by_one(d[key])
        else:
            d[key] += 1
    return d
    
print(increase_by_one({'first':27, 'second':16, 'third':8}))
print(increase_by_one({'1':2.7, '11':16, '111':{'a':5, 't':8}}))
print(increase_by_one({2:{ }, 3:{ }, 4:{ }}))
print(increase_by_one({'a':{'b':{'c':10}}}))
"""
""" #--- DATA TYPE: STACK ---#
def make_stack(seq):
    return list(seq)

def make_empty_stack():
    return make_stack(())

def is_empty_stack(stack):
    return stack == make_empty_stack()

def push_stack(stack, item):
    stack.append(item)
    return stack

def pop_stack(stack):
    if is_empty_stack(stack):
        return None
    else:
        location = len(stack) -1
        popped = stack[location]
        stack.pop(location)
        return popped

def peek_stack(stack):
    if is_empty_stack(stack) == True:
        return None
    else:
        loc = len(stack) -1
        return stack[loc]
    
def clear_stack(stack):
    # modifies the stack to be empty and returns the stack
    while stack:
        stack.pop()
    return stack

def operation(oper, int1, int2):
    if oper == '+':
        return int2 + int1
    elif oper == '-':
        return int2 - int1
    elif oper == '*':
        return int2 * int1
    elif oper == '/':
        return int2 / int1

def calculate(inputs):
    # check if input is a single integer, return int if True
    if len(inputs) == 1 and type(inputs[0]) == int:
        return inputs[0]
    else:
        numbers = make_empty_stack()
        for elem in inputs:
            if type(elem) == int:
                push_stack(numbers, elem)
            else:
                int1 = pop_stack(numbers)
                int2 = pop_stack(numbers)
                new = operation(elem, int1, int2)
                push_stack(numbers, new)
        return int(pop_stack(numbers))
"""
""" #--- DOUBLE SORTING: SCORE AND NAME ---#
def top_k(students, k):
    # sort by score
    students.sort(key= lambda student: student[2], reverse=True)

    # extract top k 
    top = students[:k]

    # check if (k+1)th student score is same as kth student score
    for i in range(k, len(students)):
        if students[i][2] == top[k-1][2]:
            top.append(students[i])
    
    # sort the top students by number, by alphabet 
    for j in range(len(top)-1):
        if top[j][2] == top[j+1][2] and top[j][0] > top[j+1][0]:
            top[j], top[j+1] = top[j+1], top[j]
    return top


### DO NOT MODIFY THIS ###
students = [('tiffany', 'A', 15), 
            ('jane', 'B', 10),
            ('ben', 'C', 8), 
            ('eugene', 'A', 21),
            ('simon', 'A', 21), 
            ('john', 'A', 15), 
            ('jimmy', 'F', 1), 
            ('charles', 'C', 9), 
            ('freddy', 'D', 4), 
            ('dave', 'B', 12),
            ('tester','B', 12)]

print(top_k(students, 5))
"""
""" #--- Counting mode ---#
def mode_score(students):
    # Extracting just the grade scores from students
    grades = []
    for i in range(len(students)):
        grades.append(students[i][2])

    # Counting the number of times a number appears
    grade_count = {}
    for j in grades:
        if j not in grade_count:
            grade_count.update({j:1})
        else:
            grade_count[j] = grade_count[j] + 1
    # Sorting by value into a list modal
    modal = []
    for k, v in sorted(grade_count.items(), key=lambda item: item[1]):
        modal.append([k,v])
    modal.sort(key=lambda modal: modal[1], reverse=True)
    
    # Returning the modal value(s)
    final = [modal[0][0]]
    for x in range(1, len(modal)-1):
        if modal[x][1] == modal[0][1]:
            final.append(modal[x][0])
    return final


### DO NOT MODIFY THIS ###
students = [('tiffany', 'A', 15), 
            ('jane', 'B', 10),
            ('ben', 'C', 8), 
            ('simon', 'A', 21), 
            ('eugene', 'A', 21), 
            ('john', 'A', 15), 
            ('jimmy', 'F', 1), 
            ('charles', 'C', 9), 
            ('freddy', 'D', 4), 
            ('dave', 'B', 12),
            ('q','B',15)]

print(mode_score(students))
"""
""" #--- TRANSPOSE A MATRIX ---#
def transpose(matrix):
    non_row = len(matrix)
    for col in range(len(matrix[0])):
        temp_row = []
        for row in range(non_row):
            temp_row.append(matrix[row][col])
        matrix.append(temp_row)
    for _ in range(non_row):
        matrix.pop(0)
    return matrix

### DO NOT MODIFY THIS ###
matrix1 = [[ 1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[ 1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix3 = [[1, 2, 3]]
print(transpose(matrix2))
"""
""" #--- COL SUM OF MATRIX ---#
def col_sum(matrix):
    sum_list = matrix[0]
    for row in range(1, len(matrix)):
        for col in matrix[row]:
            hold = col + sum_list[0]
            sum_list.pop(0)
            sum_list.append(hold)
    return sum_list

# print(col_sum([[1,2],[3,4],[5,6]]))
"""
""" #--- ROW SUM OF MATRIX ---#
def row_sum(matrix):
    sum_list = []
    summation = 0
    for row in matrix:
        for i in row:
            summation += i
        sum_list.append(summation)
        summation = 0
    return sum_list

# print(row_sum([[ 1, 2, 3], [4, 5, 6], [7, 8, 9]]))
"""
""" #--- SORTING: MERGE SORT ---#
def merge_lists(list1, list2):
    merged_list = []
    while list1 and list2:
        if list1[0] > list2[0]:
            merged_list.append(list1[0])
            list1.remove(list1[0])
        else:
            merged_list.append(list2[0])
            list2.remove(list2[0])
    merged_list.extend(list1)
    merged_list.extend(list2)
    return merged_list

print(merge_lists([6, 4, 2, 1], [5, 3]))
"""
""" #--- SORTING: SELECTION SORT
def sort_age(lst):
    sorted = []
    unsorted = lst.copy()
    while unsorted:
        biggest = unsorted[0]
        for element in unsorted[1:]:
            if element[1] > biggest[1]:
                biggest = element
        unsorted.remove(biggest)
        sorted.append(biggest)
    return sorted

print(sort_age([("F", 18), ("M", 23), ("F", 19), ("M", 30)]))

def sort_by_gender_then_age(lst):
    males = []
    females = []
    for elem in lst:
        if elem[0] == 'M':
            males.append(elem)
        else:
            females.append(elem)
    males = sort_age(males)
    females = sort_age(females)
    return males + females 
"""
""" #--- LIST FLATTENING ---#
def flatten_list(lst):
    flat_list = []
    for i in range(len(lst)):
        if type(lst[i]) != list:
            flat_list.append(lst[i])
        else:
            flat_list += flatten_list(lst[i])
    return flat_list


def count_occurrences(lst, num):
    flat_lst = flatten_list(lst)
    count = 0
    for i in range(len(flat_lst)):
        if flat_lst[i] == num:
            count += 1
    return count
    
# print(count_occurrences([[], [[]], [[[]]], [[[[]]]]], 2))
"""
""" #--- REMOVING FROM LIST WITHOUT MAKING A NEW LIST ---#
def remove_extras(lst):
    # your code here
    lst.sort()
    remove = []
    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:
            remove.append(lst[i])
    for j in range(len(remove)):
        if remove[j] in lst:
            lst.remove(remove[j])
    return lst

lst2 = [2, 2, 2, 1, 5, 4, 4]
lst1 = [1, 5, 1, 1, 3]
# print(remove_extras(lst1))
"""
""" #--- TOWERS OF HANOI TUPLE ---#
def hanoi(n, src, dsc, aux):
    moves = ()
    if n == 0:
        return moves
    else:
        moves += hanoi(n-1, src, aux, dsc)
        moves += ((src,dsc),)
        moves += hanoi(n-1, aux, dsc, src)
    return moves
# print(hanoi(3, 1, 2, 3))
"""
""" #--- TUPLE RECURSION ---#
def count_leaves(tree):
    if tree == ():
        return 0
    elif is_leaf(tree):
        return 1
    else:
        return count_leaves(tree[0]) + count_leaves(tree[1:])

def is_leaf(n):
    if type(n) != tuple:
        return True

x = ((1, 2), ((3, 4), (5, (6, 7), (8, 9))), (10, (11, 12)), (13, (14,), (16,), 17, 18, (19, 20)))
print(count_leaves(x))
"""
""" #--- TUPLE MANIPULATION II---#
def copy_tree(tree):
    new_tree = ()
    # base case 1: if all elem are int return copy of tree
    for i in range(len(tree)):
        if type(tree[i]) != tuple:
            new_tree += (tree[i],)
        else:
            new_tree += (copy_tree(tree[i]),)
    return new_tree

# Do not remove this line
original = (1,(2,3),4)
print(copy_tree(original))
"""
""" #--- TUPLE MANIPULATION ---#
def accumulate(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0],  accumulate(fn, initial, seq[1:]))

# print(accumulate(lambda x,y:(x, y), (), (1, 2, 3)) )

def map(fn, seq):
    if seq == ():
        return ()
    else:
        return (fn(seq[0]), ) + map(fn, seq[1:])
    
def filter(pred, seq):
    if seq == ():
        return ()
    elif pred(seq[0]):
        return (seq[0],) + filter(pred, seq[1:])
    else:
        return filter(pred, seq[1:])
    
minus = lambda x,y: x - y 
is_odd = lambda x: x%2 == 1 
square = lambda x: x**2 
# print(accumulate(minus, 0,  map(square, filter(is_odd, tuple(range(6))))))

def to_str(tup):
    # your code here
    return accumulate(lambda x, y: str(x) + str(y), '', tup)

# print(to_str(('c', 's', 1, 0, 1, 0, 's')))
"""
""" #--- LIST MANIPULATION ---#
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
"""
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