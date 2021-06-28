class Solution(object):
    def smallerNumbersThanCurrent_my(self, nums):
        out = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    out[i] += 1
        return out

    def smallerNumbersThanCurrent_better(self, nums):  # better
        res = []
        for i in nums:
            cnt = 0
            for j in nums:
                if i > j:
                    cnt += 1
            res.append(cnt)
        return res

    def smallerNumbersThanCurrent_best(self, nums):  # best
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, 101):
            count[i] += count[i-1]
        return [count[num] for num in nums]
