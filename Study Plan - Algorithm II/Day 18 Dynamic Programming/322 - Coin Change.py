class Solution:
    def coinChange(
            self,
            coins: List[int],
            amount: int) -> int:  # 70.30% 64.30%
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i-c] + 1)

        if dp[amount] == amount+1:
            return -1
        return dp[amount]
