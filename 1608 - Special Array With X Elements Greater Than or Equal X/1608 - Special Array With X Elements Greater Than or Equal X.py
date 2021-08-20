class Solution:
    def specialArray(self, nums: List[int]) -> int:  # 24.51% 18.68%
        nums.sort()
        for i in range(1, max(nums)+1):
            if i == len([el for el in nums if el >= i]):
                return i
        return -1

    def specialArray_best_speed(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and i == nums[i] else i

    def specialArray_best_memory(self, nums: List[int]) -> int:
        for i in range(len(nums), -1, -1):
            n = 0
            for a in nums:
                if a >= i:
                    n += 1
            if n == i:
                return n
        else:
            return -1
