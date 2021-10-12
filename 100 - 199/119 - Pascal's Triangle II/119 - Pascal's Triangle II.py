class Solution(object):
    def getRow(self, rowIndex):
        out = [1]
        if rowIndex == 0:
            return out
        out = [1, 1]
        if rowIndex == 1:
            return out
        for i in range(2, rowIndex+1):
            cur = [1]
            for j in range(1, i):
                cur.append(out[j-1] + out[j])
            cur.append(1)
            out = cur
        return out
