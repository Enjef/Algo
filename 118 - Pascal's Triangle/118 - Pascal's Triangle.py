class Solution(object):
    def generate(self, numRows):
        out = [[1]]
        cur = []
        if numRows == 1:
            return out
        out.append([1, 1])
        if numRows == 2:
            return out
        for i in range(2, numRows):
            cur = (i+1) * [1]
            for j in range(1, len(cur) - 1):
                cur[j] = out[-1][j-1] + out[-1][j]
            out.append(cur)
        return out
