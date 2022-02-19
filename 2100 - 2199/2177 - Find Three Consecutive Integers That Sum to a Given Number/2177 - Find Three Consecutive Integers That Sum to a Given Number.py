class Solution:
    def sumOfThree(self, num: int) -> List[int]: # fresh problem 75.00% 100.00%
        out = []
        if num%3:
            return out
        left = -1
        right = num // 2
        while left <= right:
            mid = left + (right - left)//2
            cur = 3*mid+3
            if cur == num:
                return mid, mid+1, mid+2
            if cur > num:
                right = mid - 1
            else:
                left = mid + 1
        return out

    def sumOfThree_best_speed(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        return [num // 3 - 1, num//3, num//3 + 1]
    