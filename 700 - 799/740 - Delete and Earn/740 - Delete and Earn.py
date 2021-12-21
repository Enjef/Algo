class Solution:
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

    def deleteAndEarn_best_speed(self, nums: List[int]) -> int:
        counts = [0] * (max(nums) + 1)
        for num in nums:
            counts[num] += num
        prev, curr = 0, 0
        for elem in counts:
            prev, curr = curr, max(curr, prev + elem)
        return curr
