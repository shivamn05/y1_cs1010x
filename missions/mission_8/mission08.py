#
# CS1010S --- Programming Methodology
#
# Mission 8 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def read_data(filename):
    rows = read_csv(filename)
    rep_title = tuple(int(x) for x in rows[0][1:])
    age_title = []
    data = []
    for row in rows[1:]:
        age_title.append(int(row[0]))
        data.append(tuple(int(x) for x in row[1:]))
    return create_table(data, age_title, rep_title)

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

# print("## Q1 ##")
# Sit-up score of a 24-year-old who did 10 sit-ups.
# print(access_cell(situp_table, 24, 10))    # 0

# Push-up score of a 18-year-old who did 30 push-ups.
# print(access_cell(pushup_table, 18, 30))   # 16

# Run score of a 30-year old-who ran 12 minutes (720 seconds)
# print(access_cell(run_table, 30, 720))     # 36

# Since our run.csv file does not have data for 725 seconds, we should
# get None if we try to access that cell.
# print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

def pushup_score(pushup_table, age, pushup):
    data = get_data(pushup_table)
    pushup = int(pushup)
    if pushup > 60:
        pushup = 60
    elif pushup == 0:
        return 0
    return access_cell(pushup_table, age, pushup)


def situp_score(situp_table, age, situp):
    data = get_data(situp_table)
    situp = int(situp)
    if situp > 60:
        situp = 60
    elif situp == 0:
        return 0
    return access_cell(situp_table, age, situp)

def run_score(run_table, age, run):
    data = get_data(run_table)
    run = int(run)
    if run < 510:
        run = 510
    elif run > 1100:
        return 0
    elif run % 10 != 0:
        # Ceiling the run time to the nearest 10's
        run = run + (10 - run % 10)
    return access_cell(run_table, age, run)


# print("## Q2 ##")
# print(pushup_score(pushup_table, 18, 61))   # 25
# print(pushup_score(pushup_table, 18, 70))   # 25
# print(situp_score(situp_table, 24, 0))      # 0

# print(run_score(run_table, 30, 720))        # 36
# print(run_score(run_table, 30, 725))        # 35
# print(run_score(run_table, 30, 735))        # 35
# print(run_score(run_table, 30, 500))        # 50
# print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
    if score < 51:
        return 'F'
    elif 51 <= score < 61:
        return 'P'
    elif 61 <= score < 75:
        return 'P$'
    elif 75 <= score < 85:
        return 'S'
    else:
        return 'G'

# print("## Q3 ##")
# print(ippt_award(50))     # F
# print(ippt_award(51))     # P
# print(ippt_award(61))     # P$
# print(ippt_award(75))     # S
# print(ippt_award(85))     # G


##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    # indiv tables
    pushup_table = get_pushup_table(ippt_table)
    situp_table = get_situp_table(ippt_table)
    run_table = get_run_table(ippt_table)

    # indiv pts 
    pu_pts = pushup_score(pushup_table, age, pushup)
    su_pts = situp_score(situp_table, age, situp)
    run_pts = run_score(run_table, age, run)

    points = pu_pts + su_pts + run_pts
    award = ippt_award(points)
    return (points, award)

# print("## Q4 ##")
# print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
# print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
# print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
# print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
# print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########
def make_training_program(rate_pushup, rate_situp, rate_run):
    def training_program(ippt_table, age, pushup, situp, run, days):
        # changes
        push_up_diff = days // rate_pushup
        sit_up_diff = days // rate_situp
        run_diff  = days // rate_run

        # new results
        pushup = pushup + push_up_diff
        situp = situp + sit_up_diff
        run = run - run_diff
        results = ippt_results(ippt_table, age, pushup, situp, run)
        return (pushup, situp, run, results)
    return training_program

# print("## Q5 ##")
# tp = make_training_program(7, 3, 10)
# print(tp(ippt_table, 25, 30, 25, 820, 30))        # (34, 35, 817, (61, 'P$'))


##########
# Bonus  #
##########

""" #--- TRAINS INDIV ONLY ---#
def make_tp_bonus(rate_pushup, rate_situp, rate_run):
    def tp_bonus(ippt_table, age, pushup, situp, run, days):
        # no improvement constant - such that the indiv score doesnt change
        nic = days + 1
        nic_score = make_training_program(rate_pushup, rate_situp, rate_run)(ippt_table, age, pushup, situp, run, days)
        # improve push up only
        pu_score = make_training_program(rate_pushup, nic, nic)(ippt_table, age, pushup, situp, run, days)

        # improve sit up only 
        su_score = make_training_program(nic, rate_situp, nic)(ippt_table, age, pushup, situp, run, days)

        # improve run only 
        run_only_score = make_training_program(nic,nic,rate_run)(ippt_table, age, pushup, situp, run, days)

        # compare improved results and return best result 
        if nic_score[3][0] >= pu_score[3][0] and nic_score[3][0] >= su_score[3][0] and nic_score[3][0] > run_only_score[3][0]:
            return nic_score
        if pu_score[3][0] > su_score[3][0]  and pu_score[3][0] > run_only_score[3][0]:
            return pu_score
        elif su_score[3][0] > pu_score[3][0] and su_score[3][0] > run_only_score[3][0]:
            return su_score
        else:
            return run_only_score
    return tp_bonus
"""
#--- LOOKS AT ALL 3 AND TRAINS ---#
def make_tp_bonus(rate_pushup, rate_situp, rate_run):
    def tp_bonus(ippt_table, age, pushup, situp, run, days):
        curr_best = (pushup, situp, run, ippt_results(ippt_table, age, pushup, situp, run))
        
        # Train push ups 
        if days >= rate_pushup:
            score = tp_bonus(ippt_table, age, pushup+1, situp, run, days-rate_pushup)
            if score[3][0] > curr_best[3][0]:
                curr_best = score 

        # Train sit ups 
        if days >= rate_situp:
            score = tp_bonus(ippt_table, age, pushup, situp+1, run, days-rate_situp)
            if score[3][0] > curr_best[3][0]:
                curr_best = score 

        # Train run
        if days >= rate_run:
            score = tp_bonus(ippt_table, age, pushup, situp, run-1, days-rate_run)
            if score[3][0] > curr_best[3][0]:
                curr_best = score 
        
        return curr_best
    
    return tp_bonus

tp_bonus = make_tp_bonus(7, 3, 10)

# Note: Depending on your implementation, you might get a different number of
# sit-up, push-up, and 2.4km run timing. However, the IPPT score and grade
# should be the same as the sample output.

# print(tp_bonus(ippt_table, 25, 20, 30, 800, 30))      # (20, 40, 800, (58, 'P'))
# print(tp_bonus(ippt_table, 25, 20, 30, 800, 2))       # (20, 30, 800, (52, 'P'))
