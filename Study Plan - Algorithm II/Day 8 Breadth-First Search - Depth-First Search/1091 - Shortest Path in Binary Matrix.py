class Solution:
    def shortestPathBinaryMatrix(
            self,
            grid: List[List[int]]) -> int:  # 62.75% 64.69%
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid)-1] == 1:
            return -1
        stack = [(0, 0, 1)]
        grid[0][0] = 1
        while stack:
            i, j, path = stack.pop(0)
            if i == len(grid)-1 and j == len(grid[0])-1 and grid[i][j]:
                return path
            for x, y in (
                    (i-1, j-1), (i-1, j), (i-1, j+1),
                    (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                if (
                        0 <= x < len(grid) and
                        0 <= y < len(grid[0]) and
                        grid[x][y] == 0):
                    grid[x][y] = 1
                    stack.append((x, y, path+1))
        return -1
