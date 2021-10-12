class Solution(object):
    def areOccurrencesEqual(self, s):  # 82.00% 93.00 %
        """
        :type s: str
        :rtype: bool
        """
        if len(set(s)) == 1:
            return True
        s_map = {}
        for char in s:
            if char not in s_map:
                s_map[char] = 0
            s_map[char] += 1
        values = list(s_map.values())
        for i in range(1, len(values)):
            if values[0] != values[i]:
                return False
        return True

    def areOccurrencesEqual_best(self, s):
        return (
            len(s) == 0) or (
                all([s.count(char) == s.count(s[0]) for char in set(s)])
        )
