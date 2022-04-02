class Solution(object):
    def isPerfectSquare(self, num: int) -> bool:  # 39.94% 59.61%
        if num == 1:
            return True
        left = 1
        right = num//2
        while left <= right:
            mid = left + (right-left)//2
            cur = mid * mid
            if cur == num:
                return True
            if cur < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
