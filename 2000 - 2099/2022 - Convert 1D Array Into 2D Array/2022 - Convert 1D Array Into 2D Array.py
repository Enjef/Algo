class Solution:
    def construct2DArray(
            self,
            original: List[int],
            m: int,
            n: int) -> List[List[int]]:  # 85.71% 100.00%
        if n * m != len(original):
            return []
        mat = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(original[n*i+j])
            mat.append(row)
        return mat
