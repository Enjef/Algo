class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_max = 0
        for i in range(len(nums) - 1):
            jump_max = max(jump_max, i + nums[i])
            if i - jump_max >= 0:
                return False
        return True
