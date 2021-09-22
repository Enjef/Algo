import itertools


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:  # 83.99% 50.59%
        out = [[]]
        for num in nums:
            temp = []
            for el in out:
                temp.append(el + [num])
            out.extend(temp)
        return out

    def subset(self, nums, i):
        return list(map(list, itertools.combinations(nums, i)))

    def subsets_sec_to_best_speed(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(n+1):
            a = self.subset(nums, i)
            for j in a:
                ans.append(j)
        return ans

    def subsets_fifth_to_best_speed(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

    def subsets_sec_to_best_memory(self, nums: List[int]) -> List[List[int]]:
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
