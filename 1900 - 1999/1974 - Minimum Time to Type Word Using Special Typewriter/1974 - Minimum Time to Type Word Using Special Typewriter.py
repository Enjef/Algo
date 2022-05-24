class Solution:
    def minTimeToType(self, word: str) -> int:  # 22.84% 16.21%
        total = len(word)
        cur = ord('a')
        for i in range(len(word)):
            total += min(
                abs(cur-ord(word[i])), abs(26 - abs(cur-ord(word[i]))))
            cur = ord(word[i])
        return total

    def minTimeToType_v2(self, word: str) -> int:  # 81.77% 81.77%
        return sum([min(abs(ord(a)-ord(b)), abs(26-abs(ord(a)-ord(b)))) for a, b in pairwise('a'+word)]) + len(word)

    def minTimeToType(self, word: str) -> int:  # 16.76% 96.69%
        return sum([min(abs(ord(a)-ord(b)), abs(26-abs(ord(a)-ord(b)))) for a, b in zip('a'+word, word)]) + len(word)

    def minTimeToType_best_speed(self, word: str) -> int:
        result = len(word)
        start = ord('a')
        for ch in word:
            result += min(abs(ord(ch) - start), 26 - abs(ord(ch) - start))
            start = ord(ch)
        return result

    def minTimeToType_best_memory(self, word: str) -> int:
        ans = len(word)
        pre = 'a'
        for w in word:
            length = (ord(w) - ord(pre)) % 26
            ans += min(length, 26 - length)
            pre = w
        return ans
