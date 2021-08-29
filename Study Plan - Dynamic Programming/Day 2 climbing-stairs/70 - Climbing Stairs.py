class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1, 2]
        if n == 1:
            return fib[0]
        if n == 2:
            return fib[1]
        while n - 2 > 0:
            fib[0], fib[1] = fib[1], fib[0] + fib[1]
            n -= 1
        return fib[1]
