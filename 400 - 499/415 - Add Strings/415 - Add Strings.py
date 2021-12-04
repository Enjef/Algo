class Solution:
    def addStrings(self, num1: str, num2: str) -> str:  # 33.31% 66.91%
        def custom_int(num):
            res = 0
            for char in num:
                res = res * 10 + ord(char) - ord('0')
            return res
        return str(custom_int(num1)+custom_int(num2))

    def addStrings_best_memory(self, num1: str, num2: str) -> str:
        ptr1 = len(num1) - 1
        ptr2 = len(num2) - 1
        res = []
        carry = 0
        while ptr1 >= 0 or ptr2 >= 0 or carry > 0: 
            n1 = 0 if ptr1 < 0 else int(num1[ptr1])
            n2 = 0 if ptr2 < 0 else int(num2[ptr2])
            sumNum = n1 + n2 + carry
            carry, div = divmod(sumNum, 10)
            res.append(div)
            ptr1 -= 1
            ptr2 -= 1
        ans = ""
        for val in res[::-1]:
            ans += str(val)
        return ans
