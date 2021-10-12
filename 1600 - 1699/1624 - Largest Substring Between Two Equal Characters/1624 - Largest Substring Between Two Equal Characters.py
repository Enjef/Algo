class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:  # 75.68% 90.09%
        elin = {}
        sub_max = -1
        for i, char in enumerate(s):
            if char in elin:
                sub_max = max(sub_max, i-elin[char]-1)
            else:
                elin[char] = i
        return sub_max

    def maxLengthBetweenEqualCharacters_best_speed(self, s: str) -> int:
        first_index = {}
        max_offset = -1
        for i, c in enumerate(s):
            if c not in first_index:
                first_index[c] = i
            else:
                offset = i - first_index[c] - 1
                if offset > max_offset:
                    max_offset = offset
        return max_offset

    def maxLengthBetweenEqualCharacters_best_memory(self, s: str) -> int:
        n = len(s)
        max_ = -1
        d = dict()
        if n <= 2:
            return 0
        for i in range(0, len(s)):
            if d.get(s[i], -1) == -1:
                d[s[i]] = i
            else:
                max_ = max(max_, i-d[s[i]]-1)
        return max_
