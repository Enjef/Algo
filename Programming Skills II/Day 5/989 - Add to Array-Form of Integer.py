class Solution:
    def addToArrayForm(self, num, k):  #
        cur = 0
        for el in num:
            cur = cur*10 + el
        return [int(x) for x in str(cur+k)]