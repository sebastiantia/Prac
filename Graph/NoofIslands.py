
def dfs(visited, grid, r, c):
    #out of bounds look up
    rowInbounds = 0 <= r and r < len(grid)
    colomnInbounds = 0 <= c and c < len(grid[0])
    if not rowInbounds or not colomnInbounds: return False
    
    #Don't have to recurse for water
    if grid[r][c] == "W":
        return False
    
    #prevent infinite cycles
    pos = str(r) + ',' + str(c)
    if pos in visited: return False
    visited.add(pos)

    dfs(visited, grid, r-1, c)
    dfs(visited, grid, r+1, c) 
    dfs(visited, grid, r, c+1)
    dfs(visited, grid, r, c-1)
    #Just finished exploring brand new island
    return True


if __name__ == "__main__":
    grid = [
        ["w","L","W","W","W"],
        ["w","L","W","W","W"],
        ["w","W","W","L","W"],
        ["w","W","L","W","W"],
        ["L","W","W","L","L"],
        ["L","L","W","W","W"],
    ]
    #iterate through entire grid (rows/colomns)

    visited = set()

    count = 0 
    for r in range(len(grid)):
        for c in range(len(grid[0])):
             if dfs(visited, grid, r, c) == True: count += 1

    print(count)