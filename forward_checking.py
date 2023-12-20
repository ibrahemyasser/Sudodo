from utility import get_possible_values_for_grid

def forward_check(board):
    # check if the board is still solvable
    possible_values_grid = get_possible_values_for_grid(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:  # if the cell is empty
                possible_values = possible_values_grid[i][j]
                if len(possible_values) == 0:  # if there are no possible values for the cell
                    return True
    return False
