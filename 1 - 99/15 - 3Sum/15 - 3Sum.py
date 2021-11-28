class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:  # 99.28%
        x_map = {}
        out = set()
        for num in nums:
            if num in x_map:
                x_map[num] += 1
            else:
                x_map[num] = 1
        if 0 in x_map and x_map[0] >= 3:
            out.add((0, 0, 0))
        less = [i for i in x_map if i < 0]
        more = [i for i in x_map if i > 0]
        for i in less:
            for j in more:
                k = -(i + j)
                if k in x_map and ((k != i and k != j) or x_map[k] > 1):
                    temp = tuple(sorted([i, j, k]))
                    out.add(temp)
        return out

    def threeSum_ds_2_day_1(
            self,
            nums: List[int]) -> List[List[int]]:  # 19.87% 26.58%
        diff = set()
        n = len(nums)
        out = set()
        for i in range(n-1):
            for j in range(i+1, n):
                if -(nums[i]+nums[j]) in diff:
                    out.add(
                        tuple(sorted([-nums[i]-nums[j], nums[i], nums[j]]))
                    )
            diff.add(nums[i])
        return out
