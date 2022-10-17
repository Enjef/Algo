class Solution:
    # 73.42% 10.25% (90.43% 79.08%)
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(1, len(nums)):
            cur = nums[i]+nums[i-1]
            if cur in seen:
                return True
            seen.add(cur)
        return False
