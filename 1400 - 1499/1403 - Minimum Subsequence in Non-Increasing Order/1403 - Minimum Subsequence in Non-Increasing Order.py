class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:  # 46.09%  66.99%
        nums.sort()
        out = [nums.pop()]
        while sum(nums) >= sum(out):
            out.append(nums.pop())
        return out

    def minSubsequence_best(self, nums: List[int]) -> List[int]:
        sm = sum(nums)
        nums.sort()
        ans = []
        csm = 0
        for num in nums[::-1]:
            csm += num
            ans.append(num)
            if csm > sm/2:
                break
        return ans
