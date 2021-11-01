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

    def subsetsWithDup_second_try(
            self,
            nums: List[int]) -> List[List[int]]:  # 64.32% 58.93%
        out = [[]]
        for num in nums:
            temp = []
            for item in out:
                cur = sorted(item+[num])
                if cur not in out:
                    temp.append(cur)
            out.extend(temp)
        return out
