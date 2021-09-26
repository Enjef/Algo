class Solution:
    def minSubArrayLen(
            self,
            target: int,
            nums: List[int]) -> int:  # 92.94% 93.57%
        sum_n = 0
        i = 0
        min_len = len(nums)+1
        for j in range(len(nums)):
            sum_n += nums[j]
            while sum_n >= target:
                min_len = min(min_len, j-i+1)
                sum_n -= nums[i]
                i += 1
        return min_len if min_len <= len(nums) else 0
