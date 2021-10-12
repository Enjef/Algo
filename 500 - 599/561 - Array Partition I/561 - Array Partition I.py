#  slow 9.3%
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        summ = 0
        for i in range(0, len(nums), 2):
            summ += min(nums[i], nums[i+1])
        return summ

    def arrayPairSum_short(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
