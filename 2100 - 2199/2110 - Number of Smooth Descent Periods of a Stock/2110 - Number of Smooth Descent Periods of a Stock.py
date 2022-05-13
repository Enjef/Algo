class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:  # 73.62% 8.79%
        n = len(prices)
        total = 1
        cur = 1
        for i in range(1, n):
            if prices[i-1] - prices[i] == 1:
                cur += 1
            else:
                cur = 1
            total += cur
        return total

    def getDescentPeriods_best_speed(self, prices: List[int]) -> int:
        res = 0
        t = 1
        prev = prices[0]
        for i, n in enumerate(prices[1:]):
            if n == prev - 1:
                t += 1
            else:
                res += (t * (t + 1)) // 2
                t = 1
            prev = n
        res += (t * (t + 1)) // 2
        return res

    def getDescentPeriods_2nd_best_speed(self, prices: List[int]) -> int:
        previous = float('-inf')
        cnt = 0
        res = 0
        for price in prices:
            if previous - price == 1:
                cnt += 1
            else:
                cnt = 1
            res += cnt
            previous = price
        return res

    def getDescentPeriods_best_memory(self, prices: List[int]) -> int:
        res = len(prices)
        curr = 0
        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                curr += 1
                res += curr
            else:
                curr = 0
        return res
