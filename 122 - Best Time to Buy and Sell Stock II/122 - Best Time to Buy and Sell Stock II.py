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

    def maxProfit_fast(self, prices: List[int]) -> int:
        profit = 0
        prev = float('inf')

        for cur in prices:
            if cur > prev:
                profit += cur - prev
            prev = cur
        return profit


x = Solution()
print(x.maxProfit([7,6,4,3,1]))
