class Solution:
    def uniquePaths(self, m: int, n: int) -> int:  # 90.12% 66.56%
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]
