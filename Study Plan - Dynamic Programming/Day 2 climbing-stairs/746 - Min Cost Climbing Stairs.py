class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        out = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            out[0], out[1] = out[1], min(out[0] + cost[i], out[1] + cost[i])
        return min(out)
