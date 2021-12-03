class Solution:
    def addStrings(self, num1: str, num2: str) -> str:  # 45.44% 95.74%
        def custom_int(num):
            res = 0
            for char in num:
                res = res * 10 + ord(char) - ord('0')
            return res
        return str(custom_int(num1) + custom_int(num2))
