import copy


def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)
    
    for i in range(grid_size):  # Iterate until the last index
        for j in range(grid_size):  # Iterate until the last index
            if grid[i][j] == 1:  # If the tree is burning (1)
                # Check neighbors down and to the right (diagonal neighbors)
                if (i > 0 and grid[i-1][j]==2) or (i < grid_size - 1 and grid[i+1][j]==2) \ (j > 0 and grid[i][j-1] ==2) or (j < grid_size - 1 and grid[i][j+1]==2):
                    update_grid[i][j] = 2 
                

    return update_grid
