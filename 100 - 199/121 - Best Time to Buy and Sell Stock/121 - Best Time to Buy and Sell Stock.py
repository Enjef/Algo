class Solution:
    def maxProfit(self, prices) -> int:
        min_price, max_profit = float('inf'), 0
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)
        return max_profit


x = Solution()
print(x.maxProfit([7, 1, 5, 3, 6, 4]))
