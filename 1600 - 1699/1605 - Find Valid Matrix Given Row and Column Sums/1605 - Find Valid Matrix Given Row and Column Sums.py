class Solution:
    def restoreMatrix(self, rowSum, colSum):  # 18.37% 87.82%
        n, m = len(rowSum), len(colSum)
        res = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                cur = min(rowSum[i], colSum[j])
                res[i][j] = cur
                rowSum[i] -= cur
                colSum[j] -= cur
        return res

    def restoreMatrix_best_speed(self, rowSum, colSum):
        row_sum = rowSum
        col_sum = colSum
        mat = [([0]*len(col_sum)) for i in range(len(row_sum))]
        i = 0
        j = 0
        while i < len(row_sum) and j < len(col_sum):
            mat[i][j] = min(row_sum[i], col_sum[j])
            if row_sum[i] == col_sum[j]:
                i += 1
                j += 1
            elif row_sum[i] > col_sum[j]:
                row_sum[i] -= col_sum[j]
                j += 1
            else:
                col_sum[j] -= row_sum[i]
                i += 1
        return mat
