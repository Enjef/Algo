class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:  # 74.52% 19.50%
        up_border = left_border = 0
        down_border = right_border = n - 1
        mat = [[0]*n for _ in range(n)]
        mat[0][0] = 1
        i = j = 0
        cur = 1
        while cur < n * n:
            if i == up_border and j == left_border:
                if not(i == 0 and j == 0):
                    left_border += 1
                while j < right_border:
                    j += 1
                    cur += 1
                    mat[i][j] = cur
            elif i == up_border and j == right_border:
                up_border += 1
                while i < down_border:
                    i += 1
                    cur += 1
                    mat[i][j] = cur
            elif i == down_border and j == right_border:
                right_border -= 1
                while j > left_border:
                    j -= 1
                    cur += 1
                    mat[i][j] = cur
            elif i == down_border and j == left_border:
                down_border -= 1
                while i > up_border:
                    i -= 1
                    cur += 1
                    mat[i][j] = cur
        return mat
