class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:  # 19.87% 26.58%
        diff = set()
        n = len(nums)
        out = set()
        for i in range(n-1):
            for j in range(i+1, n):
                if -(nums[i]+nums[j]) in diff:
                    out.add(
                        tuple(sorted([-nums[i]-nums[j], nums[i], nums[j]]))
                    )
            diff.add(nums[i])
        return out
