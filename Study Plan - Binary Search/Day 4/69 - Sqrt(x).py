class Solution:
    def mySqrt(self, x: int) -> int:  # 65.54% 61.69%
        left = 1
        right = x
        while left <= right:
            mid = left + (right-left)//2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
        return right
