class Solution:

    def __init__(self, nums: List[int]):  # 91.05% 71.86%
        self.nums = nums
        self.current = nums[:]

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        import random
        random.shuffle(self.current)
        return self.current
