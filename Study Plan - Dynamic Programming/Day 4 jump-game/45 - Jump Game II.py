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
