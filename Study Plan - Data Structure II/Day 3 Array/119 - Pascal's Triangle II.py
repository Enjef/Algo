class Solution:
    def getRow(self, rowIndex: int) -> List[int]:  # 70.11% 20.68%
        out = [1]
        for i in range(rowIndex):
            row = [1]
            for j in range(1, len(out)):
                row.append(out[j-1]+out[j])
            row.append(1)
            out = row
        return out
