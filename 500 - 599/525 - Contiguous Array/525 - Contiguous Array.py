class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        diff_map = {0: -1}
        out = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count -= 1
            if count not in diff_map:
                diff_map[count] = i
            else:
                out = max(out, i - diff_map[count])
        return out
