class Solution:
    def jump(self, nums: List[int]) -> int:  # 44.84% 98.15%
        count = curr_jump = max_jump = 0
        for i in range(len(nums)-1):
            max_jump = max(max_jump, nums[i] + i)
            if i == curr_jump:
                curr_jump = max_jump
                count += 1
        return count

    def minJumps(self, nums, n):
        if n == 0:
            return 0
        prev = max_reach = jumps = 0
        for i in range(n):
            if i > prev:
                jumps += 1
                prev = max_reach
            max_reach = max(max_reach, i + nums[i])
        return jumps

    def jump_best_speed(self, nums: List[int]) -> int:
        return self.minJumps(nums, len(nums))
