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

    def updateMatrix_best_speed(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if mat[0][0]:
            mat[0][0] = float('inf')
        if mat[-1][-1]:
            mat[-1][-1] = float('inf')
        for i, row in enumerate(mat):
            for j, col in enumerate(row):
                if col:
                    if i and j:
                        mat[i][j] = min(mat[i-1][j], mat[i][j-1]) + 1
                    elif i:
                        mat[i][j] = mat[i-1][j] + 1
                    elif j:
                        mat[i][j] = mat[i][j-1] + 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if mat[i][j]:
                    if i < m - 1 and j < n - 1:
                        mat[i][j] = min(mat[i][j], mat[i+1][j]+1, mat[i][j+1]+1)
                    elif i < m - 1:
                        mat[i][j] = min(mat[i][j], mat[i+1][j]+1)
                    elif j < n - 1:
                        mat[i][j] = min(mat[i][j], mat[i][j+1]+1)
        return mat

    def updateMatrix_best_memory(self, mat):
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]
        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1:
                    continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat
