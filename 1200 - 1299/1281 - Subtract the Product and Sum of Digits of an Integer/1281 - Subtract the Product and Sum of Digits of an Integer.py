class Solution:
    def subtractProductAndSum(self, n: int) -> int: # 83.82% 35.39%
        out = 1
        d_sum = 0
        z = n
        while z:
            out *= z % 10
            d_sum += z % 10
            z //= 10
        return out - d_sum

    def subtractProductAndSum_study_plan(self, n: int) -> int: # 55.77% 78.69%
        digs = [int(x) for x in str(n)]
        mult = 1
        for el in digs:
            mult *= el
        return mult - sum(digs)

    def subtractProductAndSum_best_speed(self, n: int) -> int:
        _sum = 0
        _prod = 1
        while n > 0:
            n, temp = divmod(n, 10)
            _sum += temp
            _prod *= temp
        return _prod - _sum

    def subtractProductAndSum_2nd_best_speed(self, n: int) -> int:
        digits = []
        while n:
            digits.append(n % 10)
            n = int(n / 10)
        m = 1
        for i in digits:
            m *= i
        return m - sum(digits)

    def subtractProductAndSum_best_memory(self, n: int) -> int:
        res = 1
        ss = [int(i) for i in str(n)]
        for x in ss:
            res *= x
        return res-sum(ss)
