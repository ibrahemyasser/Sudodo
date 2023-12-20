# Maintaining Arc Consistency
from utility import get_possible_values_for_grid
import copy

def MAC(grid):
    temp_grid = copy.deepcopy(grid) 
    size = len(grid)
    def rec():
        possible_values = get_possible_values_for_grid(temp_grid)
        for i in range(size):
            for j in range(size):
                if temp_grid[i][j] == 0:
                    if len(possible_values[i][j]) == 0:
                        # No possible values for this square, fail
                        return True
                    elif len(possible_values[i][j]) == 1:
                        # Only one possible value for this square, assign it
                        temp_grid[i][j] = list(possible_values[i][j])[0]
                        return rec()

        return False
    return rec()