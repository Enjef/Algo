class Solution:
    def fib(self, n: int) -> int:  # 99.94% 39.99%
        if n == 0:
            return 0
        if n == 1:
            return 1
        fib_l = [0, 1]
        if n < 2:
            return fib_l[n-1]
        while n > 2:
            fib_l = [fib_l[1], fib_l[0] + fib_l[1]]
            n -= 1
        return sum(fib_l)

    def fib_dp(self, n: int) -> int:  # 33.64% 39.99%
        dp = [0, 1]
        while n:
            n -= 1
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[0]

    def fib_v3(self, n: int) -> int:  # 85.12% 70.93%
        a = 0
        b = 1
        for _ in range(n):
            a, b = a + b, a
        return a
