class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:  # 84.07% 64.08%
        return len(set(nums)) != len(nums)
