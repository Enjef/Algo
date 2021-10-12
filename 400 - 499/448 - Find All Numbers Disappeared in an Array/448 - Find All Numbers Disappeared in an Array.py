class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        full = [x for x in range(1, len(nums)+1)]
        nums = set(nums)
        out = []
        for i in full:
            if i not in nums:
                out.append(i)
        return out
