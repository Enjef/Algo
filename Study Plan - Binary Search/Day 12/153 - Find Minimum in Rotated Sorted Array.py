class Solution:
    def findMin(self, nums: List[int]) -> int:  # 43.34% 67.25%
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
