class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:  # 12.37% 59.82%
        count = [0]*10001
        for num in nums:
            count[num] += num
        dp = [0, 0]
        for num in count:
            dp[0], dp[1] = max(dp[0], dp[1]+num), dp[0]
        return dp[0]
