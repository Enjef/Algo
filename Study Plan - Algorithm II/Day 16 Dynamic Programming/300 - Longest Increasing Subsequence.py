class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:  # 40.36% 47.31%
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    def lengthOfLIS_bin_search(self, nums: List[int]) -> int:  # 85.67% 48.48%
        sub = []
        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
            left, right = 0, len(sub)-1
            while left < right:
                mid = left + (right - left) // 2
                if sub[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            sub[left] = num
        return len(sub)
