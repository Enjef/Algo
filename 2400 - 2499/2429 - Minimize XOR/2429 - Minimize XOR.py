class Solution:
    # 83.92% 33.46%
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1 = bin(num1)[2:]
        num2 = bin(num2)[2:]
        ones = num2.count('1')
        res = ['0']*len(num1)
        for i, char in enumerate(num1):
            if ones:
                if char == '1':
                    res[i] = '1'
                    ones -= 1
        for i in range(len(res)-1, -1, -1):
            if not ones:
                break
            if res[i] == '0':
                res[i] = '1'
                ones -= 1
        if ones:
            res = ['1']*ones + res
        return int(''.join(res), 2)
