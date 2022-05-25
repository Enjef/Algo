class Solution:
    def divisorGame(self, n: int) -> bool:  # 53.51% 56.59%
        return not n % 2

    def divisorGame_best_speed(self, n: int) -> bool:
        return n % 2 == 0

    def divisorGame_best_memory(self, n: int) -> bool:
        return (n & 1) == 0
