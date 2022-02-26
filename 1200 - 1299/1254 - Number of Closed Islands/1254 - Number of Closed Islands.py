class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:  # 62.38% 8.49%
        def bfs(y, x):
            if not(0 < y < m-1 and 0 < x < n-1):
                return grid[y][x]
            if (0 < y < m-1 and 0 < x < n-1) and grid[y][x] or (y, x) in seen:
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


class Solution_best_speed:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if grid[i][j] == 1:
                return True
            if i <= 0 or i >= m-1 or j <= 0 or j >= n-1:
                return False
            grid[i][j] = 1
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            return left and right and up and down

        m, n = len(grid), len(grid[0])
        c = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0 and dfs(i, j):
                    c += 1
        return c


class Solution_best_memory:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        result = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==0:
                    result += self.is_island(grid, r, c)
        return result
        
    def is_island(self, grid, r,c):
        grid[r][c] = -1
        island_status = True
        if r==0 or c==0 or r==len(grid)-1 or c==len(grid[0])-1:
            island_status = False

        directions = [(r+1, c), (r-1,c), (r, c+1), (r, c-1)]
        for (x,y) in directions:
            if (
                0<=x<len(grid) and 0<=y<len(grid[0]) and
                grid[x][y]==0
            ):
                visit_status = self.is_island(grid, x, y)
                island_status &= visit_status
        return island_status
