class Solution:
    def lengthOfLastWord(self, s: str) -> int:  # 85.19% 54.59%
        out = 0
        if len(s) == 1 and s[0] == ' ':
            return 0
        if len(s) == 1 and s[0] != ' ':
            return 1
        for char in range(len(s)-1, -1, -1):
            if out and s[char] == ' ':
                break
            if s[char] != ' ':
                out += 1
        if out:
            return out
        return 0

    def lengthOfLastWord_v3(self, s: str) -> int:  # 94.39% 87.16%
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
