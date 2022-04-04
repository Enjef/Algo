class Solution:
    def searchRange(self, nums, target):  # 46.18% 94.38%
        n = len(nums)-1
        left, right = 0, n
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid 
        if not nums or nums[left] != target:
            return -1, -1
        first = left
        right = n
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return first, right
