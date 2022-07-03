class Solution:
    # 88.44% 63.58%
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(y, x):
            if not(-1 < y < m and -1 < x < n and grid[y][x] == '1'):
                return
            grid[y][x] = '0'
            for idx in range(4):
                bfs(y+y_dir[idx], x+x_dir[idx])
            return

        m, n, count = len(grid), len(grid[0]), 0
        x_dir, y_dir = [0, 0, -1, 1], [-1, 1, 0, 0]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        return count
