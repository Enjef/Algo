class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:  # 62.68% 97.45%
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] += dp[j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] += grid[i][j]
                    continue
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        return dp[-1]
