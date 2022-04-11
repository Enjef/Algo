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

    def findMin_linear(self, nums: List[int]) -> int:  # 98.15% 96.34%
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return

    def findMin_best_speed(self, lis: List[int]) -> int:
        lo = 0
        hi = len(lis) - 1
        while lo <= hi:
            mid = (lo + hi)//2
            if mid >= 0 and lis[mid] < lis[mid-1]:
                return lis[mid]
            elif lis[mid] < lis[hi]:
                hi = mid - 1
            else:
                lo = mid + 1
        return lis[0]
