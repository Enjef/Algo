class Solution:
    def findMin(self, nums: List[int]) -> int:  # 67.10% 87.88%
        res = nums[0]
        left, right = 0, len(nums) - 1
        while right > left:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                res = min(res, nums[right])
                left = mid + 1
            elif nums[right] > nums[mid]:
                right = mid
            else:
                right -= 1
        res = min(res, nums[left])
        return res

    def findMin_best_speed(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
