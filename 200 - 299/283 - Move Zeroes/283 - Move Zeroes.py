class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        i = j = 0
        while j < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                j += 1
                continue
            i += 1
            j += 1
