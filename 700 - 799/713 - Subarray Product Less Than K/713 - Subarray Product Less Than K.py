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

    def numSubarrayProductLessThanK_best_memory(self, nums, k):
        subsum = 1
        count = 0
        target = k
        i = - 1
        for j, num in enumerate(nums):
            if num >= target:
                i = -1
            elif i == -1:
                subsum = num
                i = j 
            else:
                subsum *= num
                while subsum >= target and i < j:
                    subsum /= nums[i]
                    i += 1
            count += (j - i + 1) if i != -1 else 0
        return count
