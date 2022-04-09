class Solution:
    def judgeSquareSum(self, c: int) -> bool:  # 6.97% 69.57%
        if c < 3:
            return True
        for i in range(int(c**0.5)+1):
            left, right = 0, int(c**0.5)
            while left <= right:
                mid = left + (right-left)//2
                cur = i*i+mid*mid
                if cur == c:
                    return True
                if cur < c:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
