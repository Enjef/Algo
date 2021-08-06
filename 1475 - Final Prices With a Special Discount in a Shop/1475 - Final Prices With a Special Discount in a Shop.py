class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:  # 88.93% 53.56%
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] = prices[i]-prices[j]
                    break
        return prices

    def finalPrices_best(self, prices: List[int]) -> List[int]:
        stack = list()
        for i in range(0, len(prices)):
            price = prices[i]
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(i)
        return prices
