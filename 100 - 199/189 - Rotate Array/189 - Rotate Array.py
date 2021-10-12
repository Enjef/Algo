class Solution:
    def rotate(self, nums: List[int], k: int) -> None:  # 58.97% 83.94%
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        if k == len(nums) or k == 0:
            return
        temp = nums[-k:]
        for i in range(len(nums)-1, k-1, -1):
            nums[i] = nums[i-k]
        for i in range(len(temp)):
            nums[i] = temp[i]
        return

    def rotate_copy(self, nums: List[int], k: int) -> None:  # 58.97% 13.41%
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        if k == len(nums) or k == 0:
            return
        temp = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = temp[i]
        return

    def rotate_best_speed(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 0 or k % l == 0:
            return nums
        k = k % l
        nums[:k], nums[k:] = nums[l-k:], nums[:l-k]
        return nums

    def rotate_third_to_best(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate_fifth_to_best(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
        nums[:] = a
