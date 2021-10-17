class NumMatrix:
    def __init__(self, matrix: List[List[int]]):  # 83.80% 70.10%
        n = len(matrix)
        m = len(matrix[0])
        mat = [matrix[0][:]]
        for i in range(1, len(mat[0])):
            mat[0][i] += mat[0][i-1]
        mat.extend([[0 for _ in range(m)] for _ in range(n-1)])
        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    mat[i][j] += matrix[i][j] + mat[i-1][j]
                else:
                    mat[i][j] += (
                        matrix[i][j] + mat[i-1][j] +
                        mat[i][j-1] - mat[i-1][j-1]
                        )
        self.matrix = mat

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.matrix[row2][col2]
        if row1 > 0:
            res -= self.matrix[row1-1][col2]
        if col1 > 0:
            res -= self.matrix[row2][col1-1]
        if row1 > 0 and col1 > 0:
            res += self.matrix[row1-1][col1-1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)