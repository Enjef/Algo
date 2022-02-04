class Solution:
    def isSameAfterReversals(self, num: int) -> bool:  # 10.38% 97.29%
        reversed1 = int(''.join(reversed(str(num))))
        reversed2 = int(''.join(reversed(str(reversed1))))
        return num == reversed2

    def isSameAfterReversals_best_speed(self, num: int) -> bool:
        return not num or num % 10 != 0

    def isSameAfterReversals_2nd_best_speed(self, num: int) -> bool:
        if num < 10:
            return True
        temp = num
        while temp != 0:
            temp, dig = divmod(temp, 10)
            if temp == num//10 and dig == 0:
                return False
            else:
                return True
