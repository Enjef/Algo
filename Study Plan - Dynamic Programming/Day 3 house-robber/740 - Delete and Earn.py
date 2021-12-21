class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:  # 12.37% 59.82%
        count = [0]*10001
        for num in nums:
            count[num] += num
        dp = [0, 0]
        for num in count:
            dp[0], dp[1] = max(dp[0], dp[1]+num), dp[0]
        return dp[0]

    def deleteAndEarn_v2(self, nums: List[int]) -> int:  # 16.22% 85.51%
        def rob(arr):
            do, skip = 0, 0
            for item in arr:
                do, skip = max(skip+item, do), do
            return do
        dp = [0] * 10001
        for num in nums:
            dp[num] += num
        return rob(dp)
