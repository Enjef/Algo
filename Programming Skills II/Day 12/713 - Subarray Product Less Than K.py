class Solution:
    def numSubarrayProductLessThanK(self, nums, k):  # 77.46% 77.46%
        if k <2:
            return 0
        n = len(nums)
        res = 0
        cur = 1
        i = 0
        for j in range(n):
            cur *= nums[j]
            while cur >= k:
                cur /= nums[i]
                i += 1
            res += j - i + 1
        return res
        