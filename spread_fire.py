import copy

def spread_fire(grid):
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)  # יצירת עותק של הגריד

    for i in range(grid_size):  # מעבר על כל שורות הגריד
        for j in range(grid_size):  # מעבר על כל עמודות הגריד
            if grid[i][j] == 1:  # אם התא הוא עץ
                neighbors = []

                # בדיקת שכנים רק אם הם בגבולות
                if i > 0: 
                    neighbors.append(grid[i-1][j])  # שכן מעל
                if i < grid_size - 1: 
                    neighbors.append(grid[i+1][j])  # שכן מתחת
                if j > 0: 
                    neighbors.append(grid[i][j-1])  # שכן משמאל
                if j < grid_size - 1: 
                    neighbors.append(grid[i][j+1])  # שכן מימין

                # אם אחד מהשכנים בוער, העץ הופך לבוער
                if 2 in neighbors:
                    update_grid[i][j] = 2  # עדכון בגריד החדש בלבד

    return update_grid  # ה
