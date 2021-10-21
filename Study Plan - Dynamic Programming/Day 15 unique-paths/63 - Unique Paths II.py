class Solution:
    def uniquePathsWithObstacles(
            self,
            obstacleGrid: List[List[int]]) -> int:  # 30.60% 60.64%
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1
        for i in range(m):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
