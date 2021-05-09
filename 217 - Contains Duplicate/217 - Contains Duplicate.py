class Solution:
    def containsDuplicate_my(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True

    def containsDuplicate_short(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
