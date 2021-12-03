class Solution:
    def longestPalindrome(self, s: str) -> int:  # 76.23% 95.01%
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        any_odd = 0
        out = 0
        for value in counter.values():
            if value % 2 != 0:
                any_odd = 1
                out += value - 1
            else:
                out += value
        return out + any_odd
