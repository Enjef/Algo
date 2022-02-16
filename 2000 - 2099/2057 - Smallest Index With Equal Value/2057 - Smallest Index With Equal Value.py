class Solution:
    def smallestEqual(self, nums: List[int]) -> int: # 34.18% 98.78%
        for i in range(len(nums)):
            if i%10 == nums[i]:
                return i
        return -1

    def smallestEqual_best_speed(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            if (i % 10 == x):
                return i
        return -1
