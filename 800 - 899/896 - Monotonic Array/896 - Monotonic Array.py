class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:  # 24.13% 27.56%
        if len(nums) < 3:
            return True
        return (
            True if nums == sorted(nums) or
            nums == sorted(nums, reverse=True) else False
        )

    def isMonotonic_variation(self, nums: List[int]) -> bool:  # 14.82% 49.20%
        if len(nums) < 3:
            return True
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)

    def isMonotonic_lines(self, nums: List[int]) -> bool:  # 42.53% 5.52%
        if len(nums) < 3:
            return True
        i = 0
        while i <= len(nums)-2 and nums[i] == nums[i + 1]:
            i += 1
            continue
        if i == len(nums)-1:
            return True
        up = False
        if nums[i] < nums[i+1]:
            up = True
        while i <= len(nums)-2:
            if up and nums[i] > nums[i+1]:
                return False
            if not up and nums[i] < nums[i+1]:
                return False
            i += 1
        return True
