class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:  # 18.55% 55.86%
        sum_set_nums = sum(set(nums))
        dubble = sum(nums) - sum_set_nums
        n = len(nums)
        sum_n = (n + 1) * n / 2
        target = int(sum_n) - sum_set_nums
        return [dubble, target]
