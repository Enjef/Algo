class Solution:
    def findDisappearedNumbers(
            self,
            nums: List[int]) -> List[int]:  # 94.07% 35.84%
        full = [x for x in range(1, len(nums)+1)]
        nums = set(nums)
        out = []
        for i in full:
            if i not in nums:
                out.append(i)
        return out

    def findDisappearedNumbers_mock(
        self,
        nums: List[int]) -> List[int]:  # 96.85% 26.94%
        n = len(nums)
        nums = set(nums)
        return [x for x in range(1, n+1) if x not in nums]

    def findDisappearedNumbers_best_memory(self, nums: list[int]) -> list[int]:
        for n in nums:
            nums[abs(n) - 1] = -1 * abs(nums[abs(n) - 1])
        j = 0
        for i, n in enumerate(nums):
            if nums[i] > 0:
                nums[j] = i + 1
                j += 1
        del nums[j:]
        return nums
