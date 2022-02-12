class Solution:
    def findFinalValue(self, nums, original: int) -> int: # 78.55% 69.33%
        nums = set(nums)
        while original in nums:
            original *= 2
        return original
