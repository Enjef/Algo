class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:  # 92.19% 76.36%
        out = 0
        n = len(mat)
        for i in range(n):
            out += mat[i][i] + mat[i][n-i-1]
        return out - n%2 * mat[n//2][n//2]
