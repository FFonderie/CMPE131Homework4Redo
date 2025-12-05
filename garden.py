def max_flowers(grid):
    def check(row, col):
        # returns true if this space can be occupied
        # check self and edges, if they exist
        # if ANY edge is 1, stop and return false
        if grid[row][col] == 1:
            return False
        if col > 0:
            if grid[row][col-1] == 1:
                return False
        if col < (len(grid[0]) - 1):
            if grid[row][col+1] == 1:
                return False
        if row > 0:
            if grid[row-1][col] == 1:
                return False
        if row < (len(grid) - 1):
            if grid[row+1][col] == 1:
                return False
        return True
    
    # I am tired so this is very unoptimized
    # go through all spots in the grid
    row = 0
    spots = 0
    for i in grid:
        col = 0
        for j in i:
            if check(row, col):
                spots +=1
                grid[row][col] = 1
            col += 1
        row += 1
    return spots