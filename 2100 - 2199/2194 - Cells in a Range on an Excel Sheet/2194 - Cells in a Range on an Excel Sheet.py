class Solution:
    def cellsInRange(self, s: str) -> List[str]:  # 83.81% 72.61%
        row_st, row_fin = int(s[1]), int(s[-1])
        col_st, col_fin = s[0], s[3]
        result = []
        for col in range(ord(col_st), ord(col_fin)+1):
            result.extend(
                [f'{chr(col)}{str(row)}' for row in range(row_st, row_fin+1)])
        return result

    def cellsInRange_best_speed(self, s: str) -> List[str]:
        return [chr(col) + chr(row)
                for col in range(ord(s[0]), ord(s[3]) + 1)
                for row in range(ord(s[1]), ord(s[4]) + 1)]

    def cellsInRange_best_memory(self, s: str) -> List[str]:
        chStart = ord(s[0])
        chEnd = ord(s[3])
        digStart = int(s[1])
        digEnd = int(s[4])
        ret = []
        for i in range(chStart, chEnd+1):
            for j in range(digStart, digEnd+1):
                ret.append(chr(i)+str(j))
        return ret
