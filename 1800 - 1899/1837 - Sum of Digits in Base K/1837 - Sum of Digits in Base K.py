class Solution:
    def sumBase(self, n: int, k: int) -> int:  # 5.03% 46.15%, 2nd run: 30% 46%
        res = 0
        while n > 0:
            res += n % k
            n //= k
        return res
