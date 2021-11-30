class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:  # 69.19% 85.72%
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = matrix[::-1]
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
