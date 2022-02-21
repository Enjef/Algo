class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int: # 31.66% 89.58%
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        out = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                out += dp[i+1][j+1]
        return out

    def countSquares_best_speed(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        m = [row[:] for row in matrix]
        for row in range(1, M):
            for col in range(1, N):
                if (
                    m[row][col] and m[row-1][col-1] and m[row-1][col] and
                    m[row][col-1]):
                        m[row][col] += min(
                                m[row-1][col-1], m[row-1][col], m[row][col-1]
                        )
        return sum((sum(row) for row in m))
