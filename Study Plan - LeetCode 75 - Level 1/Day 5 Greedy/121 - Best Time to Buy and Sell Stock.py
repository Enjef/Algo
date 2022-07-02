class Solution:
    # 92.26% 85.42%
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for price in prices:
            profit = max(profit, price - buy)
            buy = min(buy, price)
        return profit
        