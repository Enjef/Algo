class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:  # 12.04 %
        out = 0
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if row == col:
                    out += mat[row][col]
                if row != col and abs(row + col) == len(mat) - 1:
                    out += mat[row][col]
        return out

    def diagonalSum_best(self, mat: List[List[int]]) -> int:
        sm = 0
        n = len(mat[0])
        for i in range(len(mat)):
            sm += mat[i][i] + mat[i][n - i - 1]
        return sm if n % 2 == 0 else sm - mat[n // 2][n // 2]

    def diagonalSum_study_plan(self, mat) -> int:  # 92.19% 76.36%
        out = 0
        n = len(mat)
        for i in range(n):
            out += mat[i][i] + mat[i][n-i-1]
        return out - n%2 * mat[n//2][n//2]
