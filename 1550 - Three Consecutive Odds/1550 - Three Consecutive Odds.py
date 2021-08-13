class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:  # 51.63% 55.18%
        out = 0
        for num in arr:
            if num % 2 != 0:
                out += 1
            else:
                out = 0
            if out == 3:
                return True
        return False

    def threeConsecutiveOdds_best_speed(self, arr: List[int]) -> bool:
        return any(
            len(t) == 3 and t[0] % 2 == 1 and t[1] % 2 == 1 and
            t[2] % 2 == 1 for t in zip(arr, arr[1:], arr[2:])
        )
