class Solution:
    def matrixReshape_study_plan_day_4(
            self,
            mat: List[List[int]],
            r: int,
            c: int) -> List[List[int]]:
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
