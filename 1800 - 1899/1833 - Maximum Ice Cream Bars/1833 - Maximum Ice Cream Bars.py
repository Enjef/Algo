class Solution:
    def maxIceCream(self, costs, coins):  # 64.72% 60.48%
        costs.sort()
        i = 0
        res = 0
        while i < len(costs) and coins >= costs[i]:
            coins -= costs[i]
            res += 1
            i += 1
        return res

    def maxIceCream_best_speed(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        n = 0
        while costs and costs[0] <= coins:
            n += 1
            coins -= heapq.heappop(costs)
        return n

    def maxIceCream_2nd_best_speed(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0
        for i, c in enumerate(costs):
            total += c
            if total > coins:
                return i
        return len(costs)

    def maxIceCream_best_memory(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        res = 0
        while coins > 0 and costs:
            cost = heapq.heappop(costs)
            if coins-cost >= 0:
                coins -= cost
                res += 1
        return res
