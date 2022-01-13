class Solution:
    def topKFrequent(
            self, words: List[str], k: int) -> List[str]:  # 76.86% 5.00%
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        rev_d = {}
        for key, value in d.items():
            if value not in rev_d:
                rev_d[value] = []
            rev_d[value].append(key)
        out = []
        for key in sorted(rev_d, reverse=True):
            out.extend(sorted(rev_d[key]))
            if len(out) > k:
                break
        return out[:k]

    def topKFrequent_best_speed(self, words: List[str], k: int) -> List[str]:
        c = {}
        for word in words:
            c[word] = 1 + c.get(word, 0)
        h = [(-val, key) for key, val in c.items()]
        h.sort()
        output = []
        while len(output) < k:
            if h:
                word = h.pop(0)
                output.append(word[1])
        return output

    def topKFrequent_2nd_best_speed(self, words, k: int) -> List[str]:
        count = collections.Counter(words)
        words = sorted(set(words), key = lambda x : (-count[x], x))
        return words[0:k]

    def topKFrequent_3d_memory(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        h = []
        for key, val in counter.items():
            heappush(h, (-val, key))
        res = []
        for _ in range(k):
            res.append(heappop(h)[1])
        return res
