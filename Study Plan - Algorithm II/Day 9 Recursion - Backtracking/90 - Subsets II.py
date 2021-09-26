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
