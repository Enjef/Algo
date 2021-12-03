class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # 78.12% 93.49%
        if nums.count(0) > 1:
            return [0] * len(nums)
        out = [1] * len(nums)
        for i in range(1, len(nums)):
            out[i] = out[i-1] * nums[i-1]
        acc = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * acc
            acc *= nums[i]
        return out
