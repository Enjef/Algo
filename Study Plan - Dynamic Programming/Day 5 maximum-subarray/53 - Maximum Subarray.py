class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = float('-inf')
        cur_sub = float('-inf')
        for num in nums:
            cur_sub = max(cur_sub + num, num)
            max_sub = max(max_sub, cur_sub)
        return max_sub
