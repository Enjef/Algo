class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:  # 45.60% 42.47%
        def search(r, c):
            if grid[r][c] != '1':
                return
            grid[r][c] = '0'
            if r > 0:
                search(r-1, c)
            if r < len(grid)-1:
                search(r+1, c)
            if c > 0:
                search(r, c-1)
            if c < len(grid[0])-1:
                search(r, c+1)
            return

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    search(i, j)
                    count += 1
        return count
