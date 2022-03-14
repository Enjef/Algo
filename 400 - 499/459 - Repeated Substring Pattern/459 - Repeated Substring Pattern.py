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

    def repeatedSubstringPattern_best_speed(self, s: str) -> bool:
        return s in (s+s)[1:-1]

    def repeatedSubstringPattern_best_memory(self, s: str) -> bool:
        n = len(s)
        for i in range(n-1):
            if n%(i+1) == 0:
                if s[:i+1] * (n//(i+1)) == s:
                    return True
        return False
