class Solution:
    def titleToNumber(self, columnTitle):  # 98.23% 56.94%
        """
        :type columnTitle: str
        :rtype: int
        """
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        out = 0
        for i, char in enumerate(columnTitle):
            out += (abc.index(char) + 1) * (26**(len(columnTitle)-i-1))
        return out

    def titleToNumber_mock(self, columnTitle: str) -> int:  # 33.80%  98.11%
        alp = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))
        res = 0
        for i, char in enumerate(columnTitle):
            res = res*26 + alp[char]
        return res

    def titleToNumber_best_speed(self, columnTitle: str) -> int:
        total = 0
        for c, v in enumerate(columnTitle[::-1]):
            total += (ord(v)-64)*(26**c)
        return total

    def titleToNumber_3rd_best_speed(self, columnTitle: str) -> int:
        result = 0
        for letter in columnTitle:
            result = result * 26 + ord(letter) - ord('A') + 1
        return result
