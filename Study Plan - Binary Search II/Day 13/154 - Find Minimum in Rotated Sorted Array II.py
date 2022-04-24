class Solution:
    def findMin(self, nums: List[int]) -> int:  # 67.10% 87.88%
        res = nums[0]
        left, right = 0, len(nums) - 1
        while right > left:
            mid = left  + (right - left) // 2
            if nums[right] < nums[mid]:
                res = min(res, nums[right])
                left = mid + 1
            elif nums[right] > nums[mid]:
                right = mid
            else:
                right -= 1
        res = min(res, nums[left])
        return res
