class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        out = []
        row = []
        k = 0
        if len(mat) * len(mat[0]) != c * r:
            return mat
        for item in mat:
            for el in item:
                row.append(el)
                if len(row) == c:
                    out.append(row)
                    row = []
        return out
