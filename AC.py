def generate_domains(grid):
    """Generate the domains for each cell in the grid."""
    domains = {}
    size = len(grid)

    for i in range(size):
        for j in range(size):
            if grid[i][j] != 0:
                # If the cell is filled in, its domain is a singleton
                domains[(i, j)] = [grid[i][j]]
            else:
                # If the cell is empty, its domain is all numbers from 1 to 9
                domains[(i, j)] = list(range(1, size + 1))

    return domains

def enforce_arc_consistency(grid):
    """Enforce arc consistency on the domains."""
    domains = generate_domains(grid)
    queue = [(Xi, Xj) for Xi in domains for Xj in domains if Xi != Xj]
    while queue:
        Xi, Xj = queue.pop(0)
        # If the domain of Xi is a single value, remove it from the domain of Xj
        if len(domains[Xi]) == 1 and domains[Xi][0] in domains[Xj]:
            domains[Xj].remove(domains[Xi][0])
            # If the domain of Xj is now empty, the CSP is not arc consistent
            if not domains[Xj]:
                return False
            # If the domain of Xj has been reduced, add all arcs (Xk, Xj) to the queue
            for Xk in domains:
                if Xk != Xi and Xk != Xj:
                    queue.append((Xk, Xj))
    return True