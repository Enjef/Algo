class Solution:
    def isPowerOfTwo(self, n: int) -> bool:  # 24.16% 67.37%
        if n == 0:
            return False
        while n % 2 == 0:
            n //= 2
        if n == 1:
            return True
        return False

    def isPowerOfTwo_bin(self, n: int) -> bool:  # 33.41% 38.86%
        return n >= 1 and (n == 1 or bin(n)[2:].count('1') == 1)
