class Solution:
    def rob(self, nums: List[int]) -> int:  # 99.35% 79.96%
        def helper(nums, left, right):
            first = second = 0
            for i in range(left, right):
                first, second = second+nums[i], max(first, second)
            return max(first, second)
        return (
            nums[0] if len(nums) == 1 else
            max(helper(nums, 1, len(nums)), helper(nums, 0, len(nums)-1))
        )
