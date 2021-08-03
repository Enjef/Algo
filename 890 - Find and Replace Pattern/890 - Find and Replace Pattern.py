class Solution:
    def findAndReplacePattern(
            self,
            words: List[str],
            pattern: str
            ) -> List[str]:  # 50.23% 32.60%
        w_map = {}
        out = []
        for word in words:
            out.append(word)
            for i in range(len(word)):
                if word[i] not in w_map:
                    w_map[word[i]] = pattern[i]
                if (
                        w_map[word[i]] != pattern[i] or
                        w_map[word[i]] == pattern[i] and
                        list(w_map.values()).count(pattern[i]) > 1):
                    out.pop()
                    break
            w_map.clear()
        return out

    def findAndReplacePattern_s_to_best(
            self,
            words: List[str],
            pattern: str) -> List[str]:
        pm = self.strToPat(pattern)
        res = []
        for w in words:
            if self.strToPat(w) == pm:
                res.append(w)
        return res
   
    def strToPat(self, s):
        i = 0
        m = {}
        res = ""
        for c in s:
            if c not in m:
                m[c] = i
                i += 1
            res += str(m[c])
        return res

    def findAndReplacePattern_best(
            self, words: List[str], pattern: str) -> List[str]:
        p = dict()
        seen = set()
        res = []
        for c in pattern:
            p[c] = ""
        for w in words:
            flag = 1
            for i in range(len(pattern)):
                c = pattern[i]
                if p[c] == "":
                    if w[i] in seen:
                        flag = 0
                        break
                    p[c] = w[i]
                    seen.add(w[i])
                else:
                    if w[i] != p[c]:
                        flag = 0
                        break
            if flag:
                res.append(w)
            for c in pattern:
                p[c] = ""
            seen = set()
        return res
