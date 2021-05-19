class Solution:
    def arrangeCoins(self, n: int) -> int:
        level = 0
        while n > 0:
            level += 1
            n -= level
            if n == 0:
                return level
        return level - 1
