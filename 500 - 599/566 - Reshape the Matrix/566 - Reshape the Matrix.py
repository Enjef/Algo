class Solution:
    def matrixReshape(
            self,
            mat: List[List[int]],
            r: int,
            c: int) -> List[List[int]]:  # 60.73% 72.96%
        out = []
        row = []
        if len(mat) * len(mat[0]) != c * r:
            return mat
        for item in mat:
            for el in item:
                row.append(el)
                if len(row) == c:
                    out.append(row)
                    row = []
        return out

    def matrixReshape_study_plan_day_4(
            self,
            mat: List[List[int]],
            r: int,
            c: int) -> List[List[int]]:  # 5.24% 72.96%
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
