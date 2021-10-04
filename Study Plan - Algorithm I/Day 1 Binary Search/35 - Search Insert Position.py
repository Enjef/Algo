class Solution:
    def searchInsert(
            self,
            nums: List[int],
            target: int) -> int:  # 25.32%  22.29%
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def searchInsert_rec(
            self,
            nums: List[int],
            target: int) -> int:  # 22.13% 22.29%
        def rec(left, right):
            mid = left + (right - left) // 2
            if left > right:
                return left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return rec(mid+1, right)
            else:
                return rec(left, mid-1)
        return rec(0, len(nums)-1)
