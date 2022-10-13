class Solution:
    # 90.06% 55.10% (93.77% 94.59%)
    def partitionString(self, s: str) -> int:
        prev = set()
        res = 0
        for char in s:
            if char in prev:
                prev = set()
                res += 1
            prev.add(char)
        return res + int(not not prev)

    def partitionString_best_speed(self, s: str) -> int:
        res = 0
        tmp = ''
        for c in s:
            if c not in tmp:
                tmp += c
            else:
                tmp = c
                res += 1
        res += 1 if tmp else 0
        return res
