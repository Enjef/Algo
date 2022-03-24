class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:  # 99.68% 66.83%
        total = sum(nums)
        cur = 0
        for i, num in enumerate(nums):
            if total - cur - num == cur:
                return i
            cur += num
        return -1
