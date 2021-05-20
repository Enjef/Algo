class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        if n == 0:
            return a
        if n == 1:
            return b
        while n-1 > 0:
            a, b = b, a + b
            n -= 1
        return b
