class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:  # 74.00% 31.75%
        return len(nums) != len(set(nums))
