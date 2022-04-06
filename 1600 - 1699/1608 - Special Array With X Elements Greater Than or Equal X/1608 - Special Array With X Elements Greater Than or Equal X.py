class Solution:
    def specialArray(self, nums: List[int]) -> int:  # 24.51% 18.68%
        nums.sort()
        for i in range(1, max(nums)+1):
            if i == len([el for el in nums if el >= i]):
                return i
        return -1

    def specialArray_bin_search_study_plan(self, nums):  # 14.08-60.51%% 67.28%
        nums.sort()
        n = len(nums)
        for i in range(n+1):
            left = 0
            right = n-1
            while left <= right:
                mid = left + (right-left)//2
                if i > nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            if i == n-left:
                return i
        return -1

    def specialArray_best_speed(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if i + 1 > nums[i]:
                return i if i and nums[i] != i else -1
        return len(nums)

    def specialArray_2nd_best_speed(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if len(nums)-m <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        if l != 0:
            return len(nums)-l if l != len(nums) and nums[l-1] != len(nums)-l else -1
        else:
            return len(nums)-l

    def specialArray_best_memory(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] >= len(nums):
            return len(nums)
        for i in range(1, len(nums)):
            count = 0
            for n in nums:
                if n >= i:
                    count += 1
            if count == i:
                return i
        return -1
