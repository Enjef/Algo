class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:  # 86.51% 8.48%
        diff = max(nums) - min(nums)
        if not diff or diff < k * 2:
            return 0
        else:
            return diff - k * 2

    def smallestRangeI_best_speed(self, nums: List[int], k: int) -> int:
        return max(0, (max(nums)-k)-(min(nums)+k))

    def smallestRangeI_best_memory(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        if ans <= 2 * k:
            return 0
        return ans - 2 * k
