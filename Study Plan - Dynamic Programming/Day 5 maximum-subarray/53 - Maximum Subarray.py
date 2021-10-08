class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  # 63.58%  44.12%
        max_sub = float('-inf')
        cur_sub = float('-inf')
        for num in nums:
            cur_sub = max(cur_sub + num, num)
            max_sub = max(max_sub, cur_sub)
        return max_sub

    def maxSubArray_dp(self, nums: List[int]) -> int:  # 12.46% 22.12%
        dp = [-10001]*3
        for num in nums:
            dp[0], dp[1] = dp[1], max(num, dp[1]+num)
            if dp[1] > dp[2]:
                dp[2] = dp[1]
        return dp[2]
