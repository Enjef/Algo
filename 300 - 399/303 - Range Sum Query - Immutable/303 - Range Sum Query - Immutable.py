class NumArray:

    def __init__(self, nums):  # 41.95% 88.94%
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return sum(self.nums[left: right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


class NumArray_best_speed:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        for num in nums:
            self.sums += self.sums[-1] + num,

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
