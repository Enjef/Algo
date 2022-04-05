class Solution:
    def arrangeCoins(self, n: int) -> int:  # 30.30% 5.00%
        level = 0
        while n > 0:
            level += 1
            n -= level
            if n == 0:
                return level
        return level - 1

    def arrangeCoins_study_plan(self, n: int) -> int:  # 71.66% 60.45%
        left = 0
        right = n
        while left <= right:
            mid = left + (right-left)//2
            mid_row_sum = mid*(mid+1)//2
            if mid_row_sum == n:
                return mid
            if mid_row_sum < n:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    def arrangeCoins_best_speed(self, n: int) -> int:
        return int((2 * n + 0.25)**0.5 - 0.5)

    def arrangeCoins_2nd_best_speed(self, n: int) -> int:
        res = 0
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            coins = (m / 2) * (m + 1)
            if coins == n:
                return m
            elif coins > n:
                r = m - 1
            else:
                l = m + 1
                res = max(res, m)
        return res
