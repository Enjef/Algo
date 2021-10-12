class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:  # 74.05% 41.73%
        def dfs(nums, temp=[], res=[]):
            if not nums:
                res.append(temp)
                return res
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], temp+[nums[i]], res)
            return res
        return dfs(nums)

    def permute_best_speed(self, nums: List[int]) -> List[List[int]]:
        def pick(nums):
            if len(nums) == 0:
                return []
            if len(nums) == 1:
                return [nums]
            result = []
            for i in range(len(nums)):
                v = nums.pop(i)
                permutes = self.permute(nums)
                for p in permutes:
                    p.insert(0, v)
                result += permutes
                nums.insert(i, v)
            return result
        return pick(nums[:])

    def permute_fourth_best_memory(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for sub in self.permute(nums[1:]):
            for i in range(len(sub) + 1):
                result.append(sub[:i] + nums[0:1] + sub[i:])
        return result
