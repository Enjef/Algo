class Solution:
    # 37.55% 67.29% (76.86% 16.22%)
    def longestSubarray(self, nums: List[int]) -> int:
        x_max = max(nums)
        i, n = 0, len(nums)
        res = 1
        while i < n:
            cur = 1
            while i < n and nums[i] == x_max:
                cur += 1
                i += 1
            res = max(res, cur-1)
            i += 1
        return res

    def longestSubarray_best_speed(self, nums: List[int]) -> int:
        max_ = max(nums)
        res = 0
        for k, grp in itertools.groupby(nums):
            if k == max_:
                res = max(res, len(list(grp)))
        return res

    def longestSubarray_2nd_best_speed(self, nums: List[int]) -> int:
        n = len(nums)
        maxx = max(nums)
        count = 0
        max_count = 0
        for i in range(0, n):
            if nums[i] == maxx:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0
        if count > max_count:
            max_count = count
        return max_count

    def longestSubarray_best_memory(self, nums: List[int]) -> int:
        ans = 0
        maxIndex = 0
        sameNumLength = 0
        for i, num in enumerate(nums):
            if nums[i] == nums[maxIndex]:
                sameNumLength += 1
                ans = max(ans, sameNumLength)
            elif nums[i] > nums[maxIndex]:
                maxIndex = i
                sameNumLength = 1
                ans = 1
            else:
                sameNumLength = 0
        return ans
