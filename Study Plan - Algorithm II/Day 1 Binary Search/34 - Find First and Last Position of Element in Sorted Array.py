class Solution:
    def searchRange(
            self,
            nums: List[int],
            target: int) -> List[int]:  # 53.72% 50.91%
        out = [-1, -1]
        if not nums:
            return out
        left = 0
        right = len(nums)-1
        first = None
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                if not first:
                    first = mid
                right = mid - 1
        if first is None:
            return out
        out[0] = left
        right = len(nums)-1
        left = first
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1
        out[1] = right
        return out
