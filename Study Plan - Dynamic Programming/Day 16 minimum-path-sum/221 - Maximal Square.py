class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:  # 72.95% 51.08%
        area = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                area = max(area, dp[i+1][j+1])
        return area ** 2
