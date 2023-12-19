


class SudokuCSP:
    size = 0 # size of the grid
    length = 0 # sqrt(size)
    def __init__(self, grid, select_unassigned_var = None , order_domain_values = None, inference = None):
        if not self.is_solvable(grid):
            raise ValueError("Invalid Sudoku Puzzle")
        size = len(grid)
        length = self.get_length(grid)
        self.size = size
        self.length = length
        self.grid = grid
        self._select_unassigned_var = select_unassigned_var
        self._order_domain_values = order_domain_values
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
            return self._select_unassigned_var(self)
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None
    def order_domain_values(self):
        if self._order_domain_values is not None:
            return self._order_domain_values(self)
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

def main():
    #cspWithMRV = SudokuCSP(sudoku_board9_9, select_unassigned_var = select_unassigned_var_MRV)
    #csmWithMRV_CP = SudokuCSP(sudoku_board9_9, select_unassigned_var = select_unassigned_var_MRV, inference = enforce_arc_consistency)
    #cspWithMRV_forward_check = SudokuCSP(sudoku_board9_9, select_unassigned_var = select_unassigned_var_MRV, inference = forward_check)
    #cspWithForwardCheck = SudokuCSP(sudoku_board9_9, inference = forward_check)
    #cspWithCP = SudokuCSP(sudoku_board9_9, inference = enforce_arc_consistency)
    csp = SudokuCSP(sudoku_board9_9)
    backtrack(csp)
    print(csp.grid)
    # todo compare performance of different algorithms
    return None

main()