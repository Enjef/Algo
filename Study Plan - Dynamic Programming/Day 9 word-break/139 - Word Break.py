class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:  # 15.17% 87.84%
        next_start = [0]
        n = len(s)
        for i in range(n):
            for j in next_start:
                if s[j:i+1] in wordDict:
                    next_start.append(i+1)
                    break
        return n == next_start[-1]
