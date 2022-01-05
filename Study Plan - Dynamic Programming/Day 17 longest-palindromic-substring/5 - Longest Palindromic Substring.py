class Solution:
    def longestPalindrome(self, s: str) -> str:  # 8.50% 81.55%
        if s==s[::-1]:
            return s
        n = len(s)
        size = 1
        s_max = s[0]
        while size < n:
            for i in range(n-size+1):
                if (
                    s[i:i+size] == s[i+size-1:i-n-1:-1] and
                    len(s_max) < len(s[i:i+size])):
                        s_max = s[i:i+size]
            size += 1
        return s_max
