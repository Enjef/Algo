class Solution:
    def findNumbers(self, nums: List[int]) -> int:  # 77.34% 41.94%
        out = 0
        if not nums:
            return out
        for num in nums:
            if len(str(num)) % 2 == 0:
                out += 1
        return out
