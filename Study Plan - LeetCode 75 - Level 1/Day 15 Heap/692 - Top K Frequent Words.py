class Solution:
    # 98.82% 27.36%
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
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
