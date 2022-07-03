class Solution:
    # 32.88% 56.99%
    def climbStairs(self, n: int) -> int:
        a = b = 1
        while n:
            n -= 1
            a, b = a + b, a
        return b
