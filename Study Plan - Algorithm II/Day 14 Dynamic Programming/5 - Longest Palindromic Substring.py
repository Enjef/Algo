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

    def longestPalindrome_dp_slice(self, s: str) -> str:  # 23.36% 12.17%
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        out = s[0]
        for i in range(n):
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    if i-j == 1 or dp[i-1][j+1]:
                        dp[i][j] = 1
                        if len(out) < len(s[j:i+1]):
                            out = s[j:i+1]
        return out
