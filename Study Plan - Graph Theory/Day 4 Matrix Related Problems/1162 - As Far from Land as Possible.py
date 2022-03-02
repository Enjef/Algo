class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:  # 58.13% 11.54%
        n = len(grid)
        total = 0
        current = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    current.update([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
                    total += 1
        if not current or total == n*n:
            return -1
        out = -1
        while current:
            temp = set()
            while current:
                row, col = current.pop()
                if not(-1<col<n and -1<row<n) or grid[row][col]:
                    continue
                grid[row][col] = 1
                temp.update(
                    [(row+1, col), (row-1, col), (row, col+1), (row, col-1)])
            out += 1
            current = temp
        return out
