class Solution:
    def removePalindromeSub(self, s: str) -> int: # 31.36% 100.00%
        return int(s == s[::-1]) or 2

    def removePalindromeSub_best_speed(self, s: str) -> int:
        if s==s[::-1]:
            return 1
        else:
            return 2
