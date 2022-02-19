class Solution:
    def countPairs(self, nums: List[int], k: int) -> int: # fresh no data
        n = len(nums)
        out = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j] and not i*j % k:
                    out += 1
        return out
