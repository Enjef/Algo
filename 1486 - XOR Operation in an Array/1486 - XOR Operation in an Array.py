class Solution:
    def xorOperation_my(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res

    def xorOperation_best(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans^=(start + 2*i)
        return ans
