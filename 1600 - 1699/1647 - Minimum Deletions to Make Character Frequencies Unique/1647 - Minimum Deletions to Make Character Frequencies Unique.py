class Solution:
    def minDeletions(self, s: str) -> int:  # 72.96% 17.36%
        count = Counter(s)
        d = dict()
        seen = set()
        for (char, qty) in count.items():
            if qty not in d:
                d[qty] = set()
            d[qty].add(char)
        seen = set(d)
        result = 0
        for char, qty in count.items():
            if len(d[qty]) == 1:
                continue
            temp = qty
            while qty > 0:
                qty -= 1
                result += 1
                if qty not in seen:
                    seen.add(qty)
                    d[temp].discard(char)
                    break
            else:
                d[temp].discard(char)
        return result

    def minDeletions_best_speed(self, s: str) -> int:
        freq = {k: s.count(k) for k in 'abcdefghijklmnopqrstuvwxyz'}
        freq = dict(x for x in sorted(freq.items(), reverse=True,
                    key=lambda item: item[1]) if x[1])
        seen = set()
        ops = 0
        for key, value in freq.items():
            if value in seen:
                while value in seen:
                    ops += 1
                    value -= 1
            if value:
                seen.add(value)
        return ops

    def minDeletions_best_memory(self, s: str) -> int:
        frequencies = [0]*26
        for c in s:
            frequencies[ord(c)-ord('a')] += 1
        seen_f = set()
        deleted_f = 0
        for i in range(26):
            while frequencies[i] and frequencies[i] in seen_f:
                frequencies[i] -= 1
                deleted_f += 1
            seen_f.add(frequencies[i])
        return deleted_f
