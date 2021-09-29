class Solution:
    def numberOfArithmeticSlices(
            self,
            nums: List[int]) -> int:  #  83.22% 44.05%
        if len(nums) < 3:
            return 0
        combo = False
        count = 0
        for i in range(len(nums)-2):
            if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
                count += 1 + combo * i
                combo = True
            else:
                combo = False
        return count
