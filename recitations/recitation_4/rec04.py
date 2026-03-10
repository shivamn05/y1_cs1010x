# QUESTION 1 #
"""
a) (10, 12, 13, 14)
b) ("CS1010X","CS1231")
c) (10, 12, 13, 14, "CS1010X", "CS1231")
d) 6
e) True
f) False
g) CS1010XCS1010XCS1010XCS1010X
h) C
i) S1010XCS1010XCS1010XCS1010X
j) 0 + 10 + 12 + 13 + 14 = 49 
k) 14
l) 10
m) TypeError
n) TypeError

"""
"""tup_a = (10,12,13,14)
tup_b = ("CS1010X","CS1231")
tup_c = tup_a + tup_b
tup_d = tup_b[0] * 4
print(max(tup_c))"""

# QUESTION 2 #
"""
a) (1,) + (2,) + (3,)
b) (1, (2), 3) ???? so it is actually make it into a string 
c) (1,) + ((2,),) + (3,)
d) ((1, 2),) + ((3, 4),) + ((5, 6),)

"""

# Question 3 #
"""
a) x[3]
b) x[1][2]
c) x[1][0][2][0]

"""

# Question 4 #
# I chose to do in list but they want in tuples 

def make_module(course_code, units):
    return (course_code, units)

def make_units(lecture, tutorial, lab, homework, prep):
    return (lecture, tutorial, lab, homework, prep)

def get_module_code(course):
    return course[0]

def get_module_units(course):
    return course[1]

def get_module_total_units(units):
    return units[0] + units[1] + units[2] + units[3] + units[4]

# a)
def make_empty_schedule():
    return ()

# Time and Space are both O(1)

# b)
def add_class(course, schedule):
    if (course in schedule):
        return schedule         # just to ensure no duplicate courses 
    else:
        return schedule + (course,)

# Time: O(n), where n is the length of schedule. Since tuples are immutable, you need to make a new tuple
# Space: O(n), where n is the number of courses.

# c)
def total_scheduled_units(schedule):
    total = 0
    for mod in schedule:
        total += get_module_total_units(get_module_units(mod))
    return total 

# Time: O(n) where n is the number of modules in the schedule. Because of the loop, as n increases, the time increases proportionally
# Space: O(1) as the only variable is total

# d)
def drop_class(schedule, course):
    if schedule == ():
        return schedule
    elif schedule[0] == course:
        return schedule[1:]     # if course matched the first course in schedule
    else:
        return (schedule[0],) + drop_class(schedule[1:], course) # else, keep course and try again

# Time: O(n^2) where n is the number of courses in schedule.
# Space: O(n^2)

# version 2 is creating a new empty schedule and adding the course, except the course to be dropped in it. This way, the space is O(n) as the tuples are overwritten and the old ones become garbage and space can be reused 

# e)
def credit_limit(schedule, max_credits):
    curr_credits = total_scheduled_units(schedule)
    if curr_credits <= max_credits:
        return schedule
    elif curr_credits > max_credits:
        return credit_limit(drop_class(schedule, schedule[0]), max_credits)

# Time: O(n^3) where n is the number of courses. n times for t_s_u, n^2 for drop_class
# Space: O(n^2)

# f)
def credit_limit_new(schedule, max_credits):
    curr_credits = total_scheduled_units(schedule)
    temp = list(schedule) # n time 
    sorted_list = sorted(temp, key=get_module_total_units) # nlogn time 
    while curr_credits > max_credits:
        curr_credits = curr_credits - get_module_total_units(sorted_list[-1])
        sorted_list = drop_class(sorted_list, sorted_list[-1])
    return tuple(sorted_list)
    

