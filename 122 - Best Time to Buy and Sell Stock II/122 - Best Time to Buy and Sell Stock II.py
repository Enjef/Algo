class Solution:
    def maxProfit(self, prices) -> int:
        price_min, price_max, profit = float('inf'), 0, 0
        for price in prices:
            if price_min == price_max == price:
                continue
            if price < price_max:
                profit += price_max - price_min
                price_min, price_max = price, 0
                continue
            if price < price_min:
                price_min = price
            if price > price_max:
                price_max = price
        if price_max - price_min > 0:
            profit += price_max - price_min

        return profit


x = Solution()
print(x.maxProfit([7,6,4,3,1]))
