class Solution:
    def findDuplicate(self, nums: List[int]) -> int:  # 36.37% 61.27%
        left, right = 1, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if sum([num <= mid for num in nums]) > mid:
                duplicate = mid
                right = mid - 1
            else:
                left = mid + 1
        return duplicate
