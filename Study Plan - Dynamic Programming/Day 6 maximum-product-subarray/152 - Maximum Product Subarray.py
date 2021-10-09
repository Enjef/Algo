class Solution:
    def maxProduct(self, nums: List[int]) -> int:  # 48.00% 36.19%
        total_max = cur_max = nums[0]
        total_min = cur_min = nums[0]
        for i in range(1, len(nums)):
            cur_max, cur_min = (
                max(nums[i], cur_max*nums[i], cur_min*nums[i]),
                min(nums[i], cur_min*nums[i], cur_max*nums[i])
            )
            total_max = max(total_max, cur_max, cur_min)
            total_min = min(total_min, cur_min, cur_max)
        return max(total_max, total_min)
