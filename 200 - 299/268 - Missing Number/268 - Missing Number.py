class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            else:
                return 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                return nums[i]+1
        if nums[0] == 0:
            return nums[-1]+1
        return 0
