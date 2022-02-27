class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int: # 33.73% 38.79%
        def bfs(row, col):
            nonlocal boundary
            if not(-1<row<m and -1<col<n):
                boundary = True
                return 0
            if -1<row<m and -1<col<n and not grid[row][col]:
                return 0
            grid[row][col] = 0
            return (
                bfs(row, col-1) +
                bfs(row, col+1) +
                bfs(row-1, col) +
                bfs(row+1, col) + 1
            )

        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    boundary = False
                    cur = bfs(i, j)
                    if not boundary:
                        res += cur
        return res

    def numEnclaves_best_speed(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        def dfs(i, j):
            if i < 0 or i >=  m or j < 0 or j >= n or A[i][j] != 1:
                return 
            A[i][j] = 0
            for di, dj in (1,0), (0,1), (-1,0), (0,-1):
                dfs(i+di, j+dj)
        if not A:
            return 0
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        return sum(sum(row) for row in A)

class Solution_memory_best:
    def dfs(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i, j - 1)
            
    def numEnclaves(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or i == len(grid) - 1 or j ==0 or j == len(grid[0]) - 1) and grid[i][j] == 1:
                    self.dfs(grid, i, j)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 1
        
        return res
