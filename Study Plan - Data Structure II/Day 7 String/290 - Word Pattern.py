class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:  # 95.51% 99.37%
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
