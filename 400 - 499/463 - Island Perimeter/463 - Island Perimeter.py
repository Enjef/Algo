class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0:
                        perimeter += 1
                    else:
                        if grid[i-1][j] != 1:
                            perimeter += 1
                    if i == len(grid) - 1:
                        perimeter += 1
                    else:
                        if grid[i+1][j] != 1:
                            perimeter += 1
                    if j == 0:
                        perimeter += 1
                    else:
                        if grid[i][j-1] != 1:
                            perimeter += 1
                    if j == len(grid[0]) - 1:
                        perimeter += 1
                    else:
                        if grid[i][j+1] != 1:
                            perimeter += 1
        return perimeter
