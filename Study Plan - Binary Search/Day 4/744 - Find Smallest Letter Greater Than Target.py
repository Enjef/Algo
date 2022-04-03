class Solution:
    def nextGreatestLetter(self, letters, target):  # 83.00% 24.34%
        n = len(letters)
        left = 0
        right = n-1
        while left < right:
            mid = left + (right-left)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        if left == n-1 and letters[left] <= target:
            return letters[0]
        return letters[right]
