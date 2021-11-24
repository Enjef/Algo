class Solution:
    def fib(self, n: int) -> int:  # 85.26% 42.68%
        a = 0
        b = 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        while n:
            n -= 1
            a, b = b, a + b
        return a

    def fib_for(self, n: int) -> int:
        a, b = 0, 1
        if n == 0:
            return a
        for i in range(n):
            a, b = b, a + b
        return a

    def fib_mock(self, n: int) -> int:  # 29.11% 1.00%
        cache = {
            0: 0,
            1: 1
        }
        if n < 2:
            return cache[n]
        i = 2
        while i <= n:
            cache[i] = cache[i-1] + cache[i-2]
            i += 1
        return cache[i-1]
