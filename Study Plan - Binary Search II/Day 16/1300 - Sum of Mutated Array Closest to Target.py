class Solution:
    def findBestValue(self, arr, target):  # 37.43% 12.30%
        left, right = 0, max(arr)
        while left < right:
            mid = (left+right+1)//2
            cur = sum([mid if num > mid else num for num in arr])
            if cur <= target:
                left = mid
            else:
                right = mid - 1
        if (
            target - sum([left if num > left else num for num in arr]) <=
            abs(sum([left+1 if num > left+1 else num for num in arr]) - target)):
            return left
        return left + 1
