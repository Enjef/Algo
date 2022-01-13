class Solution:
    def search(self, nums: List[int], target: int) -> int:  # 7.43% 56.19%
        def bin_search(l, r):
            while l <= r:
                m = l + (r-l) // 2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
                
        out = -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                out = bin_search(left, mid-1)
                left = mid + 1
            else:
                out = bin_search(mid+1, right)
                right = mid - 1
            if out != -1:
                return out
        return out

    def recursiveBinarySearch(self, nums, target):
        high = len(nums) - 1
        if (high < 0):
            return -1
        
        mid = high // 2
        if (nums[mid] == target):
            return nums.index(target)
        elif (nums[mid] < target):
            return self.recursiveBinarySearch(nums[mid + 1:], target)
        else:
            return self.recursiveBinarySearch(nums[:mid], target)
                
    def search_1st_speed(self, nums: List[int], target: int) -> int:        
        try:
            pivot = nums.index(target)
        except ValueError:
            return -1
        firstHalf  = nums[:pivot]
        secondHalf = nums[pivot + 1:]
        if (target == nums[pivot]):
            return pivot
        elif (target in firstHalf):
            return self.recursiveBinarySearch(firstHalf, target)
        else:
            return self.recursiveBinarySearch(secondHalf, target)

    def search_2nd_best_speed(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
