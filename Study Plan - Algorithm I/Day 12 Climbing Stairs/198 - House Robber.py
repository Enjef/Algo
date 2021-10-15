class Solution:
    def rob(self, nums: List[int]) -> int:  # 42.08% 92.85%
        prev = 0
        cur = nums[0]
        for i in range(1, len(nums)):
            prev, cur = cur, max(cur, prev+nums[i])
        return cur
