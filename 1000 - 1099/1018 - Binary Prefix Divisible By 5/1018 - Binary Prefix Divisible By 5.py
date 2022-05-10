class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:  # 46.15% 51.72%
        out = [None] * len(nums)
        cur = 0
        for i, num in enumerate(nums):
            cur = cur*2 + num
            out[i] = cur % 5 == 0
        return out
 
    def prefixesDivBy5_best_speed(self, nums: List[int]) -> List[bool]:
        remainder = 0
        ans = []
        for num in nums:
            remainder = ((remainder << 1) + num) % 5
            ans.append(remainder == 0)
        return ans

    def prefixesDivBy5_2nd_best_speed(self, nums: List[int]) -> List[bool]:
        res = []
        sum = 0
        for bit in nums:
            sum = ( sum*2 + bit ) % 5
            res.append(sum == 0)
        return res
