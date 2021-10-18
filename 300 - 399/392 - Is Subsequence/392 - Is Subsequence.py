class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:  # 53.28% 24.06%
        if not s:
            return True
        filtred = ''
        for char in t:
            if char in set(s):
                filtred += char
        j = 0
        for char in filtred:
            if char == s[j]:
                j += 1
            if j == len(s):
                return True
        return False

    def isSubsequence_no_filter(self, s: str, t: str) -> bool:  # 77.70% 24.06%
        if not s:
            return True
        j = 0
        for char in t:
            if char == s[j]:
                j += 1
            if j == len(s):
                return True
        return False
