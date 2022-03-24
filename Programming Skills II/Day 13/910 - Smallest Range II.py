class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:  # 80.29% 29.75%
        nums.sort()
        n = len(nums)
        n_min, n_max = nums[0]+k, nums[-1]-k
        res = nums[-1] - nums[0]
        for i in range(n-1):
            res = min(res, max(n_max, nums[i]+k) - min(n_min, nums[i+1]-k))
        return res
