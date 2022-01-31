class Solution:
    def targetIndices(
            self, nums: List[int], target: int) -> List[int]:  # 16.49% 90.15%
        start = 0
        end = 0
        for num in nums:
            if num < target:
                start += 1
            if num == target:
                end += 1
        return range(start, start+end)

    def targetIndices_best_speed(
            self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        nums.sort()
        start, end = -1, -1
        while (l <= r):
            m = (l+r)//2
            if (target == nums[m]):
                start = m
                r = m-1
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
        l, r = start, len(nums)-1
        while (l <= r):
            m = (l+r)//2
            if (target == nums[m]):
                end = m
                l = m+1
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
        if start == end == -1:
            return []
        else:
            res = list(range(start, end+1))
            return res

    def targetIndices_2nd_best_speed(
            self, nums: List[int], target: int) -> List[int]:
        l = e = 0
        for n in nums:
            if n < target:
                l += 1
            elif n == target:
                e += 1
        return [i for i in range(l, l + e)]
