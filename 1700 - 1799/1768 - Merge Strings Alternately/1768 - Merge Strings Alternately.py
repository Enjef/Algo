class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:  # 96.09% 50.41%
        diff = len(word1) - len(word2)
        end = ''
        out = ''
        if diff < 0:
            end = word2[len(word1):]
        if diff > 0:
            end = word1[len(word2):]
        for i in range(min(len(word1), len(word2))):
            out += f'{word1[i]}{word2[i]}'
        out += end
        return out

    def mergeAlternately_best(self, word1: str, word2: str) -> str:
        c = ""
        j = 0
        k = 0
        p = min(len(word1), len(word2))
        for i in range(0, p*2):
            if i % 2 == 0:
                c = c + word1[j]
                j += 1
            else:
                c = c + word2[k]
                k += 1
        if j != len(word1):
            while (j != len(word1)):
                c = c+word1[j]
                j += 1
        elif k != len(word2):
            while k != len(word2):
                c = c + word2[k]
                k += 1
        return c
