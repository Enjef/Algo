class Solution:
    def maxScore(self, s: str) -> int:  # 28.01% 77.23%
        score_max = 0
        for i in range(1,len(s)):
            score_max = max(score_max, s[:i].count('0') + s[i:].count('1'))
        return score_max

    def maxScore_best(self, nums: str) -> int:
        ans = float('-inf')
        zeros = 0
        ones = 0
        for i in range(len(nums)):
            if nums[i] == '0':
                zeros += 1
            else:
                ones += 1
            if i != len(nums)-1:
                ans = max(ans, zeros-ones)
        return ans + ones
