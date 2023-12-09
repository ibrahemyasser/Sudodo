import time


def is_valid(board, row, col, num):
    # Check if the number is not in the current row and column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False
    
    # Check if the number is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def find_empty_location(board):
    # Find the first empty (0) cell in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def forward_check(board, row, col, num):
    # Update the domains of the variables in the same row, column, and subgrid
    for i in range(9):
        # Update row
        if board[row][i] == 0:
            if num in board[row][:i] + board[row][i+1:]:
                return False

        # Update column
        if board[i][col] == 0:
            if num in [board[j][col] for j in range(9) if j != i]:
                return False

        # Update subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        if board[start_row + i // 3][start_col + i % 3] == 0:
            if num in [
                board[start_row + j // 3][start_col + j % 3]
                for j in range(9)
                if j != i
            ]:
                return False

    return True

def backtrack_forward_check(board):
    # Find the first empty cell
    row, col = find_empty_location(board)
    
    # If there are no empty cells, the puzzle is solved
    if row is None and col is None:
        return True

    # Try filling the cell with values 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Assign the value to the cell
            board[row][col] = num
            
            # Forward check to update domains
            forward_check(board, row, col, num)

            # Recursively try to solve the rest of the puzzle
            if backtrack_forward_check(board):
                return True

            # If the current assignment leads to a conflict, backtrack
            board[row][col] = 0

    # If no valid value is found, backtrack to the previous cell
    return False

# Example usage:
sudoku_board = [
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

start_time = time.time()  # Record the start time
if backtrack_forward_check(sudoku_board):
    print("Solution found:")
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists.")
end_time = time.time()  # Record the end time

execution_time = end_time - start_time  # Calculate the total execution time
print(f"Total execution time: {execution_time} seconds")
