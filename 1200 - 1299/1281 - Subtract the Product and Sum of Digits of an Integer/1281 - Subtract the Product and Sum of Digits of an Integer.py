class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        out = 1
        d_sum = 0
        z = n
        while z:
            out *= z % 10
            d_sum += z % 10
            z //= 10
        return out - d_sum
