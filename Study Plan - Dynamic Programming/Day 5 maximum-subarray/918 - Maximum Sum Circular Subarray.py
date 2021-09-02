class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sum_max = cur_max = float('-inf')
        cur_min = sum_min = float('inf')
        all_negative = True
        for num in nums:
            if num > 0:
                all_negative = False
                break
        if all_negative:
            return max(nums)
        total = sum(nums)
        for num in nums:
            cur_min = min(cur_min + num, num)
            sum_min = min(sum_min, cur_min)
            cur_max = max(cur_max + num, num)
            sum_max = max(sum_max, cur_max)
        if sum_min < 0:
            total -= sum_min
        return max(total, sum_max)
