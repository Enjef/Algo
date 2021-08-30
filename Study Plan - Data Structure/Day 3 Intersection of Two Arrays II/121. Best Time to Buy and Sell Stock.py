class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_min = 10 ** 4 + 1
        profit_max = 0
        for price in prices:
            profit_max = max(profit_max, price - price_min)
            price_min = min(price_min, price)
        return profit_max
