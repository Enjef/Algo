class Solution:
    def nextPermutation(self, nums: List[int]) -> None:  # 98.81% 28.25%
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        j = n-2
        while j > -1 and nums[j] >= nums[j+1]:
            j -= 1
        if j == -1:
            nums[:] = nums[::-1]
            return
        i = n-1
        while i > j and nums[j] >= nums[i]:
            i -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[j+1:] = sorted(nums[j+1:])
        return

    def nextPermutation_best_speed(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tail1 = tail2 = len(nums) - 1
        while nums[tail1] <= nums[tail1-1] and tail1 > 0:
            tail1 -= 1
        if tail1 == 0:
            return nums.reverse()
        swap = tail1 - 1
        while nums[tail2] <= nums[swap]:
            tail2 -= 1
        nums[swap], nums[tail2] = nums[tail2], nums[swap]
        revStart = swap + 1
        revEnd = len(nums) - 1
        while revStart < revEnd:
            nums[revStart], nums[revEnd] = nums[revEnd], nums[revStart]
            revStart += 1
            revEnd -= 1

    def nextPermutation_best_memory(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = i
            while j < n-1 and nums[j+1] > nums[i]:
                j += 1
            nums[i], nums[j] = nums[j], nums[i]
        l, r = i+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
