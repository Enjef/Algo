class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:  # 48.97% 57.15%
        buy = float('-inf')
        sell = 0
        for price in prices:
            buy = max(buy, sell-price)
            sell = max(sell, buy+price-fee)
        return sell

    def maxProfit_from_second(
            self,
            prices: List[int],
            fee: int) -> int:  # 58.51% 37.16%
        buy = -prices[0]
        sell = 0
        for i in range(1, len(prices)):
            buy = max(buy, sell-prices[i])
            sell = max(sell, buy+prices[i]-fee)
        return sell
