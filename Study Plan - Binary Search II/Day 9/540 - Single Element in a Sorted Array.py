class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:  # 62.17% 13.20%
        left, right = 0, len(nums)-1
        n = len(nums)
        while left <= right:
            mid = left + (right-left) // 2
            if mid > 0 and nums[mid] == nums[mid-1]:
                if mid % 2:
                    left = mid + 1
                else:
                    right = mid - 2
            elif mid < n-1 and nums[mid] == nums[mid+1]:
                if mid % 2:
                    right = mid - 1
                else:
                    left = mid + 2
            else:
                return nums[mid]
        return nums[left]

    def singleNonDuplicate_best_memory(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r-l)//2
            if m % 2:
                m -= 1
            if nums[m] == nums[m+1]:
                l = m + 2
            else:
                r = m
        return nums[l]
