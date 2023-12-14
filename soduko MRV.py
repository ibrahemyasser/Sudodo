import time

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    
    # Base case: if no empty cells are found, the puzzle is solved
    if not empty_cell:
        return True
    
    row, col = empty_cell
    
    # Get the possible values for the current empty cell
    possible_values = get_possible_values(board, row, col)
    
    # Sort the possible values based on the number of constraints
    possible_values.sort(key=lambda x: len(get_constraints(board, row, col, x)))
    
    # Try each possible value and recurse
    for value in possible_values:
        board[row][col] = value

        # Recursively try to solve the remaining puzzle
        if solve_sudoku(board):
            return True

        # If the current value leads to an invalid solution, backtrack
        board[row][col] = 0
    
    # If no value leads to a solution, backtrack
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def get_possible_values(board, row, col):
    values = set(range(1, 10))
    
    # Check the row and column
    for i in range(9):
        values.discard(board[row][i])
        values.discard(board[i][col])
    
    # Check the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            values.discard(board[i][j])
    
    return list(values)

def get_constraints(board, row, col, value):
    constraints = set()

    # Check the row and column
    for i in range(9):
        if board[row][i] == value:
            constraints.add((row, i))
        if board[i][col] == value:
            constraints.add((i, col))
    
    # Check the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == value:
                constraints.add((i, j))
    
    return constraints

def solve_and_print_sudoku(board):
    start_time = time.time()  # Record the start time

    # Attempt to solve the Sudoku puzzle
    if solve_sudoku(board):
        print("\nSolved Sudoku Puzzle:")
        for row in board:
            print(row)
    else:
        print("\nNo solution exists for the Sudoku puzzle.")

    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the total execution time
    print(f"\nTotal execution time: {execution_time} seconds")

# Example Sudoku puzzle (0 represents an empty cell)
sudoku_board_without_solution = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 8]  # Duplicate 8 in the last row
]

sudoku_board_with_solution = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print the unsolved Sudoku puzzle
print("Unsolved Sudoku Puzzle:")
for row in sudoku_board_without_solution:
    print(row)
# Solve and print the Sudoku puzzle
solve_and_print_sudoku(sudoku_board_with_solution)
