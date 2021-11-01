class Solution:
    def maximumDifference(self, nums: List[int]) -> int:  # 86.25% 68.81%
        n_min = float('inf')
        max_diff = float('-inf')
        for i in range(1, len(nums)):
            n_min = min(n_min, nums[i-1])
            max_diff = max(max_diff, nums[i] - n_min)
        return max_diff if max_diff > 0 else -1

    def maximumDifference_best_speed(self, nums: List[int]) -> int:
        ans, mn = -1, nums[0]
        for i in nums:
            ans = max(ans, i - mn)
            mn = min(mn, i)
        return ans if ans != 0 else -1
