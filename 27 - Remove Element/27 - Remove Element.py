class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1 and val == nums[0]:
            return 0
        count = 0
        i, j = 0, len(nums)-1
        while i < j:
            while nums[i] != val:
                i += 1
                if i > len(nums)-1:
                    return len(nums)
            while nums[j] == val:
                count += 1
                j -= 1
                if j < 0:
                    return 0
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        return len(nums) - count


x = Solution()
print(x.removeElement([3,3], 3))
