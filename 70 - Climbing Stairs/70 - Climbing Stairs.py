class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        a = b = 1
        while n-1:
            a, b = b, a + b
            n -= 1
        return b


x = Solution()
print(x.climbStairs(1))
