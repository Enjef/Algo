class Solution:
    def shortestPathBinaryMatrix(self, grid):  # 69.85% 77.05%
        stack = [(0, 0)]
        n = len(grid)
        way = 10001
        r_dir = [-1, -1, -1, 0, 0, 1, 1, 1]
        c_dir = [-1, 0, 1, -1, 1, -1, 0, 1]
        cur = 1
        while stack:
            temp = []
            while stack:
                row, col = stack.pop()
                if not(-1<row<n and -1<col<n) or grid[row][col]:
                    continue
                grid[row][col] = 1
                if (row, col) == (n-1, n-1):
                    return cur
                for idx in range(8):
                    temp.append((row+r_dir[idx], col+c_dir[idx]))
            stack = temp
            cur += 1
        return -1
