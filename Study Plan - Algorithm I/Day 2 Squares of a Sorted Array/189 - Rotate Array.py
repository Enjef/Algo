class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
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
