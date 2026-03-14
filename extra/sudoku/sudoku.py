# 4x4 sudoku
"""
Algorithm:
1. check row. if only one zero, fill it in
2. check column. if only one zero, fill it in
3. check 2x2 square. if only one zero, fill it in
repeat until no zeros 
"""

#--- TEST BOARDS ---#
SIZE = 4
board1 = [[1, 0, 3, 0], [3, 0, 0, 2], [4, 3, 2, 1], [0, 0, 0, 3]]
board2 = [[0, 1, 3, 2], [2, 0, 1, 0], [1, 0, 0, 3], [3, 4, 2, 1]]
board3 = [[0, 0, 0, 0], [0, 1, 2, 4], [0, 3, 4, 1], [0, 4, 0, 2]]
#-------------------#

def fill_row(board):
    global flag
    flag = False
    for row in board:
        count = row.count(0)    # count number of zeros
        if count == 1:
            idx = row.index(0)
            # get missing value
            for value in [1,2,3,4]:
                if value not in row:
                    row[idx] = value 
                    flag = True
                    break
    return flag

def fill_col(board):
    # make the columns the row 
    all_col = []
    for row in range(SIZE):
        col = []
        for num in range(SIZE):
            col.append(board[num][row])
        all_col.append(col)
    # use fill_row to change the numbers in col
    changed = fill_row(all_col)
    # make the rows back into columns
    for i in range(SIZE):
        for j in range(SIZE):
            board[i][j] = all_col[j][i]

    # return fill_row bool
    return changed

def fill_section(board):
    all_sect = []
    size = SIZE
    sect_size = int(size/2)
    for row in range(0,size,sect_size):
        for col in range(0,size,sect_size):
            sect = []
            for r in range(sect_size):
                for c in range(sect_size):
                    sect.append(board[row+r][col+c])
            all_sect.append(sect)

    # use fill_row to change numbers 
    changed = fill_row(all_sect)
    # make the sections back into the board 
    sect_idx = 0
    for block_row in range(0,size,sect_size):
        for block_col in range(0,size,sect_size):
            sect = all_sect[sect_idx]
            idx = 0
            for a in range(sect_size):
                for b in range(sect_size):
                    board[block_row+a][block_col+b] = sect[idx]
                    idx += 1
            sect_idx += 1
    # return fill_row bool 
    return changed

def fill_board(board):
    fillable = True  # indicate if a board is still fillable
    while fillable:
        fill_row(board)
        fill_col(board)
        fill_section(board)
        if fill_section(board) == False and fill_row(board) == False and fill_col(board) == False:
            fillable = False
    return board


#--- TEST CASES ---#

# print(fill_col(board3))
# fill_row(board3)
# fill_col(board3)
# print(board3)
# fill_section(board3)
# print(board3)
print(fill_board(board1))