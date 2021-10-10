class Solution:
    def maxProfit(self, prices) -> int:  # 79.76% 65.01%
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

    def maxProfit_fast(self, prices: List[int]) -> int:
        profit = 0
        prev = float('inf')

        for cur in prices:
            if cur > prev:
                profit += cur - prev
            prev = cur
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:  # 57.85% 98.89%
        profit = 0
        price_min = prices[0]
        for price in prices:
            profit += price - price_min if price - price_min > 0 else 0
            price_min = price
        return profit
