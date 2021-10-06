class Solution:
    def moveZeroes_count_zeroes(
            self,
            nums: List[int]) -> None:  # 87.50 % 88.31%
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        for i in range(count, len(nums)):
            nums[i] = 0
        return

    def moveZeroes_(self, nums: List[int]) -> None:  # 20.65% 23.19%
        i = j = 0
        while i < len(nums) and j < len(nums):
            if i < j and nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                continue
            elif nums[i] != 0 and i < j:
                i += 1
            elif nums[j] == 0:
                j += 1
            else:
                i += 1
                j += 1
        return
