class Solution:
    def jump(self, nums: List[int]) -> int:  # 78.87% 45.59%
        max_jump = 0
        cur_jump = 0
        jumps = 0
        for i in range(len(nums)-1):
            max_jump = max(i + nums[i], max_jump)
            if i == cur_jump:
                cur_jump = max_jump
                jumps += 1
        return jumps
