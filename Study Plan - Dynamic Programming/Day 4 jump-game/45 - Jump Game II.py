class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_jump = 0
        max_jump = 0
        count = 0
        for i in range(len(nums)-1):
            if nums[i] + i > max_jump:
                max_jump = nums[i] + i
            if i == cur_jump:
                cur_jump = max_jump
                count += 1
        return count

    def jump_dp(self, nums: List[int]) -> int:  # 95.81% 97.51%
        if len(nums) == 1:
            return 0
        count = 0
        cur = 0
        dp = [0] * len(nums)
        for i in range(len(nums)-1):
            if dp[i-1]-1 < nums[i]:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1]-1
            if i == cur:
                count += 1
                cur = dp[i]+i
        return count
