class Solution:
    # 28.86% 54.38%
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        for _ in range(n):
            a, b = a + b, a
        return a
