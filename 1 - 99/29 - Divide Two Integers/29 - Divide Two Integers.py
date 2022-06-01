class Solution:
    def divide(self, dividend: int, divisor: int) -> int:  # 43.36% 76.13%
        out = 0
        sign = 1
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            cur = divisor
            acc = 1
            while dividend > (cur+cur):
                cur += cur
                acc += acc
            dividend -= cur
            out += acc
        if sign*out > 2**31 - 1:
            return sign*(2**31 - 1)
        return sign*out

    def divide_best_speed(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31-1
        INT_MIN = -2 ** 31
        INT_MIN_HALF = INT_MIN // 2
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        negative = 2
        if dividend > 0:
            negative -= 1
            dividend = -dividend
        if divisor > 0:
            negative -= 1
            divisor = -divisor
        doubles = []
        i = 1
        while dividend <= divisor:
            doubles.append((divisor, i))
            if divisor < INT_MIN_HALF:
                break
            divisor += divisor
            i += i
        res = 0
        for i in range(len(doubles)-1, -1, -1):
            if dividend <= doubles[i][0]:
                dividend -= doubles[i][0]
                res += doubles[i][1]
        return -res if negative == 1 else res

    def divide_best_memory(self, dividend: int, divisor: int) -> int:
        flag = False
        if (dividend ^ divisor) < 0:
            flag = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        residual = dividend
        re = 0
        temp_d = 0
        temp = 0
        while (divisor) <= residual:
            re += temp
            temp = 1
            residual -= temp_d
            temp_d = divisor
            while (temp_d << 1) <= residual:
                temp <<= 1
                temp_d <<= 1
        if flag:
            return -re
        else:
            if 2147483648 == re:
                return 2147483647
            else:
                return re
