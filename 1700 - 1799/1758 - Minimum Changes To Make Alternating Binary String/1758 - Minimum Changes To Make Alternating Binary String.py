class Solution:
    def minOperations(self, s: str) -> int:  # 92.59% 94.86%
        odd = 0
        even = 0
        n = len(s)
        for i, dig in enumerate(s):
            if i % 2 == 0 and dig == '1':
                even += 1
            if i % 2 != 0 and dig == '0':
                odd += 1
        shift = n - even - odd
        return min(odd+even, shift)

    def minOperations_best_speed(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        a, b = '0', '1'
        c1, c2 = 0, 0
        for c in s:
            if c != a:
                c1 += 1
            if c != b:
                c2 += 1
            a, b = b, a
        return min(c1, c2)

    def minOperations_2nd_best_speed(self, s: str) -> int:
        res_1 = 0
        res_2 = 0
        for i in range(1,len(s),2):
            if s[i] == '0':
                res_1 += 1
            else:
                res_2 += 1
        for i in range(0,len(s),2):
            if s[i] == '1':
                res_1 += 1
            else:
                res_2 += 1                
        return min(res_1, res_2)

    def minOperations_3rd_best_speed(self, s: str) -> int:
        num_of_zeros = 0 
        num_of_ones = 0 
        curr = '1'
        for ch in s: 
            if ch == curr: 
                num_of_zeros += 1
            else: 
                num_of_ones += 1
            curr = '1' if curr == '0' else '0'    
        return min(num_of_ones, num_of_zeros)
