class Solution:
    def jump(self, nums: List[int]) -> int:
        count = curr_jump = max_jump = 0
        for i in range(len(nums)-1):
            max_jump = max(max_jump, nums[i] + i)
            if i == curr_jump:
                curr_jump = max_jump
                count += 1
        return count
