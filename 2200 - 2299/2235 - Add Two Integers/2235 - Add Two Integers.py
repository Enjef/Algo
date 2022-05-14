class Solution:
    def sum(self, num1: int, num2: int) -> int:  # 5.05% 95.60%
        cur = float('inf')
        while num1 + num2 != cur:
            cur = randrange(-200, 201)
        return cur
