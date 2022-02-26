class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int: # 62.38% 8.49%
        def bfs(y, x):
            if not(0<y<m-1 and 0<x<n-1):
                return grid[y][x]
            if (0<y<m-1 and 0<x<n-1) and grid[y][x] or (y, x) in seen:
                return 1
            seen.add((y, x))
            up = bfs(y-1, x)
            left = bfs(y, x-1)
            right = bfs(y, x+1)
            down = bfs(y+1, x)
            return up and left and right and down
        
        m, n = len(grid), len(grid[0])
        seen = set()
        res = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not grid[i][j] and (i, j) not in seen:
                    res += bfs(i, j)
        return res
