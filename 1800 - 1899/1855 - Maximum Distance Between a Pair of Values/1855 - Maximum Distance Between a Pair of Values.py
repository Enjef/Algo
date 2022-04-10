class Solution:
    def maxDistance(self, nums1, nums2):  # 26.91% 57.18%
        dist = 0
        for i in range(len(nums1)):
            left, right = i+1, len(nums2) - 1
            while left < right:
                mid = left + (right-left+1)//2
                if nums2[mid] >= nums1[i]:
                    left = mid
                else:
                    right = mid - 1
            if nums1[i] > nums2[right]:
                right = i
            dist = max(dist, right-i)
        return dist

    def maxDistance_v2(self, nums1, nums2) -> int:  # 81.84% 77.13%
        res = 0
        n, m = len(nums1), len(nums2)
        i = j = 0
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                res = max(res, j-i)
                j += 1
            else:
                i += 1
                j += 1
        return res

    def maxDistance_best_speed(self, nums1: List[int], nums2: List[int]):
        left = 0
        right = 0
        limit = len(nums1)
        for right in range(len(nums2)):
            if left == limit:
                break
            if nums1[left] > nums2[right]:
                left += 1
        return max(right - left, 0)

    def maxDistance_best_memory(self, nums1: List[int], nums2: List[int]):
        res, j = 0, -1
        for i, a in enumerate(nums1):
            while j + 1 < len(nums2) and a <= nums2[j + 1]:
                j += 1
            res = max(res, j - i)
        return res
