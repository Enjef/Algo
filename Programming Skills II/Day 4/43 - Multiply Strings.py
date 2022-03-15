class Solution:
    def multiply(self, num1: str, num2: str) -> str:  # 77.62% 51.62%
        def custom_int(num):
            out = 0
            for char in num:
                out = out * 10 + ord(char) - ord('0')
            return out
        return str(custom_int(num1)*custom_int(num2))
