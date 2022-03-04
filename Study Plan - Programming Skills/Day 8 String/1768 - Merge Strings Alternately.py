class Solution: # second run 25.81% 99.91%
    def mergeAlternately(self, word1: str, word2: str) -> str: # 40.30% 48.10%
        n, m = len(word1), len(word2)
        if n > m:
            rest = word1[m:]
        else:
            rest = word2[n:]
        return ''.join(''.join(x) for x in zip(word1, word2)) + rest
