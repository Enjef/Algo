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

    def permuteUnique_tup_set(
            self,
            nums: List[int]) -> List[List[int]]:  # 21.03% 32.37%
        def helper(arr, cur=tuple(), out=set()):
            if not arr:
                out.add(cur)
            for i in range(len(arr)):
                new_cur = cur + (arr[i],)
                helper(arr[:i]+arr[i+1:], new_cur, out)
            return out
        return helper(nums)
