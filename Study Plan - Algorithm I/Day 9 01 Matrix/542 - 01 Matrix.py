class Solution:
    def updateMatrix(
            self,
            mat: List[List[int]]) -> List[List[int]]:  # 69.89% 75.32%
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    up = mat[i-1][j] if i > 0 else 10001
                    left = mat[i][j-1] if j > 0 else 10001
                    mat[i][j] = min(up, left) + 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if mat[i][j] != 0:
                    down = mat[i+1][j] if i < n-1 else 10001
                    right = mat[i][j+1] if j < m-1 else 10001
                    mat[i][j] = min(mat[i][j], min(down, right)+1)
        return mat
