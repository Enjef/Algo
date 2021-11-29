class Solution:
    def sortColors_ds_2_day_2(self, nums: List[int]) -> None:  # 48.58% 13.35%
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        for num in nums:
            if num == 0:
                zero = zero + 1
            elif num == 1:
                one = one + 1
            else:
                two = two + 1
        nums[:] = [0] * zero + [1] * one + [2] * two
        return