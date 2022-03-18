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
