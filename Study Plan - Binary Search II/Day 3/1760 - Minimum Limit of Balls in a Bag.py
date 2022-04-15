class Solution:
    def minimumSize(self, nums, maxOperations):  # 99.25% 38.81%
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right-left)//2
            if sum([(num-1)//mid for num in nums]) > maxOperations:
                left = mid + 1
            else:
                right = mid
        return left
