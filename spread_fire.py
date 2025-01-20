import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)  # Create a copy of the grid for updates

    for i in range(grid_size):  # Iterate over rows
        for j in range(grid_size):  # Iterate over columns
            if grid[i][j] == 1:  # If the tree is burning (1)
                # Check if the tree down and to the right are on fire (i.e., grid value = 2)
                if i + 1 < grid_size and grid[i+1][j] == 2:  # Down
                    update_grid[i][j] = 2  # Set the tree on fire
                if j + 1 < grid_size and grid[i][j+1] == 2:  # Right
                    update_grid[i][j] = 2  # Set the tree on fire

    return update_grid
