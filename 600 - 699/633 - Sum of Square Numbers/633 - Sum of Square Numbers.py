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

    def judgeSquareSum_2nd_best_speed(self, c: int) -> bool:
        for i in range(2, int(math.sqrt(c)) + 1):
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c //= i
                if i % 4 == 3 and count % 2 != 0:
                    return False
        return c % 4 != 3

    def judgeSquareSum_best_memory(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            if l*l + r*r < c:
                l += 1
            elif l*l + r*r > c:
                r -= 1
            else:
                return True
        return False
