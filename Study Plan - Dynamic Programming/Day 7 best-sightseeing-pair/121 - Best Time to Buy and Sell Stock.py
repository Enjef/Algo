class Solution:
    def maxProfit(self, prices: List[int]) -> int:  # 43.92% 52.61%
        buy_min = prices[0]
        res = 0
        for price in prices:
            res = max(res, price - buy_min)
            buy_min = min(buy_min, price)
        return res
