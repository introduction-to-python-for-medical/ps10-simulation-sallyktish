import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)  # Create a copy of the grid for updates
    
    # Loop through all the elements of the grid
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:  # If the tree is burning (value 1)
                # Check downwards and to the right neighbors
                if i + 1 < grid_size and grid[i+1][j] == 1:  # Check downward neighbor
                    update_grid[i+1][j] = 2  # Set the neighbor tree on fire
                if j + 1 < grid_size and grid[i][j+1] == 1:  # Check rightward neighbor
                    update_grid[i][j+1] = 2  # Set the neighbor tree on fire

    return update_grid
