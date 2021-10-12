class Solution:  # 6.84%  69.49%
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mark = float('inf')
        for i in range(len(nums)):
            if nums[i] != target:
                nums[i] = mark
                mark += 1
                continue
            if nums[i] == target:
                nums[i] = 0
                mark = 1
                continue
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != 0:
                nums[i] = min(mark, nums[i])
                mark += 1
                continue
            if nums[i] == 0:
                mark = 1
                continue
        return nums[start]

    def getMinDist(self, nums: List[int], target: int, start: int) -> int:
        ans = 1001
        for i in range(len(nums)):
            if nums[i] == target:
                ans = min(ans, abs(i - start))
        return ans
