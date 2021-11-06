class Solution:
    def numberOfArithmeticSlices(
            self,
            nums: List[int]) -> int:  #  83.22% 44.05%
        if len(nums) < 3:
            return 0
        combo = False
        count = 0
        for i in range(len(nums)-2):
            if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
                count += 1 + combo * i
                combo = True
            else:
                combo = False
        return count

    def numberOfArithmeticSlices_v2(
            self,
            nums: List[int]) -> int:  # 99.73% 74.02%
        if len(nums) < 3:
            return 0
        out = 0
        j = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                j += 1
                out += j
            else:
                j = 0
        return out
