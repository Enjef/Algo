# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:  # 44.07% 69.37%
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right-left)//2
            res = guess(mid)
            if not res:
                return mid
            if res == 1:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def guessNumber_best_speed(self, n: int) -> int:
        low = 1
        high = n
        answer = 2
        while low <= high:
            mid = low + (high - low) // 2
            answer = guess(mid)
            if answer == 0:
                return mid
            elif answer == 1:
                low = mid + 1
            elif answer == -1:
                high = mid - 1
