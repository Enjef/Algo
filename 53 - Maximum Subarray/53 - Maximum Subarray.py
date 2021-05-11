class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)
           
        return max_sum


x = Solution()
print(x.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]))
