class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        j = 0
        n = len(s)
        for char in t:
            if char == s[j]:
                j += 1
            if j == n:
                return True
        return False
