class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:  # 24.98% 67.98%
        if not nums:
            return 0
        length = 1
        pos = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and pos != True:
                length += 1
                pos = True
            if nums[i] < nums[i - 1] and pos != False:
                length += 1
                pos = False
        return length
