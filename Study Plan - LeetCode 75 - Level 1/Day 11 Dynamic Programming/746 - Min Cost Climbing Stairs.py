class Solution:
    # 5.01% 97.21%
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0
        for price in cost:
            first, second = min(first, second)+price, first
        return min(first, second)
