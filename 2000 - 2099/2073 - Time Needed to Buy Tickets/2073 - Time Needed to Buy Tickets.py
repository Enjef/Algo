class Solution:
    def timeRequiredToBuy(
            self, tickets: List[int], k: int) -> int: # 75.22% 100.00%
        res = 0
        target = tickets[k]
        for qty in tickets[:k+1]:
            res += min(qty, target)
        for qty in tickets[k+1:]:
            res += min(qty, target-1)
        return res

    def timeRequiredToBuy_best_speed(self, tickets: List[int], k: int) -> int:
        return (
            sum(min(t, tickets[k]) for t in tickets[:k + 1]) +
            sum(min(t, tickets[k] - 1) for t in tickets[k + 1:])
        )
