class Solution:
    def findTargetSumWays(
            self, nums: List[int], target: int) -> int:  # 9.10% 26.07%
        def dfs(idx=0,cur=0):
            if (idx, cur) in self.memo:
                return self.memo[(idx, cur)]
            if idx == n:
                if cur == target:
                    return 1
                return 0
            res = dfs(idx+1, cur+nums[idx]) + dfs(idx+1, cur-nums[idx])
            self.memo[(idx, cur)] = res
            return self.memo[(idx, cur)]
        n = len(nums)
        self.memo = {}
        return dfs()
