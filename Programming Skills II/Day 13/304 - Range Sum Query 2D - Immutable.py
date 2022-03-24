class NumMatrix:

    def __init__(self, matrix: List[List[int]]):  # 46.93% 56.33%
        m, n = len(matrix), len(matrix[0])
        self.matrix = matrix
        for i in range(1, n):
            matrix[0][i] += matrix[0][i-1]
        for i in range(1, m):
            matrix[i][0] += matrix[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                self.matrix[i][j] += (
                    self.matrix[i-1][j] +
                    self.matrix[i][j-1] -
                    self.matrix[i-1][j-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.matrix[row2][col2] -
            self.matrix[row1-1][col2]*(row1!=0) -
            self.matrix[row2][col1-1]*(col1!=0) +
            self.matrix[row1-1][col1-1]*(row1!=0 and col1!=0)
        )
