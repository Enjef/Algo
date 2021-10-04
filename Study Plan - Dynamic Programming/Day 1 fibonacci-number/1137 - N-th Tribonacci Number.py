class Solution:
    def tribonacci(self, n: int) -> int:  # 6.07%  70.75%
        a = 0
        b = 1
        c = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        while n >= 3:
            a, b, c = b, c, a + b + c
            n -= 1
        return c

    def tribonacci_dp(self, n: int) -> int:  # 6.07% 70.75%
        dp = [0, 1, 1]
        for _ in range(n):
            dp[0], dp[1], dp[2] = dp[1], dp[2], dp[0] + dp[1] + dp[2]
        return dp[0]
