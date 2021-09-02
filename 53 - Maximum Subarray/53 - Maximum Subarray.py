class Solution:
    def maxSubArray(self, nums):  # 67.92% 86.72%
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum

    def maxSubArray_best_speed(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = cur_max = 0
        for num in nums:
            cur_max += num
            if cur_max > res:
                res = cur_max
            if cur_max < 0:
                cur_max = 0
                continue
        return res if res > 0 else max(nums)
