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


class Solution_best_speed:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dp = [[float('inf')] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    left = dp[r][c-1] if c != 0 else float('inf')
                    top = dp[r-1][c] if r != 0 else float('inf')
                    dp[r][c] = min(dp[r][c], 1 + left, 1 + top)
        max_dist = 0
        for r in range(N-1,-1,-1):
            for c in range(N-1,-1,-1):
                if grid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    right = dp[r][c+1] if c < N-1 else float('inf')
                    bottom = dp[r+1][c] if r < N-1 else float('inf')
                    dp[r][c] = min(dp[r][c], 1 + right, 1 + bottom)
                    max_dist = max(max_dist, dp[r][c])
        if max_dist == 0 or max_dist == float('inf'):
            return -1
        else:
            return max_dist


class Solution_best_memory:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = 1000
        for i in range(n):
            for j in range(n):
                if i:
                    grid[i][j] = min(grid[i-1][j] + 1, grid[i][j])
                if j:
                    grid[i][j] = min(grid[i][j], 1+ grid[i][j-1])
        for i in range(n)[::-1]:
            for j in range(n)[::-1]:
                if i < n - 1:
                    grid[i][j] = min(grid[i][j], grid[i+1][j] + 1)

                if j < n - 1:
                    grid[i][j] = min(grid[i][j], grid[i][j+1] + 1)
        ans = max(max(grid[i]) for i in range(n))
        if ans >= 1000 or ans == 0:
            return -1
        return ans
