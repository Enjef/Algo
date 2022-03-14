class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:  # 42.97% 47.51%
        n = len(s)
        win = 1
        while win < n//2+1:
            if not n%win:
                if s[:win]*(n//win) == s:
                    return True
            win += 1
        return False
