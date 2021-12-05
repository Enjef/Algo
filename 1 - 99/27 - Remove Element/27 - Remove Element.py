class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:  # 78.64% 48.89%
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return i

    def removeElement_mock(
            self,
            nums: List[int],
            val: int) -> int:  # 53.12% 48.89%
        nums[:] = [x for x in nums if x != val]
        return len(nums)

    def removeElement_best_speed(self, nums: List[int], val: int) -> int:
        start = 0
        for i in range(len(nums)):
            if nums[start] == val:
                nums.pop(start)
            else:
                start += 1
        return len(nums)
