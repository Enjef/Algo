class Solution:
    def minSubArrayLen_st_plan_bin_search(self, target, nums):  # 14.98% 53.81%
        n = len(nums)
        if n == 1:
            return int(nums[0] >= target)
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        if nums[-1] < target:
            return 0
        out = n+1
        for i in range(n):
            left, right = i, n-1
            if nums[i] >= target:
                out = min(out, i+1)
            while left < right:
                mid = left + (right-left)//2
                cur = nums[mid]-nums[i]
                if cur >= target:
                    right = mid
                else:
                    left = mid + 1
            if nums[left]-nums[i] >= target:
                out = min(out, left-i)
        if out == n+1 and nums[-1] == target:
            out = n
        return out if out != n+1 else 0

    def minSubArrayLen_best_speed(self, target: int, nums: List[int]) -> int:
        const = 100001
        result = const
        start_id = 0
        value = 0
        for end_id in range(len(nums)):
            value += nums[end_id]
            if value >= target:
                while value >= target:
                    value -= nums[start_id]
                    start_id += 1
                result = min(result, end_id - start_id + 1 + 1)
        return result if result < const else 0

    def minSubArrayLen_2nd_best_speed(self, target: int, nums: List[int]):
        currSum = nums[0]
        length = inf
        left = 0
        right = 1
        while True:
            if target <= currSum:
                length = min(length, right - left)
            if right == len(nums):
                if currSum < target:
                    break
                elif currSum == target:
                    length = min(length, right - left)
                    break
            if currSum <= target:
                currSum += nums[right]
                right += 1
            else:
                currSum -= nums[left]
                left += 1
        return length if length != inf else 0

    def minSubArrayLen_best_memory(self, target: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        shortest = len(nums) + 1
        j = 0
        for i in range(len(nums)):
            while sum(nums[j+1:i+1]) >= target:
                j += 1
            if (i - j + 1) < shortest and sum(nums[j:i+1]) >= target:
                shortest = (i - j + 1)
        return shortest if shortest < len(nums) + 1 else 0
