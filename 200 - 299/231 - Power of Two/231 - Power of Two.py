class Solution(object):
    def isPowerOfTwo(self, n):  # 64.15% 89.71%
        """
        :type n: int
        :rtype: bool
        """
        while n >= 1:
            if n == 1:
                return True
            if n % 2 != 0:
                return False
            n //= 2

    def isPowerOfTwo_best_speed(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 0
        while 2 ** x <= n:
            if 2 ** x == n:
                return True
            x += 1
        return False

    def isPowerOfTwo_2nd_best_speed(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 or n < 0:
            return False
        return n & (n - 1) == 0

    def isPowerOfTwo_best_speed_v2(self, n: int) -> bool:
        # recursion
        # base case
        if n == 0:
            return False
        if n==1 or n == 2:
            return True
        if n % 2 != 0:
            return False
        
        return self.isPowerOfTwo(n//2)

    def isPowerOfTwo_2nd_best_speed_v2(self, n: int) -> bool:
        x = 1
        while x < n:
            x *= 2
        return True if x == n else False

    def isPowerOfTwo_mock(self, n: int) -> bool:  # 89.60% 0%
        if n <= 0:
            return False
        while n > 2:
            if n % 2 != 0:
                return False
            n //= 2
        return True
