class Solution:
    def dominantIndex(self, nums: List[int]) -> int:  # 62.23% 61.87%
        idx = -1
        first, second = float('-inf'), float('-inf') 
        for i, num in enumerate(nums):
            if num > first:
                if second < first:
                    second = first
                first = num
                idx = i
            elif num > second:
                second = num
        if second == float('-inf') or second*2 <= first:
            return idx
        return -1

    def dominantIndex_best_speed(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        a = max(nums)
        b = [i for i in nums]
        b.remove(a)
        for i in b:
            if (i*2) > a:
                return -1
        return nums.index(a)
