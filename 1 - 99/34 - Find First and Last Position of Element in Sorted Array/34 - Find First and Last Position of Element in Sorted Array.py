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

    def searchRange_best_speed(self, nums, target):
        if nums == None or len(nums) == 0:
            return [-1, -1]
        def find(arr, target):
            low, high = 0, len(arr)-1
            while low <= high:
                mid = low + (high-low)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
        
        if not find(nums, target):
            return [-1, -1]
        left  = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return [left, right-1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def binary_search(arr, target):
            left = 0 
            right = len(arr) - 1
            while left < right:
                mid = left + (right - left) // 2
                if target > arr[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        idx = binary_search(nums,target)
        if nums[idx] != target:
            return [-1, -1]
        right = left = idx
        while left > 0:
            if nums[left - 1] == target:
                left -= 1
            else:
                break
        while right < len(nums) - 1:
            if nums[right + 1] == target:
                right += 1
            else:
                break
        return [left, right]
