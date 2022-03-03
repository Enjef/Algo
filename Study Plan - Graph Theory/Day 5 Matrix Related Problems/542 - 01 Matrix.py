class Solution:
    def updateMatrix(self, mat):  # 5.01% 75.40%
        m, n = len(mat), len(mat[0])
        r_dir = [0, 0, -1, 1]
        c_dir = [-1, 1, 0, 0]
        out = [[0]*n for _ in range(m)]
        seen = set()
        stack = []
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    stack.append((i, j))
                    seen.add((i, j))
        cur = 1
        while stack:
            temp = []
            while stack:
                row, col = stack.pop()
                for idx in range(4):
                    y = row+r_dir[idx]
                    x = col+c_dir[idx]
                    if not(-1<y<m and -1<x<n) or (y, x) in seen:
                        continue
                    out[y][x] = cur
                    temp.append((y, x))
                    seen.add((y, x))
            stack = temp
            cur += 1
        return out
