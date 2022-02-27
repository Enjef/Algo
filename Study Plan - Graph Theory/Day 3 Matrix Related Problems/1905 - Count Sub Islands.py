class Solution: # 41.13% 54.43%
    def __init__(self):
        self.good = True
    
    def countSubIslands(self, grid1, grid2) -> int:
        def bfs(row, col):
            if not(-1<row<m and -1<col<n and grid2[row][col]):
                return
            if not grid1[row][col]:
                self.good = False
            grid2[row][col] = 0
            bfs(row, col-1)
            bfs(row, col+1)
            bfs(row-1, col)
            bfs(row+1, col)
            return
        
        m, n = len(grid1), len(grid1[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    self.good = True
                    bfs(i, j)
                    if self.good:
                        res += 1
        return res
