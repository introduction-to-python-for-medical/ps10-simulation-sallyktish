import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)
    
    for i in range(grid_size):  # Iterate until the last index
        for j in range(grid_size):  # Iterate until the last index
            if grid[i][j] == 1:  # If the tree is burning (1)
                # Check for fire in neighbors down and to the right
                if i < grid_size - 1 and grid[i+1][j] == 2:  # Check down
                    update_grid[i][j] = 2  # Set the current tree on fire
                if j < grid_size - 1 and grid[i][j+1] == 2:  # Check right
                    update_grid[i][j] = 2  # Set the current tree on fire

    return update_grid
