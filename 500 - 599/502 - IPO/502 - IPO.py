class Solution:
    # 57.37% 19.41% (60.49% 17.50%)
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pool = sorted([(-prof, cap) for prof, cap in zip(profits, capital)], key=lambda x: x[1], reverse=True)
        projects = []
        while k > 0:
            while pool and pool[-1][1] <= w:
                heappush(projects, pool.pop())
            if not projects:
                break
            w += -heappop(projects)[0]
            k -= 1
        return w

    # 95.15% 17.50%
    def findMaximizedCapital_v2(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pool = sorted([(-prof, cap) for prof, cap in zip(profits, capital)], key=lambda x: x[1], reverse=True)
        projects = []
        while k > 0:
            while pool and pool[-1][1] <= w:
                heappush(projects, pool.pop()[0])
            if not projects:
                break
            w += -heappop(projects)
            k -= 1
        return w


class Solution_best_speed:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(nlargest(k, profits))
        c_to_p = [(c, profits[i]) for i,c in enumerate(capital)]
        heapify(c_to_p)
        valid_profits = []
        for i in range(k):
            while c_to_p and c_to_p[0][0] <= w:
                _, profit = heappop(c_to_p)
                heappush(valid_profits, -profit)
            if valid_profits:
                w += -heappop(valid_profits)
            else:
                break
        return w


class Solution_best_memory:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        while k > 0:
            if k >= len(profits) and w >= max(capital):
                return w + sum(profits)
            projects = [i for i in range(len(capital)) if capital[i] <= w]
            if not projects:
                break
            maxProfit = max([profits[p] for p in projects])
            index = [i for i in projects if profits[i] == maxProfit]
            profits.pop(index[-1])
            capital.pop(index[-1])
            w += maxProfit
            k -= 1
        return w
