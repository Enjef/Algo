class Solution:
    def maxProfit(self, prices: List[int]) -> int:  # 16.28% 66.53%
        hold = float('-inf')
        sell = 0
        cooldown = 0
        for price in prices:
            hold = max(hold, cooldown-price)
            cooldown = max(cooldown, sell)
            sell = max(sell, hold+price)
        return sell
