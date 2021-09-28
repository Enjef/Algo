class Solution:
    def canJump(self, nums: List[int]) -> bool:  # 51.45% 34.89%
        max_jump = nums[0]
        cur_jump = nums[0]
        for i, num in enumerate(nums):
            if i == cur_jump:
                cur_jump = max_jump
            if i > max_jump:
                return False
            cur = i + num
            max_jump = max(cur, max_jump)
        return True
