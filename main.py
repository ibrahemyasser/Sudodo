import time
from AC import constraint_propagation
from forward_checking import forward_check
from sudoku import Sudoku
from prettytable import PrettyTable
import copy
from mrv import mrv


class SudokuCSP:
    size = 0 # size of the grid
    length = 0 # sqrt(size)
    number_of_steps = 0
    def __init__(self, grid, select_unassigned_var = None , inference = None):
        if not self.is_solvable(grid):
            raise ValueError("Invalid Sudoku Puzzle")
        size = len(grid)
        length = self.get_length(grid)
        self.size = size
        self.length = length
        self.grid = grid
        self._select_unassigned_var = select_unassigned_var
        self._inference = inference
    def is_solvable(self, grid):
        # Check if grid size is solvable, i.e. sqrt(size) is an integer
        size = len(grid)
        if size == 0 or int(size ** 0.5) ** 2 != size:
            return False
        return True
    def get_length(self, grid):
        # return sqrt(size)
         return int(len(grid) ** 0.5)
    def increase_number_of_steps(self):
        self.number_of_steps += 1
    def used_in_row(self, row, num):
        return num in self.grid[row]

    def used_in_col(self, col, num):
        return num in [self.grid[i][col] for i in range(self.size)]
    
    def used_in_box(self, start_row, start_col, num, size):
        return any(num in self.grid[i][start_col:start_col + int(size**0.5)] for i in range(start_row, start_row + int(size**0.5)))

    
    def is_assignment_consistent(self, row, col, num):
        return (    
        not self.used_in_row( row, num) and
        not self.used_in_col( col, num) and
        not self.used_in_box( row - row % int(self.size**0.5), col - col % int(self.size**0.5), num, self.size)
        )

    def select_unassigned_var(self):
        if self._select_unassigned_var is not None:
            return self._select_unassigned_var(self.grid)
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None
    def order_domain_values(self):
        return range(1, self.size + 1)
    # var is a tuple (row, col)
    # return true if incosistency is found otherwise false
    def inference(self):
        if self._inference is not None:
            return self._inference(self.grid)
        return False
    def set_grid_value(self, row, col, value):
        self.grid[row][col] = value


    
def backtrack(csp):
    empty_cell = csp.select_unassigned_var()
    if empty_cell is None:
        return True
    [row, col] = empty_cell
    for value in csp.order_domain_values():
        csp.increase_number_of_steps()
        if csp.is_assignment_consistent(row, col, value):
            csp.set_grid_value(row, col, value)
            inferences = csp.inference()
            # if inferences is true we messed up and we need to backtrack
            if inferences:
                csp.set_grid_value(row, col, 0)
                continue
            res = backtrack(csp)
            if res:
                return True
            csp.set_grid_value(row, col, 0) 
    return None

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

def print_grid(grid):
    for row in grid:
        print(row)

def replace_none_with_zero(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] is None:
                grid[i][j] = 0
    return grid

def main():



    puzzles =[Sudoku(i).difficulty(0.9) for i in range(2, 5)]

    table = PrettyTable()
    table.field_names = [ "Algorithm", "Size", "Time", "Number of steps"]
    select_unassigned_var_list = [{"func":None, "name": ""},{ "func":mrv, "name": "MRV"}]
    inference_list = [{"func":None, "name": "basic backtracking"},{ "func":forward_check, "name": "Forward Checking"}, {"func":constraint_propagation, "name": "AC-3"}]
    for i in inference_list:
        for select_unassigned_var_strategy in select_unassigned_var_list:
            for puzzle in puzzles:
                if(i['func'] is None and select_unassigned_var_strategy['func'] is None and len(puzzle.board) > 9): 
                    continue
                csp = SudokuCSP(replace_none_with_zero(copy.deepcopy(puzzle.board)), inference=i['func'], select_unassigned_var=select_unassigned_var_strategy["func"])
                start_time = time.time()
                backtrack(csp)
                print("---------------------------")
                print(i['name'] + " " + select_unassigned_var_strategy['name'])
                print("Solution, Size: ", len(csp.grid))
                is_solution_correct = check_sudoku(csp.grid)
                print("Is solution correct: ", is_solution_correct)
                print_grid(csp.grid)
                print("---------------------------")
                end_time = time.time()
                elapsed_time = end_time - start_time
                table.add_row([ i['name'] + " " + select_unassigned_var_strategy['name'], csp.size, elapsed_time, csp.number_of_steps, is_solution_correct])
    table.sortby = "Size"
    print(table)

    # backtrack(cspWithCP)
    # print_grid("answer", cspWithCP.grid)
    return None
def check_sudoku(grid):
    n = len(grid)
    for row in range(n):
        for col in range(n):
            # check value is an int and within 1 through n
            if not isinstance(grid[row][col], int) or not 1 <= grid[row][col] <= n:
                return False

    # check the rows
    for row in grid:
        if sorted(set(row)) != sorted(row):
            return False

    # check the cols
    for col in range(n):
        cols = [row[col] for row in grid]
        if sorted(set(cols)) != sorted(cols):
            return False

    # if you get past all the false checks return True
    return True
   
if __name__ == "__main__":
    main()
