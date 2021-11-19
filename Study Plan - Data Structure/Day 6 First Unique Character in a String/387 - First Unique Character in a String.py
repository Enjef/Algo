class Solution:
    def firstUniqChar(self, s: str) -> int:  # 12.73% 70.16%
        x_dict = {}
        for char in s:
            x_dict[char] = x_dict.get(char, 0) + 1
        for i, char in enumerate(s):
            if x_dict[char] == 1:
                return i
        return -1

    def firstUniqChar_v2(self, s: str) -> int:  # 63.32% 45.45%
        count = {}
        n = len(s)
        for i, char in enumerate(s):
            if char in count:
                count[char] = n + 1
            else:
                count[char] = i
        out = min(count.values())
        return out if out != n + 1 else -1
