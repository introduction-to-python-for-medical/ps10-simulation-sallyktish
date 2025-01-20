import copy


def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)
    
    for i in range(grid_size):  # Iterate until the last index
        for j in range(grid_size):  # Iterate until the last index
            if grid[i][j] == 1:  # If the tree is burning (1)
                # Check neighbors down and to the right (diagonal neighbors)
                if i + 1 < grid_size and grid[i+1][j] == 1:  # Check down
                    update_grid[i+1][j] = 2  # Set the neighbor on fire
                
                if j + 1 < grid_size and grid[i][j+1] == 1:  # Check right
                    update_grid[i][j+1] = 2  # Set the neighbor on fire

    return update_grid
