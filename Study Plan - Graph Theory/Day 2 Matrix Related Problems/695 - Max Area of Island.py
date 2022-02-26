class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: # 62.54% 21.88%
        def bfs(y, x):
            if not(-1<y<m and -1<x<n and grid[y][x] and (y, x) not in seen):
                return 0
            seen.add((y, x))
            res = 0
            for idx in range(4):
                res += bfs(y+y_dir[idx], x+x_dir[idx])
            return res + 1
        
        m, n = len(grid), len(grid[0])
        seen = set()
        area_max = 0
        y_dir = [0, 0, 1, -1]
        x_dir = [1, -1, 0, 0]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area_max = max(area_max, bfs(i, j))
        return area_max
