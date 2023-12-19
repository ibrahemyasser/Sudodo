import math

def forward_check(board):
    # check if the board is still solvable
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:  # if the cell is empty
                possible_values = get_possible_values(board, i, j)
                if not possible_values:  # if there are no possible values for the cell
                    return True
    return False

def get_possible_values(board, row, col):
    # returns a list of all possible values that can be placed in the cell at (row, col)
    possible_values = set(range(1, len(board) + 1))  # initially, any value from 1 to board size can be placed in the cell
    for i in range(len(board)):
        possible_values.discard(board[i][col])  # remove values that are already used in the column
        possible_values.discard(board[row][i])  # remove values that are already used in the row

    # calculate the size of the sub-grid
    box_size = int(math.sqrt(len(board)))
    box_row_start = (row // box_size) * box_size
    box_col_start = (col // box_size) * box_size
    for i in range(box_size):
        for j in range(box_size):
            possible_values.discard(board[box_row_start + i][box_col_start + j])  # remove values that are already used in the box

    return possible_values