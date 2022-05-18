class Solution:
    def pivotIndex(self, nums: List[int]) -> int:  # 27.06% 50.45%
        left = 0
        right = sum(nums)
        for i, num in enumerate(nums):
            left += num
            if left == right:
                return i
            right -= num
        return -1

    def pivotIndex_best_speed(self, nums: List[int]) -> int:
        i, j = 0, sum(nums)
        for idx, x in enumerate(nums):
            j -= x
            if i == j:
                return idx
            i += x
        return -1
