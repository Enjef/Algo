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
