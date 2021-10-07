class Solution:
    def rob(self, nums: List[int]) -> int:  # 72.53% 19.27%
        memo = {}

        def rec(i):
            if i < 0:
                return 0
            if i not in memo:
                memo[i] = max(rec(i-1), nums[i]+rec(i-2))
            return memo[i]
        return rec(len(nums)-1)

    def rob_dp(self, nums: List[int]) -> int:  # 72.53% 98.76%
        dp = [0, 0]
        for num in nums:
            dp[0], dp[1] = dp[1], max(dp[1], dp[0]+num)
        return max(dp)

    def rob_best_speed(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n <= 2:
            return max(nums[0], nums[1])
        twoDown = nums[0]
        oneDown = max(twoDown, nums[1])
        for i in range(2, n):
            tmp = max(twoDown + nums[i], oneDown)
            twoDown = oneDown
            oneDown = tmp
        return oneDown
