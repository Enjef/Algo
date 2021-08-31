class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1], [1, 1]]
        if numRows == 1:
            return [out[0]]
        for _ in range(numRows-2):
            out.append([1])
            for j in range(1, len(out[-2])):
                out[-1].append(out[-2][j-1] + out[-2][j])
            out[-1].append(1)
        return out
