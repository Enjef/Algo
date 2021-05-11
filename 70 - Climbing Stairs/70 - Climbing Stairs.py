class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 1
        else:
            return self.climbStairs(n-2) + self.climbStairs(n-1)


x = Solution()
print(x.climbStairs(1))
