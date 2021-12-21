class Solution:
    def rob_dp(self, nums: List[int]) -> int:  # 72.53% 98.76%
        dp = [0, 0]
        for num in nums:
            dp[0], dp[1] = dp[1], max(dp[1], dp[0]+num)
        return max(dp)

    def rob_v2(self, nums: List[int]) -> int:  # 86.87% 19.92%
        robbery, skip = 0, 0
        for num in nums:
            robbery, skip = max(skip+num, robbery), robbery
        return robbery
