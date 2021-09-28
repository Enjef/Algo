class Solution:
    def uniquePaths(self, m: int, n: int) -> int:  # 88.41% 65.89%
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]
        return dp[n-1]
