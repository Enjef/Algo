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

class Solution_v2: # 56.83% 38.79%
    def __init__(self):
        self.boundary = False
        
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(row, col):
            if not(-1<row<m and -1<col<n):
                self.boundary = True
                return 0
            if -1<row<m and -1<col<n and not grid[row][col]:
                return 0
            grid[row][col] = 0
            return bfs(row, col-1)+bfs(row, col+1)+bfs(row-1, col)+bfs(row+1, col) + 1

        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    self.boundary = False
                    cur = bfs(i, j)
                    if not self.boundary:
                        res += cur
        return res
            
