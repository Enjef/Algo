class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:  # 58.78% 49.32%
        return abs(goal-sum(nums)) // limit + bool(abs(goal-sum(nums)) % limit)

    def minElements_best_peed(self, nums: List[int], limit: int, goal: int) -> int:
        curr = sum(nums)
        if curr >= goal:
            addtl = curr-goal
        else:
            addtl = goal-curr
        return addtl//limit + 1 if addtl % limit else addtl//limit

    def minElements_best_memory(self, nums: List[int], limit: int, goal: int) -> int:
        s = 0
        for i in nums:
            s += i
        x = abs(goal-s)
        result = x/limit
        return math.ceil(result)
