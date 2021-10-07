class Solution:
    def rob_dp(self, nums: List[int]) -> int:  # 72.53% 98.76%
        dp = [0, 0]
        for num in nums:
            dp[0], dp[1] = dp[1], max(dp[1], dp[0]+num)
        return max(dp)
