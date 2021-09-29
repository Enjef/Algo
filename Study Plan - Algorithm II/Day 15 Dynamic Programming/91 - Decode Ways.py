class Solution:
    def numDecodings(self, s: str) -> int:  # 99.33% 65.02%
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(dp)):
            if 0 < int(s[i-1]) < 10:
                dp[i] += dp[i-1]
            if s[i-2:i][0] != '0' and int(s[i-2:i]) < 27:
                dp[i] += dp[i-2]
        return dp[-1]
