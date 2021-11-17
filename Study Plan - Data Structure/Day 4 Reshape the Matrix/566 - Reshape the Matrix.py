class Solution:
    def matrixReshape_study_plan_day_4(
            self,
            mat: List[List[int]],
            r: int,
            c: int) -> List[List[int]]:  # 5.94% 73.86%
        if (
                len(mat) == r and len(mat[0]) == c
                or len(mat) * len(mat[0]) != r * c):
            return mat
        out = [[]]
        temp_c = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                out[-1].append(mat[i][j])
                temp_c += 1
                if temp_c == c:
                    temp_c = 0
                    out.append([])
        out.pop()
        return out

    def matrixReshape_sp_v2(
            self,
            mat: List[List[int]],
            r: int,
            c: int) -> List[List[int]]:  # 87.41% 19.87%
        m, n = len(mat), len(mat[0])
        if m == r and n == c or m * n != r * c:
            return mat
        new_mat = [[0]*c for _ in range(r)]
        ii = jj = 0
        for i in range(m):
            for j in range(n):
                new_mat[ii][jj] = mat[i][j]
                jj += 1
                if jj == c:
                    jj = 0
                    ii += 1
                    if ii == r:
                        ii = 0
        return new_mat
