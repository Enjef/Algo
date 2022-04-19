class Solution:
    def minAbsoluteSumDiff(self, nums1, nums2):  # 57.84% 14.18%
        candidates = sorted(set(nums1))
        total = 0
        max_shift = 0
        for first, second in zip(nums1, nums2):
            total += abs(first-second)
            left, right = 0, len(candidates)-1
            while left < right:
                mid = left + (right-left)//2
                if candidates[mid] < second:
                    left = mid + 1
                else:
                    right = mid
            if left < len(candidates):
                max_shift = max(
                    max_shift, abs(first-second)-abs(candidates[left]-second))
            if left > 0:
                max_shift = max(
                    max_shift, abs(first-second)-abs(candidates[left-1]-second))
        return (total-max_shift) % (10**9+7)
