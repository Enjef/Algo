class Solution:
    def combinationSum2(
            self,
            candidates: List[int],
            target: int) -> List[List[int]]:  # 5.02% 75.88%
        candidates.sort()

        def helper(arr, target, nums=[], res=[]):
            if target == 0:
                cur = sorted(nums)
                if cur not in res:
                    res.append(cur)
            elif target < 0:
                return
            for i, num in enumerate(arr):
                if i > 0 and arr[i] == arr[i-1]:
                    continue
                helper(arr[:i]+arr[i+1:], target-num, nums+[num], res)
            return res
        return helper(candidates, target)
