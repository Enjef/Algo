class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
        return len(nums)


x = Solution()
print(x.searchInsert([1,3,5,6], 0))
