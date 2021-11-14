class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  # 93.32% 89.67%
        out = cur = float('-inf')
        for num in nums:
            cur = max(num, cur + num)
            out = max(out, cur)
        return out

    def maxSubArray_v_2(self, nums: List[int]) -> int:  # 52.16% 62.31%
        cur = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur+nums[i])
            res = max(res, cur)
        return res
