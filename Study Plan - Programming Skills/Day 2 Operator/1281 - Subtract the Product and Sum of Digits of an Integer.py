class Solution:
    def subtractProductAndSum(self, n: int) -> int: # 55.77% 78.69%
        digs = [int(x) for x in str(n)]
        mult = 1
        for el in digs:
            mult *= el
        return mult - sum(digs)
