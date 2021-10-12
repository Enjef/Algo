class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:  # 90.81% 22.43%
        if len(cost) <= 2:
            return min(cost)
        out = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            out[0], out[1] = out[1], min(out[0] + cost[i], out[1] + cost[i])
        return min(out)

    def minCostClimbingStairs_best_speed(self, cost: List[int]) -> int:
        lengthOfStairs = len(cost)
        dp = [None] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, lengthOfStairs):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[lengthOfStairs-1], dp[lengthOfStairs-2])

    def minCostClimbingStairs_best_memory(self, cost: List[int]) -> int:
        if not cost:
            return 0
        elif len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost[0], cost[1])
        minCost = [0] * len(cost)
        minCost[0] = cost[0]
        minCost[1] = cost[1]
        for i in range(2, len(cost)):
            minCost[i] = min(minCost[i-1], minCost[i-2]) + cost[i]
        return min(minCost[-1], minCost[-2])
