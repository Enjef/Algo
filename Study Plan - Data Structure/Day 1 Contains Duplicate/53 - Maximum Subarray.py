class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = cur = float('-inf')
        for num in nums:
            cur = max(num, cur + num)
            out = max(out, cur)
        return out
