class Solution:
    def countOperations(self, num1: int, num2: int) -> int: # 59.58% 97.39%
        out = 0
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            out += 1
        return out

    def countOperations_best_speed(self, num1: int, num2: int) -> int:
        ops = 0
        while num1 != 0 and num2 != 0:
            if num1 == num2:
                ops += 1
                break
            elif num1 < num2:
                ops += (num2 // num1)
                num2 = num2 % num1
            else:
                ops += (num1 // num2)
                num1 = num1 % num2
        return ops

    def countOperations_2nd_best_speed(self, num1: int, num2: int) -> int:
        count = 0
        while num1 and num2:
            if num1 < num2: num1, num2 = num2, num1
            qnt, num1 = divmod(num1,num2)
            count+=qnt
        return count
