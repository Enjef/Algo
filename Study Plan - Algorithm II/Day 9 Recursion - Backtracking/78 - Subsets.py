class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:  # 84.09% 50.57%
        res = []
        subres = []

        def dfs(i):
            if i >= len(nums):
                res.append(subres[:])
                return
            subres.append(nums[i])
            dfs(i+1)
            subres.pop()
            dfs(i+1)
        dfs(0)
        return res
