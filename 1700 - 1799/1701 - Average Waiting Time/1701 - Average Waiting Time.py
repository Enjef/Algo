class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:  # 31.94% 48.67%
        total = 0
        cur = 0
        for start, wait in customers:
            cur = max(cur, start) + wait
            total += cur - start
        return total / len(customers)

    def averageWaitingTime_best_speed(self, customers: List[List[int]]) -> float:
        free = 0
        total = 0
        for a, t in customers:
            free = max(free, a)
            total += free + t - a
            free += t
        return total / len(customers)
