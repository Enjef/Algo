class Solution:
    def addToArrayForm(self, num, k):  # 55.43% 37.80%
        cur = 0
        for el in num:
            cur = cur*10 + el
        return [int(x) for x in str(cur+k)]

    def addToArrayForm_v2(self, num, k):  # 28.93% 94.47%
        cur = 0
        for el in num:
            cur = cur*10 + el
        return list(str(cur+k))
