class Solution:
    def search(self, nums: List[int], target: int) -> int:  # 6.07% 69.47%
        if nums[0] == target:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def search_rec(self, nums: List[int], target: int) -> int:  # 38.39% 28.09%
        def rec(left, right):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return rec(left, mid - 1)
            else:
                return rec(mid + 1, right)
        return rec(0, len(nums)-1)
