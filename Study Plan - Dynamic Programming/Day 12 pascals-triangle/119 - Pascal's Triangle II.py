class Solution:
    def getRow(self, rowIndex: int) -> List[int]:  # 88.34% 92.55%
        row = [1]
        for i in range(rowIndex):
            new_row = [1]
            for i in range(1, len(row)):
                new_row.append(row[i]+row[i-1])
            new_row.append(1)
            row = new_row
        return row
