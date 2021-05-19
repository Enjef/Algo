class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_map = {}
        for i in s:
            if i not in s_map:
                s_map[i] = 1
            else:
                s_map[i] += 1
        out = 0
        odd = False
        for key in s_map:
            if s_map[key] % 2 != 0:
                out += s_map[key] - 1
                odd = True
            else:
                out += s_map[key]
        if odd:
            out += 1
        return out

    def longestPalindrome_set(self, s: str) -> int:
        s_set = set()
        for i in s:
            if i not in s_set:
                s_set.add(i)
            else:
                s_set.remove(i)
        return len(s) if not s_set else len(s) - len(s_set) + 1
