class Solution:
    def totalMoney(self, n: int) -> int:  # 5.95% 71.21%
        bank = 0
        day = 0
        cur = 1
        for i in range(n):
            bank += cur + day
            day += 1
            if day == 7:
                day = 0
                cur += 1
        return bank

    def totalMoney_best_speed(self, n: int) -> int:
        return (
            n//7 * 28 +
            sum(range(n//7))*7 +
            sum(range(n//7+1, n % 7 + n//7 + 1))
        )
