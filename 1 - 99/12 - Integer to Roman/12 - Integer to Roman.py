import math

symb_dist = [['I', 'V'], ['X', 'L'], ['C', 'D'], ['M']]


class Solution:
    def intToRoman(self, num: int) -> str:
        size = int(math.log10(num))
        out = ''
        for i in range(size + 1):
            index = size - i
            digit = num // 10 ** (index) % 10
            if digit < 4:
                for j in range(digit):
                    out += symb_dist[index][0]
            if digit == 4:
                out += symb_dist[index][0] + symb_dist[index][1]
            if digit == 5:
                out += symb_dist[index][1]
            if 5 < digit < 9:
                out += symb_dist[index][1]
                for j in range(digit-5):
                    out += symb_dist[index][0]
            if digit == 9:
                out += symb_dist[index][0] + symb_dist[index+1][0]
        return out


x = Solution()
x.intToRoman(1994)
