class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:  # 57.37% 41.14%
        n = len(costs)
        costs.sort(key=lambda x: x[0]-x[1])
        return sum([x[0] if i < n//2 else x[1] for i, x in enumerate(costs)])

    def twoCitySchedCost_best_speed(self, costs: List[List[int]]) -> int:
        test = [(abs(x[0] - x[1]), x) for x in costs]
        test.sort(reverse=True)
        maxi = len(costs)/2
        a = 0
        b = 0
        total = 0
        for diff, cost in test:
            if cost[0] < cost[1]:
                if a >= maxi:
                    total += cost[1]
                    b += 1
                else:
                    total += cost[0]
                    a += 1
            else:
                if b >= maxi:
                    total += cost[0]
                    a += 1
                else:
                    total += cost[1]
                    b += 1
        return total

    def twoCitySchedCost_2nd_best_speed(self, costs: List[List[int]]) -> int:
        costs = [[c[0]-c[1]]+c for c in costs]
        costs = sorted(costs, key=lambda x: x[0])
        n = len(costs)//2
        ans = sum([c[1] for c in costs[:n]]) + sum([c[2] for c in costs[n:]])
        return ans

    def twoCitySchedCost_best_memory(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs_diff = [ca - cb for ca, cb in costs]
        idx = sorted(range(len(costs_diff)), key=lambda x: costs_diff[x])
        total_cost_a = sum([costs[i][0] for i in idx[:n]])
        total_cost_b = sum([costs[i][1] for i in idx[n:]])
        return total_cost_a + total_cost_b
