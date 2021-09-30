class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:  # 59.91% 93.25%
        if not nums:
            return 0
        n = len(nums)
        max_size, dp, cnt = 0, [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j]+1:
                        dp[i], cnt[i] = dp[j]+1, cnt[j]
                    elif dp[i] == dp[j]+1:
                        cnt[i] += cnt[j]
            max_size = max(max_size, dp[i])
        return sum(count for size, count in zip(dp, cnt) if size == max_size)
