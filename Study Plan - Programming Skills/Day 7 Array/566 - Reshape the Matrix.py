class Solution:
    def matrixReshape(self, mat, r, c):  # 59.11% 90.20%
        def next_el(arr):
            for i in range(m):
                for j in range(n):
                    yield arr[i][j]
        
        m, n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat
        stack = next_el(mat)
        out = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(next(stack))
            out.append(row)
        return out
