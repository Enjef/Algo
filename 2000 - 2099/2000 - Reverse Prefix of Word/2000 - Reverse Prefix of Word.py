class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:  # 96.97% 98.01%
        for i, char in enumerate(word):
            if char == ch:
                break
        else:
            return word
        return ''.join([word[:i+1][::-1], word[i+1:]])

    def reversePrefix_best_speed(self, word: str, ch: str) -> str:
        if word.find(ch) >= 0:
            x = word.find(ch)
            w = word[:x+1]
            return w[::-1]+word[x+1:]
        return word

    def reversePrefix_2nd_best_speed(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            loc = word.index(ch)
            txt = word[0:loc+1]
            return txt[::-1] + word[loc+1:]

    def reversePrefix_best_memory(self, s: str, c: str) -> str:
        i = 0
        if c in s:
            while s[i] != c:
                i += 1
            s = s.replace(s[:i+1], s[:i+1][::-1])
        return s

    def reversePrefix_2nd_best_memory(self, word: str, ch: str) -> str:
        for i, letter in enumerate(word):
            if ch == letter:
                return word[:i+1][::-1] + word[i+1:]
        return word
