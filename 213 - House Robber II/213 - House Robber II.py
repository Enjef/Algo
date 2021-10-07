class Solution:
    def rob(self, nums: List[int]) -> int:  # 72.35% 23.74%
        if len(nums) < 3:
            return max(nums)
        def simple_rob(left, right):
            dp = [0, 0]
            for i in range(left, right):
                dp[0], dp[1] = dp[1], max(dp[1], dp[0]+nums[i])
            return max(dp)
        return max(simple_rob(0, len(nums)-1), simple_rob(1, len(nums)))
