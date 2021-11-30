class Solution(object):
    def getRow(self, rowIndex):  # 83.97% 42.07%
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

    def getRow_ds2_day_3(self, rowIndex: int) -> List[int]:  # 70.11% 20.68%
        out = [1]
        for i in range(rowIndex):
            row = [1]
            for j in range(1, len(out)):
                row.append(out[j-1]+out[j])
            row.append(1)
            out = row
        return out

    def getRow_best_speed(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """    
        i, j = 1, 1
        previous = [1]
        current = []
        while i <= rowIndex:
            current.append(1)
            while j < i:
                current.append(previous[j-1] + previous[j])
                j += 1
            current.append(1)
            i += 1
            j = 1
            previous = current
            current = []
        return previous

    def getRow_best_memory(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        prev = [[1,1]]
        for i in range(2,rowIndex+2):
            prev = [1] + [prev[j]+prev[j+1] for j in range(len(prev)-1)] + [1]
        return prev
