class Solution:
    def addDigits(self, num):
        if num == 0:
            return 0
        if num < 10:
            return num
        while num > 9:
            num = sum([int(x) for x in list(str(num))])
        return num
