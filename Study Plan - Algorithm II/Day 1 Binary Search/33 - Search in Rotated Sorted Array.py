class Solution:
    def search(self, nums: List[int], target: int) -> int:  # 55.65% 22.04%
        left_a = 0
        right_a = len(nums) - 1

        def checker(arr, left, right, target):
            if left > right:
                return -1
            if arr[left] < arr[right]:
                return bin_s(arr, left, right, target)
            mid_t = left + (right - left) // 2
            if arr[mid_t] == target:
                return mid_t
            return max(
                checker(nums, left, mid_t-1, target),
                checker(nums, mid_t+1, right, target)
            )

        def bin_s(arr, left, right, target):
            left = left
            right = right
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
            return -1
        return checker(nums, left_a, right_a, target)
