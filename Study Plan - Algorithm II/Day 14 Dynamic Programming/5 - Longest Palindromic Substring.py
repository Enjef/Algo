class Solution:
    def longestPalindrome(self, s: str) -> str:  # 18.74% 59.95%
        if s == s[::-1]:
            return s
        win = len(s)
        while win > 0:
            for i in range(len(s)-win+1):
                cur = s[i:i+win]
                if cur == cur[::-1]:
                    return cur
            win -= 1
