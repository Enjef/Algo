class Solution:
    def mySqrt(self, x: int) -> int:  # 97.16% 13.08%
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid*mid == x:
                return mid
            if mid*mid < x:
                left = mid + 1
            else:
                right = mid - 1
        if mid*mid > x:
            return mid - 1
        return mid

    def mySqrt_study_plan_version(self, x: int) -> int:  # 65.54% 61.69%
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

    def mySqrt_best_speed_binary(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            squere = mid * mid
            if squere == x:
                return mid
            if squere > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
