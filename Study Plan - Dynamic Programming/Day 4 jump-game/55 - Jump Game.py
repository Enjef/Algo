class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_max = 0
        for i in range(len(nums) - 1):
            jump_max = max(jump_max, i + nums[i])
            if i - jump_max >= 0:
                return False
        return True
        
    def canJump_dp(self, nums: List[int]) -> bool:  # 57.41% 35.65%
        if len(nums) == 1:
            return True
        dp = [0]*len(nums)
        for i in range(len(nums)-1):
            dp[i] = max(dp[i-1]-1, nums[i])
            if dp[i] <= 0:
                return False
        return True