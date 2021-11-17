class Solution:
    def generate(self, numRows: int) -> List[List[int]]:  # 17.61% 81.94%
        out = [[1], [1, 1]]
        if numRows == 1:
            return [out[0]]
        for _ in range(numRows-2):
            out.append([1])
            for j in range(1, len(out[-2])):
                out[-1].append(out[-2][j-1] + out[-2][j])
            out[-1].append(1)
        return out

    def generate_v2(self, numRows: int) -> List[List[int]]:  # 66.99% 81.94%
        out = [[1]]
        for _ in range(numRows-1):
            new_row = [1]
            prev = out[-1]
            for i in range(1, len(prev)):
                new_row.append(prev[i-1]+prev[i])
            new_row.append(1)
            out.append(new_row)
        return out
