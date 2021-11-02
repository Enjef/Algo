class Solution:
    def combinationSum(
            self,
            candidates: List[int],
            target: int) -> List[List[int]]:  # 22.42% 51.39%
        candidates.sort()

        def helper(part, nums, tar, path=[]):
            if tar == 0:
                path.append(part)
            if tar < 0:
                return
            for i, num in enumerate(nums):
                helper(part[:]+[num], nums[i:], tar-num)
            return path
        return helper([], candidates, target)

    def combinationSum_tuple_set(
            self,
            candidates: List[int],
            target: int) -> List[List[int]]:  # 6.13% 51.98%
        def helper(arr, target, cur=tuple(), out=set()):
            if target < 0:
                return out
            if not target:
                out.add(tuple(sorted(cur)))
                return out
            for i in range(len(arr)):
                helper(arr, target-arr[i], cur+(arr[i],), out)
            return out
        return helper(candidates, target)
