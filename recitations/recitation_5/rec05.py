#--- QUESTION 1 ---#
"""
a) True
b) True
c) True
d) False
e) False
f) True
g) True
h) False
i) True
j) True
k) False
l) False
m) True
n) True
o) True
p) True
q) False
r) True
s) True () == () 
t) True
u) False
v) True
w) True
"""
x=(1,2)
y=(1,2)
z = x
a = (tuple([1,2]),(3,4))
b = (x, (3,4))


#--- Question 2 ---#
def contains(obj, tup):
    for part in tup:
        if obj is part:
            return True 
    return False

def deep_contains(obj, tup):
    for part in tup:
        if obj is part:
            return True
        if type(part) == tuple:
            if deep_contains(obj, part):
                return True
    return False

x = (1,2)
a = ( tuple([1,2]), ((3,4),x), (5,6) )
# print(contains(x,a))
# print(deep_contains(x,a))


#--- QUESTION 3 ---#
"""
a(i) 1.5
a(ii) 1 / 6
a(iii) (1, (2, (3, ())))
a(iv) ((((),1),2),3)
b) fn should be a commutative and associative operation
"""
def fold_right(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0], fold_right(fn, initial, seq[1:]))
    
def fold_left(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(fold_left(fn, initial, seq[:-1]), seq[-1])
    
def pair(a, b):
    return (a,b)

def divide(a,b):
    return a/b
# print(fold_left(pair, (),(1,2,3)))
# print(fold_right(divide, 1, (1,2,3)))
# print(fold_left(divide, 1, (1,2,3)))


#--- QUESTION 4 ---#
# a) Using tuples 
# b)
def empty_queue():
    return ()
# Time and Space are both O(1)
# c)
def enqueue(x,q):
    return q + (x,)
# Time and Space are both O(n) where n is the number of elements of q. As tuples are immutable, a new tuple must be created to add the element x.
# d)
def dequeue(q):
    return q[1:]
# Time and Space are both O(n) where n is the number of elements of q. As tuples are immutable, a new tuple must be created to remove the head element.
# e)
def qhead(q):
    return q[0]
# Time and Space are both O(1) as only the first element of the tuple is indexed into
q = enqueue(4, enqueue(5, enqueue(6, empty_queue())))
# print(qhead(q))
# print(qhead(dequeue(q)))


#--- QUESTION 5 ---#
# map 
def map(fn, seq):
    if seq == ():
        return ()
    else:
        return (fn(seq[0]), ) + map(fn, seq[1:])

# filter
def filter(pred, seq):
    if seq == ():
        return ()
    elif pred(seq[0]):
        return (seq[0],) + filter(pred, seq[1:])
    else:
        return filter(pred, seq[1:])

# accumulate 
def accumulate(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0],  accumulate(fn, initial, seq[1:]))

x = (1, 2, 3, 4, 5, 6, 7)

# a)
def square(x):
    return map(lambda y: y*y, x)
# print(square(x))

# b)
def odd_only(x):
    return filter(lambda y: y%2, x)
# print(odd_only(x))

# c)
def duplicates(x):
    return map(lambda y: (y,y), x)
# print(duplicates(x))

# d)
def is_even(x):
    return x%2 == 0

def even_fold(x):
    return fold_left(lambda a,b: b if a==() else (a,b),
                      (), 
                      filter(is_even, x)
                      )
# print(even_fold(x))

# e)
def even_fold_left(x):
    return fold_left(lambda a,b: (b,) if a==() else (a,b), 
                     (), 
                     filter(is_even, x))
# print(even_fold_left(x))

# f) 
def max_x(x):
    return accumulate(lambda a,b: b if b>a else a, x[0], x)
# print(max_x(x))

# g)
def min_x(x):
    return accumulate(lambda a,b: a if a<b else b, x[0], x)
# print(min_x(x))

# h)
def max_x2(x):
    return max_x(square(filter(lambda a: a%2 == False,x)))
# print(max_x2(x))

# i)
def sos(x):
    return accumulate(lambda a,b: a+b, 0, square(x))
# print(sos(x))


""" #--- QUEUE LIST---#
def make_queue():
    return []

def enqueue(q, item):
    q.append(item)
    return q 

def dequeue(q):
    return q.pop(0)
    
def size(q):
    return len(q)

def who_wins(m,players):
    if size(players) <= m:
        return players[1:]
    
    temp = make_queue()
    for _ in range(m):
        enqueue(temp, dequeue(players)) # adds surviving players
    dequeue(players)    # removes the mth player
    # add in remaining players before passed players
    while size(temp) > 0:
        enqueue(players, dequeue(temp))
    return who_wins(m, players)
    
print(who_wins(3, ['val', 'hel', 'jam', 'jin', 'tze', 'eli', 'zha', 'lic']))
print(who_wins(2, ['poo', 'ste', 'sim', 'nic', 'luo', 'ibr', 'sie', 'zhu']))"""