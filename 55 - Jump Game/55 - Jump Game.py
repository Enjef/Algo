class Solution:
    def canJump(self, nums: List[int]) -> bool:  # 17.58% 98.74%
        jump_max = 0
        for i in range(len(nums) - 1):
            jump_max = max(jump_max, i + nums[i])
            if i - jump_max >= 0:
                return False
        return True

    def canJump_best_speed(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(last, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0

    def canJump_dp(self, nums: List[int]) -> bool:  # 57.41% 35.65%
        if len(nums) == 1:
            return True
        dp = [0]*len(nums)
        for i in range(len(nums)-1):
            dp[i] = max(dp[i-1]-1, nums[i])
            if dp[i] <= 0:
                return False
        return True
