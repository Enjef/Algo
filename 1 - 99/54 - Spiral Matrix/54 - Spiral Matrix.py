class Solution:
    def spiralOrder(self, matrix):  # 24.16%  49.17%
        size = len(matrix) * len(matrix[0])
        row_min, row_max = 0, len(matrix)
        col_min, col_max = 0, len(matrix[0])
        out = []
        while len(out) != size:
            for i in range(col_min, col_max):
                out.append(matrix[row_min][i])
            if len(out) == size:
                return out
            row_min += 1
            for i in range(row_min, row_max):
                out.append(matrix[i][col_max-1])
            if len(out) == size:
                return out
            col_max -= 1
            for i in range(col_max-1, col_min-1, -1):
                out.append(matrix[row_max-1][i])
            if len(out) == size:
                return out
            row_max -= 1
            for i in range(row_max-1, row_min-1, -1):
                out.append(matrix[i][col_min])
            if len(out) == size:
                return out
            col_min += 1
        return out


class Solution:
    def spiralOrder_v2(self, matrix):  # 54.12%s 88.09%
        size = len(matrix) * len(matrix[0])
        row_min, row_max = 0, len(matrix)
        col_min, col_max = 0, len(matrix[0])
        out = []
        while len(out) != size:
            for i in range(col_min, col_max):
                out.append(matrix[row_min][i])
            row_min += 1
            for i in range(row_min, row_max):
                out.append(matrix[i][col_max-1])
            col_max -= 1
            if len(out) == size:
                break
            for i in range(col_max-1, col_min-1, -1):
                out.append(matrix[row_max-1][i])
            row_max -= 1
            for i in range(row_max-1, row_min-1, -1):
                out.append(matrix[i][col_min])
            col_min += 1
        return out

    def spiralOrder_best_speed(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n-1
        top, bottom = 0, m-1
        ans = []
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right or top > bottom:
                break
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
            left += 1
        return ans
