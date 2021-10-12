class Solution:
    def minPairSum(self, nums: List[int]) -> int:  # 79.29% 78.09%
        nums.sort()
        out = nums[0]
        for i in range(0, len(nums)//2):
            cur = nums[i] + nums[len(nums) - i - 1]
            if out < cur:
                out = cur
        return out

    def minPairSum_best(self, nums: List[int]) -> int:
        result = sorted(nums)
        asc = result[0:int(len(nums)/2)]
        desc = result[int(len(nums)/2):]
        desc = sorted(desc, reverse=True)
        max = 0
        for asc_val, desc_val in zip(asc, desc):
            if max < asc_val + desc_val:
                max = asc_val+desc_val
        return max
