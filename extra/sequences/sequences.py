# Easy sudoku : column has 1-9, row has 1-9, box does not matter 
SIZE = 9

# incomplete slots are 0
board = (
(5, 3, 4, 6, 7, 8, 9, 1, 2),
(6, 0, 2, 1, 9, 0, 3, 4, 0),
(1, 9, 8, 3, 4, 2, 0, 6, 7),
(8, 5, 9, 7, 6, 1, 4, 2, 3),
(4, 2, 0, 8, 5, 3, 7, 9, 1),
(7, 1, 3, 9, 2, 4, 8, 5, 6),
(9, 6, 1, 0, 3, 7, 2, 8, 4),
(2, 8, 7, 4, 1, 9, 6, 0, 5),
(3, 4, 5, 2, 8, 6, 1, 7, 9)
)

def easy_sudoku(x, y, n): # (x,y) is the coordinate on the grid, n is the trial
    global board
    row_num, col_num = x-1, y-1
    row_digits = board[row_num]
    col_digits = ()
    for row in board:
        col_digits += (row[col_num],)
    # either return "No violation" or return "Violation"
    if (n in col_digits) or (n in row_digits):
        return "Violation"
    else:
        return "No violation"

#--- TEST CASES ---#
test1 = easy_sudoku(2,2,2)
# print(test1)
test2 = easy_sudoku(2,2,7)
# print(test2)

# Car : Reading and printing out statistical data about input car
# max odometer reading = 999.9
# distances is a tuple containing all distances 
# odometer is the odometer reading at the start of day 
def car(odometer, distances):
    # EOD odometer reading
    final_odometer_value = odometer
    for ride in distances:
        final_odometer_value = round(final_odometer_value,1) + ride
    while final_odometer_value > 999.9:
        # % 1000 because it goes from 0 to 999.9 which is actually 1000 numbers
        final_odometer_value = (round(final_odometer_value,1) % 1000)
    final_odometer_value = round(final_odometer_value,1)

    # total number of trips 
    total_number_of_trips = len(distances)

    # avg dist per trip 
    if total_number_of_trips > 0:
        avg_dist_per_trip = round((sum(distances) / total_number_of_trips),1)
    else:
        avg_dist_per_trip = 0.0
    
    # max difference between 2 consecutive trips 
    if total_number_of_trips <= 1:
        max_diff_between_two_consecutive_trips = 0.0
    else:
        max_gap = abs(distances[0]-distances[1])
        for trip in range(1,total_number_of_trips-1):
            curr_gap = abs(distances[trip] - distances[trip+1])
            if  curr_gap > max_gap:
                max_gap = curr_gap
        max_diff_between_two_consecutive_trips = round(max_gap,1)
    
    return (final_odometer_value, total_number_of_trips, avg_dist_per_trip, max_diff_between_two_consecutive_trips)

#--- TEST CASES ---#
car1 = car(980.5, (23.8, 19, 8.2))
car2 = car(100, (1084.9, 900))
car3 = car(820.3, (1563.2, ))
car4 = car(70, ())
# print(car1)

# Matrix - checking if the numbers in the row are ordered 
def check_matrix(matrix):
    current = matrix[0][0]
    for row in matrix:
        for i in row:
            if i >= current:
                current = i
            else:
                return False
    return True 

print(check_matrix(((-1, 2, 4, 6, 5), (8, 9, 10, 12, 13))))