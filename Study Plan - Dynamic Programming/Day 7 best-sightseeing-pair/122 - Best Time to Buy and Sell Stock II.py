class Solution:
    def maxProfit(self, prices: List[int]) -> int:  # 57.85% 98.89%
        profit = 0
        price_min = prices[0]
        for price in prices:
            profit += price - price_min if price - price_min > 0 else 0
            price_min = price
        return profit
