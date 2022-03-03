class Solution:
    def nearestExit(self, maze, entrance):  # 53.38% 95.57%
        m, n = len(maze), len(maze[0])        
        er, ec = entrance
        borders = set()
        r_dir = [-1, 1, 0, 0]
        c_dir = [0, 0, -1, 1]
        for i in range(m):
            if maze[i][0] == '.':
                borders.add((i, 0))
            if maze[i][n-1] == '.':
                borders.add((i, n-1))
        for i in range(n):
            if maze[0][i] == '.':
                borders.add((0, i))
            if maze[m-1][i] == '.':
                borders.add((m-1, i))
        borders.discard((er, ec))
        res = 0
        while borders:
            temp = set()
            while borders:
                r, c = borders.pop()
                if (r, c) == (er, ec):
                    return res
                maze[r][c] = '+'
                for i in range(4):
                    row, col = r+r_dir[i], c+c_dir[i]
                    if -1<row<m and -1<col<n and maze[row][col] == '.':
                        temp.add((row, col))
            borders = temp
            res += 1
        return -1
        