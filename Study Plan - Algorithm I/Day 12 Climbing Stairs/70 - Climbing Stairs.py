class Solution:
    def climbStairs(self, n: int) -> int:  # 14.44% 42.81%
        prev = 0
        cur = 1
        while n:
            prev, cur = cur, cur + prev
            n -= 1
        return cur
