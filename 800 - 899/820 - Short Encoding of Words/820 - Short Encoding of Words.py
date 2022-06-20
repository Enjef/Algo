class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:  # 5.58% 92.09%
        words.sort(key=len, reverse=True)
        res = set()
        for word1 in words:
            for word2 in res:
                if word2.endswith(word1):
                    break
            else:
                res.add(word1)
        return sum(len(word)+1 for word in res)

    def minimumLengthEncoding_best_speed(self, words: List[str]) -> int:
        words.sort(key=lambda x: (x[::-1]), reverse=True)
        last = words[0]
        res = len(last)+1
        for w in words[1:]:
            if not last.endswith(w):
                res += len(w)+1
                last = w
        return res

    def minimumLengthEncoding_2nd_best_speed(self, words: List[str]) -> int:
        words = sorted(word[::-1] for word in set(words))
        words = words + ['']
        res = 0
        curr = ''
        for word in words:
            if not word.startswith(curr):
                res += len(curr) + 1
            curr = word  
        return res

    def minimumLengthEncoding_5th_best_speed(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)
