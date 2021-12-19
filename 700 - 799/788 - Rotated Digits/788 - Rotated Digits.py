class Solution:
    def rotatedDigits(self, n: int) -> int:  # 77.76% 53.68%
        cont = '018'
        rotate = '2569'
        out = 0
        for num in range(2, n+1):
            flag = False
            for digit in str(num):
                if digit in cont:
                    continue
                if digit not in rotate:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                out += 1
        return out

    def rotatedDigits_mock(self, n: int) -> int:  # 56.71% 55.92%
        good = {'0':'0', '1':'1', '2':'5', '5':'2', '6':'9', '8':'8', '9':'6'}
        bad = {'3', '4', '7'}
        out = 0
        for num in range(1, n+1):
            cur = str(num)
            if set(cur) & bad:
                continue
            if cur == ''.join([good[x] for x in cur]):
                continue
            out += 1
        return out

    def rotatedDigits_best_memory(self, n: int) -> int:
        # 0 -> invalid, 1 -> same number 2 -> mirror
        d = [1, 1, 2, 0, 0, 2, 2, 0, 1, 2]
        res = 0
        for i in range(1, n+1):
            num = i
            sum = 1
            # if number is valid, i should either
            # have digists pointing to 1 or 2 or both
            while num:
                sum *= d[int(num % 10)]
                num /= 10
            if sum >= 2:
                res += 1
        return res

    def rotatedDigits_best_speed(self, n: int) -> int:
        digitstr = str(n)
        length = len(digitstr)
        found_non_self_rotate_number = False
        res = 0
        for i, digit in enumerate(digitstr):
            digit = int(digit)
            for num in range(digit):
                if num in (2, 5, 6, 9) or (
                        found_non_self_rotate_number and num in (0, 1, 8)):
                    res += self.numOfGoodIntegerHelper(length-i-1)[0]
                elif num in (0, 1, 8):
                    res += self.numOfGoodIntegerHelper(length-i-1)[1]
            if digit in (2, 5, 6, 9):
                found_non_self_rotate_number = True
            elif digit in (3, 4, 7):
                break
        if self.isValidAndDifferent(digitstr):
            res += 1
        return res

    def isValidAndDifferent(self, digitstr):
        return (
            len(set(list(digitstr)) - set(
                ['2', '5', '6', '9', '0', '1', '8'])) == 0 and
            len(set(list(digitstr)) - set(['0', '1', '8'])) > 0
        )

    def numOfGoodIntegerHelper(self, number_length):
        if number_length == 0:  # important
            return 1, 0         # important
        return 7**number_length, 7**number_length-3**number_length
