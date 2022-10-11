class Solution:
    # 5.29% 50.86% (37.28% 7.37%)
    def smallestEvenMultiple(self, n: int) -> int:
        return n * 2 if n % 2 else n

    def smallestEvenMultiple_best_speed(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2
