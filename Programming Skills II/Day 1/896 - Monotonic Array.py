class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:  # 72.02% 75.34%
        n = len(nums)
        if n < 2:
            return True
        if nums[0] > nums[-1]:
            for i in range(1, n):
                if nums[i-1] < nums[i]:
                    return False
            else:
                return True
        else:
            for i in range(1, n):
                if nums[i-1] > nums[i]:
                    return False
            else:
                return True
