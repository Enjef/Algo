class Solution:
    def largestSumAfterKNegations_my(self, nums, k):  # 27.18% memory 82.77%
        for _ in range(k):
            nums[nums.index(min(nums))] *= -1
        return sum(nums)
