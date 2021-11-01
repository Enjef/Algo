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

    def subsets_v(self, nums: List[int]) -> List[List[int]]:  # 32.22% 18.42%
        out = [[]]
        for num in nums:
            for item in out[:]:
                new = item + [num]
                if new not in out:
                    out.append(new)
        return out

    def subsets_v_2(self, nums: List[int]) -> List[List[int]]:  # 67.92% 51.62%
        out = [[]]
        for num in nums:
            temp = []
            for sample in out:
                temp.append(sample+[num])
            out.extend(temp)
        return out
