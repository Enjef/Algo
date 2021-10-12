class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:  # 22.45% 51.02%
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    total += 2 + grid[i][j] * 4
                    if i > 0 and grid[i-1][j]:
                        total -= min(grid[i-1][j], grid[i][j])
                    if i < len(grid) - 1 and grid[i+1][j]:
                        total -= min(grid[i][j], grid[i+1][j])
                    if j > 0 and grid[i][j-1]:
                        total -= min(grid[i][j], grid[i][j-1])
                    if j < len(grid[0]) - 1 and grid[i][j+1]:
                        total -= min(grid[i][j], grid[i][j+1])
        return total

    def surfaceArea_ref(self, grid: List[List[int]]) -> int:  # 84.49% 19.59%
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    total += 2 + grid[i][j] * 4
                    if i > 0 and grid[i-1][j]:
                        total -= 2 * min(grid[i][j], grid[i-1][j])
                    if j > 0 and grid[i][j-1]:
                        total -= 2 * min(grid[i][j], grid[i][j-1])
        return total

    def surfaceArea_best_speed(self, grid):
        top = 0
        for row in grid:
            for num in row:
                if num > 0:
                    top += 1
        left = 0
        for row in grid:
            std = 0
            for num in row:
                if num - std > 0:
                    left += num - std
                std = num
        front = 0
        for i in range(len(grid[0])):
            std = 0
            for row in grid:
                if row[i] - std > 0:
                    front += row[i] - std
                std = row[i]
        return 2 * (top + left + front)

    def surfaceArea_best_memory(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row != 0:
                    res -= 2 * min(grid[row][col], grid[row - 1][col])
                if col != 0:
                    res -= 2 * min(grid[row][col], grid[row][col - 1])
                res += 4 * grid[row][col]
                res += 0 if not grid[row][col] else 2
        return res
