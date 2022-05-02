class Solution:
    def minimumCost(self, cost: List[int]) -> int:  # 77.41% 57.86%
        cost.sort()
        res = 0
        while cost:
            res += cost.pop()
            if cost:
                res += cost.pop()
            if cost:
                cost.pop()
        return res

    def minimumCost_best_speed(self, cost: List[int]) -> int:
        cost = sorted(cost)[::-1]
        ans = 0
        for i, c in enumerate(cost):
            if (i+1) % 3 != 0:
                ans += c
        return ans

    def minimumCost_best_memory(self, cost: List[int]) -> int:
        cost.sort()
        pos = len(cost)
        if pos < 2:
            return sum(cost)
        max_cost = 0
        while pos >= 0:
            max_cost += sum(cost[pos-2:pos]) if pos > 1 else sum(cost[:pos])
            pos -= 3
        return max_cost
