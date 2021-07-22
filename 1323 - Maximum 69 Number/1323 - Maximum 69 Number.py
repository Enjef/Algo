class Solution:
    def maximum69Number(self, num: int) -> int:  # 59.58% 65.64%
        n = len(str(num))
        for i in range(n):
            digit = num // 10**(n - i - 1) % 10
            if digit == 6:
                num += 3 * (10 ** (n - i - 1))
                break
        return num

    def maximum69Number_str(self, num: int) -> int:  # 83.00% 65.64%
        str_num = str(num)
        n = len(str_num)
        for i in range(n):
            if str_num[i] == '6':
                list_num = list(str_num)
                list_num[i] = '9'
                num = int(''.join(list_num))
                break
        return num

    def maximum69Number_best(self, num: int) -> int:
        digits = list(str(num))
        for index, digit in enumerate(digits):
            if digit == '6':
                digits[index] = '9'
                break
        return int(''.join(digits))
