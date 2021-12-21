class Solution:
    def rob(self, nums: List[int]) -> int:  # 72.35% 23.74%
        if len(nums) < 3:
            return max(nums)

        def simple_rob(left, right):
            dp = [0, 0]
            for i in range(left, right):
                dp[0], dp[1] = dp[1], max(dp[1], dp[0]+nums[i])
            return max(dp)
        return max(simple_rob(0, len(nums)-1), simple_rob(1, len(nums)))

    def rob_best_speed(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        cash1 = [0] * len(nums)
        cash2 = [0] * len(nums)
        cash1[0] = cash1[1] = nums[0]
        cash2[0] = 0
        cash2[1] = nums[1]
        for i in range(2, len(nums)):
            cash1[i] = max(cash1[i-2]+nums[i], cash1[i-1])
            cash2[i] = max(cash2[i-2]+nums[i], cash2[i-1])
        return max(cash1[-2], cash2[-1])

    def rob_best_memory(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev_1, current_1, prev_2, current_2 = 0, 0, 0, 0
        for i, house_1 in enumerate(nums[:-1]):
            temp_1 = max(house_1 + prev_1, current_1)
            prev_1 = current_1
            current_1 = temp_1
            house_2 = nums[i + 1]
            temp_2 = max(house_2 + prev_2, current_2)
            prev_2 = current_2
            current_2 = temp_2
        return max(current_1, current_2)
