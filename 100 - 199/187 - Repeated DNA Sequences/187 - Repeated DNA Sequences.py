class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:  # 73.56% 57.92%
        if len(s) < 11:
            return []
        seen = set()
        out = set()
        for i in range(len(s)-9):
            if s[i:i+10] in seen:
                out.add(s[i:i+10])
            else:
                seen.add(s[i:i+10])
        return out

    def findRepeatedDnaSequences_best_speed(self, s: str) -> List[str]:
        result = []
        occurDict = {}
        for i in range(len(s) - 9):
            currStr = s[i: i + 10]
            if currStr in occurDict:
                if occurDict[currStr] == 1:
                    result.append(currStr)
                    occurDict[currStr] = 2
            else:
                occurDict[currStr] = 1
        return result

    def findRepeatedDnaSequences_5th_best_speed(self, s: str) -> List[str]:
        from collections import Counter
        count = Counter(s[i-10:i] for i in range(10, len(s)+1))
        return [key for key in count if count[key] > 1]

    def findRepeatedDnaSequences_best_memory(self, s: str) -> List[str]:
        if len(s) < 11:
            return []
        answer = set()
        matches = defaultdict(list)
        base = ord('T') + 1
        mod = 5381
        L = 10
        high = 1
        for _ in range(10):
            high = (high*base) % mod
        hash_key = 0
        for i in range(len(s)):
            hash_key = (hash_key*base + ord(s[i])) % mod
            if i >= L:
                hash_key = (hash_key - ord(s[i-L])*high) % mod
                if hash_key in matches.keys():
                    for idx in matches[hash_key]:
                        are_same = self.compare(s[i-L+1:i+1], s[idx:idx+L])

                        if are_same:
                            answer.add(s[idx:idx+L])
            if i >= L-1:
                matches[hash_key].append(i-L+1)
        return answer

    def compare(self, a, b):
        j = 0
        while j < len(a):
            if a[j] != b[j]:
                return False
            j += 1
        return True

    from collections import defaultdict
    def findRepeatedDnaSequences_2dn_best_memory(self, s: str) -> List[str]:
        def suffixArray1(s):
            return sorted(range(len(s)), key=lambda i: s[i:])

        def suffixArray(s, buckets, order):
            d = defaultdict(list)
            for b in buckets:
                d[s[b: b+order]].append(b)
            sol = []
            for k, v in sorted(d.items()):
                if len(v) > 1:
                    sol.extend(suffixArray(s, v, order*2))
                else:
                    sol.append(v[0])
            return sol

        def prefix(x, y):
            N1, N2 = len(x), len(y)
            i = 0
            while i < N1 and i < N2:
                if x[i] != y[i]:
                    break
                if i == 9:
                    return True
                i += 1
            return False

        N = len(s)
        sa = suffixArray(s, range(N), 1)
        sol = set()
        x = sa[0]
        for y in sa[1:]:
            if prefix(s[x:], s[y:]):
                sol.add(s[x:x+10])
            x = y
        return sol

    def findRepeatedDnaSequences_4th_best_memory(self, s: str) -> List[str]:
        ans = []
        codes = {'A': 0, 'G': 1, 'C': 2, 'T': 3}
        r_codes = 'AGCT'
        if len(s) < 10:
            return []
        h = 0
        for i in range(10):
            c = s[i]
            h = h << 2
            h += codes[c]
        max_h = 1 << 20
        hashes = [0] * max_h
        hashes[h] = 1
        for j in range(10, len(s)):
            c = s[j]
            h = h & ((1 << 18) - 1)
            h = h << 2
            h += codes[c]
            hashes[h] += 1

        def restore_str(h):
            res_s = ""
            for i in range(9, -1, -1):
                t = (h >> (2 * i)) & 3
                res_s += r_codes[t]
            return res_s

        for i in range(max_h):
            if hashes[i] > 1:
                ans.append(restore_str(i))
        return ans
