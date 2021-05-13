class Solution:
    def trailingZeroes(self, n: int) -> int:
        out = 0
        while n // 5 != 0:
            n //= 5
            out += n
        return out
