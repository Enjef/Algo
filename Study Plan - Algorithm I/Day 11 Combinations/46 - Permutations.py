class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:  # 90.51% 41.96%
        def helper(arr, cur, res=[]):
            if not arr:
                res.append(cur)
                return res
            for i, char in enumerate(arr):
                helper(arr[:i]+arr[i+1:], cur+[char], res)
            return res
        return helper(nums, [])
