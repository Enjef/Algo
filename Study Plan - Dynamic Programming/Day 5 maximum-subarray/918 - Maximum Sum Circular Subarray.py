class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:  # 13.75% 79.18%
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

    def maxSubarraySumCircular_dp(
            self,
            nums: List[int]) -> int:  # 54.32% 52.02%
        total = sum(nums)
        dp_min = [3*10**4+1] * 2
        dp_max = [-3*10**4-1] * 2
        all_negative = True
        for num in nums:
            if num > 0:
                all_negative = False
            dp_min[0] = min(num, num+dp_min[0])
            dp_min[1] = min(dp_min[1], dp_min[0])
            dp_max[0] = max(num, num+dp_max[0])
            dp_max[1] = max(dp_max[1], dp_max[0])
        if all_negative:
            return max(nums)
        if dp_min[1] < 0:
            total -= dp_min[1]
        return max(total, dp_max[1])
