class Solution:
    def maxProduct(self, words: List[str]) -> int:  # 28.65% 71.68%
        result = 0
        n = len(words)
        for i in range(n-1):
            set_i = set(words[i])
            for j in range(i+1, n):
                if not set_i & set(words[j]):
                    result = max(result, len(words[i])*len(words[j]))
        return result

    def maxProduct_best_speed(self, words: List[str]) -> int:
        def hashset(word):
                return sum(1 << (ord(c) - ord('a')) for c in set(word))

        d, ans = defaultdict(int), 0
        for w in words:
            h = hashset(w)
            if d[h] < len(w):
                for other in d:
                        if not other & h:
                            ans = max(d[other] * len(w), ans)
                d[h] = len(w)
        return ans

    def maxProduct_best_memory(self, words: List[str]) -> int:
        bitmaps = []
        for w in words:
            bmp = 0
            for c in w:
                bmp |= 1 << (ord(c) - ord('a'))
            bitmaps.append(bmp)
        best = 0
        for i in range(len(bitmaps)):
            for j in range(i + 1, len(bitmaps)):
                if not bitmaps[i] & bitmaps[j]:
                    best = max(best, len(words[i]) * len(words[j]))
        return best
