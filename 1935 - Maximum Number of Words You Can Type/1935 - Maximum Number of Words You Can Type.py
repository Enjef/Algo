class Solution:
    def canBeTypedWords(
            self,
            text: str,
            brokenLetters: str) -> int:  # 77.43% 87.59%
        words = text.split()
        out = len(words)
        if not brokenLetters:
            return out
        for word in words:
            for char in set(word):
                if char in brokenLetters:
                    out -= 1
                    break
        return out

    def canBeTypedWords_best(self, text: str, brokenLetters: str) -> int:
        c = 0
        l = text.split(' ')
        for i in l:
            b = 0
            for j in brokenLetters:
                if j in i:
                    b += 1
                    break
            if b == 0:
                c += 1
        return c
