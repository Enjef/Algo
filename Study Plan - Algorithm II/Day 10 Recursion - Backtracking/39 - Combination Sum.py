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
