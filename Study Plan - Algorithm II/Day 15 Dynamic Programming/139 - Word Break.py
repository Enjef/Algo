class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:  # 47.92% 69.13%
        dp = [0] * (len(s)+1)
        dp[0] = 1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        return dp[-1]
