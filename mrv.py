from utility import get_possible_values_for_grid
# returns the (row, col) of the cell with the least number of possible values
def mrv(board):
    possible_values_grid = get_possible_values_for_grid(board)
    min_row = 0
    min_col = 0
    min = len(board) + 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0: 
                possible_values = possible_values_grid[i][j]
                if  len(possible_values) < min: 
                    min = len(possible_values)
                    min_row = i
                    min_col = j
    if(board[min_row][min_col] != 0):
        return None
    return (min_row, min_col)

