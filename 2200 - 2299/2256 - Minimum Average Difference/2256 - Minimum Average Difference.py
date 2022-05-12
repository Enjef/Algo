class Solution:
    # 65.18% 75.06%
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        left = 0
        right = total
        min_val = float('inf')
        min_idx = 0
        for i, num in enumerate(nums):
            left += num
            right -= num
            diff = abs(left//(i+1)-(right//(n-i-1) if n-i-1 else 0))
            if diff < min_val:
                min_val = diff
                min_idx = i
        return min_idx

    def minimumAverageDifference_best_speed(self, nums: List[int]) -> int:
        suffix = sum(nums)
        mad = inf
        ans = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            suffix -= nums[i]
            left = prefix//(i+1)
            if i+1 < len(nums):
                right = suffix//(len(nums)-i-1)
            else:
                right = 0
            if abs(left-right) < mad:
                mad = abs(left-right)
                ans = i
        return ans

    def minimumAverageDifference_2nd_best_speed(self, nums: List[int]) -> int:
        left = np.cumsum(nums)
        right = sum(nums) - left
        n = len(nums)
        i = np.arange(1, n+1)
        j = n - i
        return np.argmin(np.abs(left//i - right//j))

    def minimumAverageDifference_best_memory(self, nums: List[int]) -> int:
        res, N, total, s, resv = math.inf, len(nums), sum(nums), 0, 0
        for i, v in enumerate(nums):
            s += v
            tmp = abs(
                s // (i + 1) - ((total - s) // (N - i - 1) if i < N - 1 else 0)
            )
            if tmp < res:
                res = tmp
                resv = i
        return resv
