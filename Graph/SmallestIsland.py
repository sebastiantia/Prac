

from numpy import Infinity


def dfs(visited, grid, r, c):
    if r < 0 or r >= len(grid):
        return 0
    if c < 0 or c >= len(grid[0]):
        return 0

    if grid[r][c] == "W":
        return 0
    cords = str(r) + "," + str(c)
    if cords in visited:
        return 0

    visited.add(cords)

    size = 1

    size += dfs(visited, grid, r+1, c)
    size += dfs(visited, grid, r-1, c)
    size += dfs(visited, grid, r, c+1)
    size += dfs(visited, grid, r, c-1)

    return size


if __name__ == "__main__":
    grid = [
        ["w", "L", "W", "L", "W"],
        ["L", "L", "W", "L", "W"],
        ["w", "L", "W", "W", "W"],
        ["w", "W", "L", "L", "W"],
        ["L", "W", "L", "L", "W"],
        ["L", "L", "W", "W", "W"],
    ]
    # iterate through entire grid (rows/colomns)

    visited = set()

    smallestIsland = Infinity
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            islandSize = dfs(visited, grid, r, c)
            # print(islandSize)
            if islandSize < smallestIsland and islandSize > 0 :
                smallestIsland = islandSize

    print(smallestIsland)
