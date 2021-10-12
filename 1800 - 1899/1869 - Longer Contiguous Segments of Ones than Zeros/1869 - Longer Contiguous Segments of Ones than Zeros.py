class Solution:
    def checkZeroOnes(self, s: str) -> bool:  # 30.65% 30.65%
        zero_max = 0
        one_max = 0
        cur_zero = 0
        cur_one = 0
        for i in s:
            if i == '1':
                cur_one += 1
                zero_max = max(zero_max, cur_zero)
                cur_zero = 0
            else:
                cur_zero += 1
                one_max = max(one_max, cur_one)
                cur_one = 0
        zero_max = max(zero_max, cur_zero)
        one_max = max(one_max, cur_one)
        return one_max > zero_max
