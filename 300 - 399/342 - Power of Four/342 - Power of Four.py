class Solution:
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n > 1:
            if n % 4 != 0:
                return False
            n //= 4
        return True
