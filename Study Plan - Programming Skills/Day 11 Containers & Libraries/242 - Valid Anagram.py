class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  # 51.67% 9.83%
        return sorted(s) == sorted(t)

    def isAnagram_count(self, s: str, t: str) -> bool:  # 59.40% 96.65%
        if len(s) != len(t):
            return False
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            s_dict[char] = s_dict.get(char, 0) - 1
            if s_dict[char] < 0:
                return False
        return True
