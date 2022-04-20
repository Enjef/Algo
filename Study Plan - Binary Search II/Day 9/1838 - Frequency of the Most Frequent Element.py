class Solution:
    def maxFrequency_best_speed(self, nums, k):  # 96.95% 94.63%
        nums.sort()
        n = len(nums)
        i = 0
        for j in range(n):
            k += nums[j]
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        window_s = window_len = 0
        best = 0
        prefix = [0] + list(accumulate(nums))
        best = 0
        for i, n in enumerate(nums):
            left = 0
            right = i
            while left < right:
                mid = (left + right) // 2
                window_s = prefix[i] - prefix[mid]
                window_len = i - mid
                if window_len * n - window_s <= k:
                    right = mid
                else:
                    left = mid + 1
            best = max(best, 1 + i - left)
        return best
