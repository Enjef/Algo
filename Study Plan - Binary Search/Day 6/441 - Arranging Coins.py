class Solution:
    def arrangeCoins(self, n: int) -> int:  # 71.66% 60.45%
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
