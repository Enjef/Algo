class Solution:
    def firstUniqChar(self, s: str) -> int:  # 12.73% 70.16%
        x_dict = {}
        for char in s:
            x_dict[char] = x_dict.get(char, 0) + 1
        for i, char in enumerate(s):
            if x_dict[char] == 1:
                return i
        return -1
