from copy import deepcopy


class Solution:
    def matrixBlockSum(
            self,
            mat: List[List[int]],
            k: int) -> List[List[int]]:  # 7.75% 94.58%
        old = copy.deepcopy(mat)
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                mat[i][j] = 0
                for r in range(max(0, i-k), min(n, i+k+1)):
                    mat[i][j] += sum(old[r][max(0, j-k): min(m, j+k+1)])
        return mat
