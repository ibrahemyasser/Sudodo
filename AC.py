from utility import get_possible_values_for_grid
def constraint_propagation(grid):
    size = len(grid)
    possible_values = get_possible_values_for_grid(grid)

    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                if len(possible_values[i][j]) == 0:
                    # No possible values for this square, fail
                    return True
                # elif len(possible_values[i][j]) == 1:
                #     # Only one possible value for this square, assign it
                #     grid[i][j] = possible_values[i][j][0]

    return False