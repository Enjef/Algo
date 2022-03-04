class Solution:
    def findTheDifference(self, s: str, t: str) -> str:  # 70.25% 40.04%
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

    def findTheDifference_v2(self, s: str, t: str) -> str:  # 60.75% 40.04%
        s_dict = {}
        t_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
            if char not in s_dict or t_dict[char] > s_dict[char]:
                return char
