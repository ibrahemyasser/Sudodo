import math
def get_possible_values_for_grid(board):
    size = len(board)
    box_size = int(math.sqrt(size))
    possible_values_grid = [[set(range(1, size + 1)) for _ in range(size)] for _ in range(size)]

    for row in range(size):
        for col in range(size):
            if board[row][col] != 0:
                possible_values_grid[row][col] = set()
                continue

            # Remove values that are already used in the row and column
            for i in range(size):
                possible_values_grid[row][col].discard(board[row][i])
                possible_values_grid[row][col].discard(board[i][col])

            # Remove values that are already used in the box
            box_row_start = (row // box_size) * box_size
            box_col_start = (col // box_size) * box_size
            for i in range(box_size):
                for j in range(box_size):
                    possible_values_grid[row][col].discard(board[box_row_start + i][box_col_start + j])

    return possible_values_grid