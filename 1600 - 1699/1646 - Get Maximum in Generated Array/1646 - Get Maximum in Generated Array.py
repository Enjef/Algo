class Solution:
    def getMaximumGenerated(self, n: int) -> int:  # 73.57% 91.72%
        nums = [0] * n
        nums[:1] = [0, 1]
        res = 0
        if n == 0:
            return nums[0]
        if n == 1:
            return nums[1]
        for i in range(2, n+1):
            if i % 2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[i//2+1]
            res = max(res, nums[i])
        return res
