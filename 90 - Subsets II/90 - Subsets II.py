class Solution:
    def subsetsWithDup(
            self,
            nums: List[int]) -> List[List[int]]:  # 27.71% 95.36%
        nums.sort()
        out = [[]]
        for num in nums:
            for item in out[:]:
                new = item + [num]
                if new not in out:
                    out.append(new)
        return out

    def subsetsWithDup_best_speed(self, nums: List[int]) -> List[List[int]]:
        dictNums = {}
        for num in nums:
            if num in dictNums:
                dictNums[num] += 1
            else:
                dictNums[num] = 1
        result = [[],]
        for num in dictNums.keys():
            tmp = [x[:] for x in result]
            for i in range(dictNums[num]):
                l = len(tmp)
                for n in range(l):
                    tmp[n].append(num)
                    result.append(tmp[n][:])
        return result

    def subsetsWithDup_sec_best_sp(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()
        self.dfs(nums, res, temp, 0)
        return res

    def dfs(self, nums, res, temp, start):
        res.append(temp[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue

            temp.append(nums[i])
            self.dfs(nums, res, temp, i+1)
            temp.pop()

    def subsetsWithDup_sec_best_mem(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res
