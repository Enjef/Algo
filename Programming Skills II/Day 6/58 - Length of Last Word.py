class Solution:
    def lengthOfLastWord(self, s: str) -> int:  # 94.39% 87.16%
        res = 0
        i = len(s) - 1
        while i > -1 and s[i] == ' ':
            i -= 1
        while i > -1 and s[i] != ' ':
            res += 1
            i -= 1
        return res

    def lengthOfLastWord_v2(self, s: str) -> int:  # 85.19% 54.59%
        return len(s.split()[-1])
