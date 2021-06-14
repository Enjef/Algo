class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max_s = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                max_s = max(max_s, cur)
                cur = 0
            cur += nums[i]
        return max(max_s, cur)
