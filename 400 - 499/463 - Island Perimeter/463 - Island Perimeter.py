class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int: # 90.11% 37.40%
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

    def islandPerimeter_mock(self, grid) -> int: # 6.79% 97.48%
        out = 0
        n, m = len(grid), len(grid[0])
        y_move = [-1, 0, 0, 1]
        x_move = [0, 1, -1, 0]
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    for idx in range(4):
                        x, y = j + y_move[idx], i + x_move[idx]
                        if not(-1 < x < m and -1 < y < n):
                            out += 1
                        if -1 < x < m and -1 < y < n and not grid[y][x]:
                            out += 1
        return out

    def islandPerimeter_best_speed(self, grid: List[List[int]]) -> int:
        oneCount = 0
        neighbor = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
          for j in range(n):
            if grid[i][j] == 1:
              oneCount += 1
              if i + 1 < m and grid[i + 1][j] == 1:
                neighbor += 1
              if j + 1 < n and grid[i][j + 1] == 1:
                neighbor += 1
        return oneCount * 4 - neighbor * 2

    def islandPerimeter_2nd_best_speed(self, grid: List[List[int]]) -> int:
        perimeter = 0
        m, n = len(grid), len(grid[0])
        for y in range(m):
            for x in range(n):
                if grid[y][x]:
                    perimeter += 4
                    if y > 0 and grid[y-1][x]:
                        perimeter -= 2
                    if x > 0 and grid[y][x-1]:
                        perimeter -= 2
        return perimeter

    def islandPerimeter_best_memory(self, grid: List[List[int]]) -> int:
        per = 0
        for i in range(len(grid)):
            if sum(grid[i]) != 0: 
                for j in range(len(grid[0])):
                    if  grid[i][j]== 1:
                        per += 4
                        if j !=0 and grid[i][j-1] == 1:
                            per-=1
                        if j !=len(grid[0])-1 and grid[i][j+1] == 1:
                            per-=1
                        if i != 0 and grid[i-1][j] == 1:
                            per -= 1
                        if i != len(grid)-1 and grid[i+1][j] == 1:
                            per -= 1
        return per
