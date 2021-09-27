class Solution:
    def permuteUnique(
            self,
            nums: List[int]) -> List[List[int]]:  # 7.73% 43.73%
        def dfs(arr, path=[], res=[]):
            if not arr:
                if path not in res:
                    res.append(path)
            for i, num in enumerate(arr):
                dfs(arr[:i]+arr[i+1:], path+[num], res)
            return res
        return dfs(nums)
