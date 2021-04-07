symb_dist = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        out = 0
        temp = symb_dist[s[0]]
        prev = s[0]
        for char in s[1:]:
            if char == prev:
                temp += symb_dist[char]
                continue
            if symb_dist[char] > symb_dist[prev]:
                out += symb_dist[char] - temp
                temp = 0
                prev = char
                continue
            prev = char
            out += temp
            temp = symb_dist[char]
        out += temp
        return out

x = Solution()
x.romanToInt('LVIII')
