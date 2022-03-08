class NumArray:

    def __init__(self, nums: List[int]):  # 38.04% 73.08%
        self.nums = nums
        self.total = sum(nums)

    def sumRange(self, left: int, right: int) -> int:
        if (right-left)<(len(self.nums)//2):
            return sum(self.nums[left:right+1])
        return self.total - sum(self.nums[:left]) - sum(self.nums[right+1:])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
