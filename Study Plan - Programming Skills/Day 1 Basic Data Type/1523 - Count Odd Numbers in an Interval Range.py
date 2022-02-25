class Solution:
    def countOdds(self, low: int, high: int) -> int: # 38.21% 84.12%
        return (high-low-int(not(low%2)))//2+1


def even(n):
    return n % 2 == 0

class Solution_best_speed:
    def countOdds(self, low: int, high: int) -> int:
        n_interval = high - low - 1
        cnt = 0
        cnt = cnt + 1 if not even(high) else cnt
        cnt = cnt + 1 if not even(low) else cnt
        if n_interval != 0:
            if even(low) and even(high):
                cnt += n_interval // 2 + 1
            else:
                cnt += (n_interval // 2)
        return cnt


class Solution_2nd_best_speed:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


class Solution_3nd_best_speed:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0 and high % 2 == 0:
           return (high - low) // 2 
        else:
           return ((high - low) // 2) + 1
