class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[-i] != t[-i]:
                return False
        return True

    def short(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
