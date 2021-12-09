#  slow 9.3%
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:  # 31.86% 00.00%
        nums.sort()
        summ = 0
        for i in range(0, len(nums), 2):
            summ += min(nums[i], nums[i+1])
        return summ

    def arrayPairSum_short(self, nums: List[int]) -> int:  # 95.20% 90.82%
        nums.sort()
        return sum(nums[::2])

    def arrayPairSum_mock(self, nums: List[int]) -> int:  # 54.28% 70.60%
        nums.sort()
        out = 0
        for i in range(0, len(nums), 2):
            out += nums[i]
        return out
