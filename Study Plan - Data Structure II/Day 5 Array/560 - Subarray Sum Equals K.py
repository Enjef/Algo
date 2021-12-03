class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:  # 94.45% 85.56%
        count = 0
        diffs = {0: 1}
        total = 0
        for num in nums:
            total += num
            count += diffs.get(total-k, 0)
            diffs[total] = diffs.get(total, 0) + 1
        return count
