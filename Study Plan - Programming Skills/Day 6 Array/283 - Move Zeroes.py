class Solution:
    def moveZeroes(self, nums: List[int]) -> None:  # 5.00% 16.13%
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums
        i, j = 0, 0
        while i < n or j < n:
            while j < n and nums[j] != 0:
                j += 1
            i = j
            while i < n and nums[i] == 0:
                i += 1
            if i == n or j == n:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        return

    def moveZeroes_slice_assignment(self, nums): # 62.62% 16.13%
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        zeros = nums.count(0)
        for num in nums:
            if num:
                res.append(num)
        nums[:] = res + [0]*zeros
        return
