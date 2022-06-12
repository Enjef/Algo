class Solution:
    # 33.33% 33.33%
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        d = defaultdict(set)
        for key, val in mappings:
            d[key].add(val)
        n, m = len(s), len(sub)
        for i in range(n-m+1):
            for j in range(m):
                if s[i+j] != sub[j] and s[i+j] not in d[sub[j]]:
                    break
            else:
                return True
        return False

    def matchReplacement_best_speed(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        if len(s) < len(sub):
            return False
        mp = defaultdict(set)
        for x, y in mappings:
            mp[x].add(y)

        def fn(ss):
            for cc, c in zip(ss, sub):
                if cc != c and cc not in mp[c]:
                    return False
            return True

        for i in range(0, len(s)-len(sub)+1):
            ss = s[i:i+len(sub)]
            if fn(ss):
                return True
        return False

    def matchReplacement_best_memory(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        if len(s) < len(sub):
            return False
        mp = defaultdict(set)
        for x, y in mappings:
            mp[x].add(y)
        for i in range(0, len(s)-len(sub)+1):
            ss = s[i:i+len(sub)]
            if all(cc == c or cc in mp[c] for cc, c in zip(ss, sub)):
                return True
        return False
