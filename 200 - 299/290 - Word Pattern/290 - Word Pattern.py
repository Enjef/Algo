class Solution(object):
    def wordPattern(self, pattern, s):  # 77.41% 47.14%
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        char_map = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if str(pattern[i]) not in char_map:
                if s[i] in list(char_map.values()):
                    return False
                char_map[str(pattern[i])] = s[i]
            elif char_map[str(pattern[i])] != s[i]:
                return False
        return True

    def wordPattern_mock(self, pattern: str, s: str) -> bool:  # 95.51% 99.37%
        s = s.split()
        vals = set()
        if len(pattern) != len(s):
            return False
        check = {}
        for i in range(len(s)):
            if pattern[i] in check and check[pattern[i]] != s[i]:
                return False
            if s[i] in vals and pattern[i] not in check:
                return False
            check[pattern[i]] = s[i]
            vals.add(s[i])
        return True

    def wordPattern_best_speed(self, pattern: str, s: str) -> bool:
        a = s.split()
        if len(pattern) != len(a):
            return False
        d, d2 = {}, {}
        for c, w in zip(pattern, a):
            if c not in d:
                d[c] = w
            elif d[c] != w:
                return False
            if w not in d2:
                d2[w] = c
            elif d2[w] != c:
                return False
        return True
