class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:  # 37.75% 47.87%
        return sum([s.startswith(word) for word in words])

    def countPrefixes_v2(self, words, s):  # 64.51% 93.14%
        result = 0
        for word in words:
            result += s.startswith(word)
        return result

    def countPrefixes_best_speed(self, words: List[str], s: str) -> int:
        return len(list(filter(lambda w: s.startswith(w), words)))

    def countPrefixes_3d_best_memory(self, words: List[str], s: str) -> int:
        res = 0
        for w in words:
            if w[0] != s[0]:
                continue
            if w in s[:len(w)]:
                res += 1
        return res
