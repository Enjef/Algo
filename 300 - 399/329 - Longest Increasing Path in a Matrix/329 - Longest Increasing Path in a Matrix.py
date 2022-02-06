class Solution:
    def longestIncreasingPath(self, matrix) -> int: # 46.08% 50.10%
        def bfs(x, y, prev):
            if (not (-1 < x < m and -1 < y < n) or matrix[x][y] <= prev):
                    return 0
            if memo[x][y]:
                return memo[x][y]
            cur = 0
            for ind in range(4):
                new_way = bfs(x + row[ind], y + col[ind], matrix[x][y])
                cur = max(cur, new_way)
            memo[x][y] = cur+1
            return memo[x][y]
        m = len(matrix)
        n = len(matrix[0])
        row = [-1, 0, 0, 1]
        col = [0, -1, 1, 0]
        longest = 1
        memo = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cur_way = bfs(i, j, float('-inf'))
                longest = max(longest, cur_way)
        return longest

    def longestIncreasingPath_best_speed(self, matrix: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i, j):
            val = matrix[i][j]
            res = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return res
        M, N = len(matrix), len(matrix[0])
        return max(dfs(x, y) for x in range(M) for y in range(N))  

    def longestIncreasingPath_2nd_best_memory(self, matrix) -> int:
        def dfs(i, j):
            if not dp[i][j]:
                v = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and v > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and v > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and v > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and v > matrix[i][j + 1] else 0)
            return dp[i][j]
        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))

    def longestIncreasingPath_best_memory(self, matrix) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        result = float('-inf')
        dp = [[ None for j in range(COLS)] for i in range(ROWS)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(pos):
            r, c = pos
            if dp[r][c]:
                return dp[r][c]
            lp = 1
            for dr, dc in directions:
                nr, nc = (r + dr), (c + dc)
                if (
                    nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and
                    matrix[nr][nc] > matrix[r][c]):
                        lp = max(lp, 1 + dfs((nr, nc)))
            dp[r][c] = lp
            return lp
        for r in range(ROWS):
            for c in range(COLS):
                result = max(result, dfs((r,c)))
        return result
