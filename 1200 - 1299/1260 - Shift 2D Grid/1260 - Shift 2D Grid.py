class Solution:
    def shiftGrid(
            self,
            grid: List[List[int]],
            k: int) -> List[List[int]]:  # 89.21% 19.82%
        mat_size = len(grid) * len(grid[0])
        k = k % mat_size
        if k == 0:
            return grid
        arr = []
        for row in grid:
            arr.extend(row)
        arr = arr[-k:] + arr[:-k]
        z = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = arr[z]
                z += 1
        return grid

    def shiftGrid_refactored(
            self,
            grid: List[List[int]],
            k: int) -> List[List[int]]:  # 89.21% 68.51%
        arr = []
        for row in grid:
            arr.extend(row)
        k = k % len(arr)
        if k == 0:
            return grid
        arr = arr[-k:] + arr[:-k]
        z = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = arr[z]
                z += 1
        return grid

    def shiftGrid_daily(self, grid, k):  # 100.00% 35.10%
        m, n = len(grid), len(grid[0])
        k %= m * n
        arr = []
        for row in grid:
            arr.extend(row)
        arr = arr[-k:] + arr[:-k]
        for i in range(m):
            grid[i] = arr[i*n:i*n+n]
        return grid

    def shiftGrid_best(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        total = []
        for row in grid:
            total.extend(row)
        k %= len(total)
        total = total[len(total) - k:] + total[:len(total) - k]
        new_grid = []
        for i in range(0, len(total) - C + 1, C):
            new_grid.append(total[i:i+C])
        return new_grid
