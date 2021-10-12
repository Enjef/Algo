class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:  # 96.64% 59.65%
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return
