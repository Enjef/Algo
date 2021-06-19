class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i, j = 0, n
        out = []
        for i in range(n):
            out += [nums[i], nums[j + i]]
        return out
