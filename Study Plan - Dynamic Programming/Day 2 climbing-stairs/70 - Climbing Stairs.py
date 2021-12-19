class Solution:
    def climbStairs(self, n: int) -> int:  # 60.44% 71.70%
        fib = [1, 2]
        if n == 1:
            return fib[0]
        if n == 2:
            return fib[1]
        while n - 2 > 0:
            fib[0], fib[1] = fib[1], fib[0] + fib[1]
            n -= 1
        return fib[1]

    def climbStairs_dp(self, n: int) -> int:  # 83.26% 90.44%
        dp = [1, 1]
        while n:
            n -= 1
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[0]

    def climbStairs_v3(self, n: int) -> int:  # 94.81% 44.46%
        a = b = 1
        while n:
            n -= 1
            a, b = a + b, a
        return b
