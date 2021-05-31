class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(1, len(s)-1):
            if len(set(s[i-1:i+2])) == 3:
                count += 1
        return count
