class Solution:
    def myAtoi(self, s: str) -> int:
        num = ''
        a_char = '1234567890'
        sign = False
        for char in s:
            if char in '-+' and not sign and not num:
                sign = True
                num += char
                continue
            if char == ' ' and not num and not sign:
                continue
            if char not in a_char and not num:
                return 0
            if char not in a_char and num:
                break
            num += char
        if not num.lstrip('-').lstrip('+').isdigit():
            return 0
        num = int(num)
        if num < -2**31:
            num = -2**31
        if num > 2**31 - 1:
            num = 2**31 - 1
        return num
