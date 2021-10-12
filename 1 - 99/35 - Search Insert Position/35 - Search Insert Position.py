class Solution:
    # 1
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
        return len(nums)

    # 2
    def searchInsert_bin(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left


x = Solution()
print(x.searchInsert_bin([1,3,5,6], 7))
