import time

def is_safe(grid, row, col, num, size):
    return (
        not used_in_row(grid, row, num) and
        not used_in_col(grid, col, num, size) and
        not used_in_box(grid, row - row % int(size**0.5), col - col % int(size**0.5), num, size)
    )

def used_in_row(grid, row, num):
    return num in grid[row]

def used_in_col(grid, col, num, size):
    return num in [grid[i][col] for i in range(size)]

def used_in_box(grid, start_row, start_col, num, size):
    return any(num in grid[i][start_col:start_col + int(size**0.5)] for i in range(start_row, start_row + int(size**0.5)))

def enforce_arc_consistency(grid, size):
    temp_grid = grid
    for i in range(size):
        for j in range(size):
            if temp_grid[i][j] == 0:
                for value in range(1, size + 1):
                    if is_safe(temp_grid, i, j, value, size):
                        temp_grid[i][j] = value
                        if enforce_arc_consistency(temp_grid, size):
                            return True
                        temp_grid[i][j] = 0
                return False
    return True


sudoku_board9_9 = [
    [0, 0, 0, 0, 0, 0, 6, 8, 0],
    [0, 0, 0, 0, 7, 3, 0, 0, 9],
    [3, 0, 9, 0, 0, 0, 0, 4, 5],
    [4, 9, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 3, 0, 5, 0, 9, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 3, 6],
    [9, 6, 0, 0, 0, 0, 3, 0, 8],
    [7, 0, 0, 6, 8, 0, 0, 0, 0],
    [0, 2, 8, 0, 0, 0, 0, 0, 0]
]
###Solution###
# [1, 7, 2, 5, 4, 9, 6, 8, 3]
# [6, 4, 5, 8, 7, 3, 2, 1, 9]
# [3, 8, 9, 2, 6, 1, 7, 4, 5]
# [4, 9, 6, 3, 2, 7, 8, 5, 1]
# [8, 1, 3, 4, 5, 6, 9, 7, 2]
# [2, 5, 7, 1, 9, 8, 4, 3, 6]
# [9, 6, 4, 7, 1, 5, 3, 2, 8]
# [7, 3, 1, 6, 8, 2, 5, 9, 4]
# [5, 2, 8, 9, 3, 4, 1, 6, 7]


sudoku_board_4_4 = [
    [0, 4, 2, 0],
    [2, 0, 0, 3],
    [1, 0, 0, 4],
    [0, 3, 1, 0]
]
###Solution###
# [3, 4, 2, 1]
# [2, 1, 4, 3]
# [1, 2, 3, 4]
# [4, 3, 1, 2]


# sudoku_board = sudoku_board9_9
# sudoku_size = len(sudoku_board)

# start_time = time.time()  # Record the start time
# if enforce_arc_consistency(sudoku_board,sudoku_size):
#     print("Solution found:")
#     for row in sudoku_board:
#         print(row)
# else:
#     print("No solution exists.")
# end_time = time.time()  # Record the end time

# execution_time = end_time - start_time  # Calculate the total execution time
# print(f"Total execution time: {execution_time} seconds")
