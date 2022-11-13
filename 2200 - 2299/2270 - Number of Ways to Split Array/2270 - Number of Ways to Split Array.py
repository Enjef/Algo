class Solution:
    # 15.4% 78.24% (81.44% 56.16%)
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        left = nums[0]
        right = sum(nums[1:])
        res = int(left >= right)
        for i in range(1, n-1):
            left += nums[i]
            right -= nums[i]
            res += int(left >= right)
        return res


class Solution_best_speed:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total = sum(nums)
        return sum(2 * running_sum >= total for running_sum in islice(accumulate(nums), len(nums)-1))

    def waysToSplitArray_2nd(self, nums: List[int]) -> int:
        n = len(nums)
        rightSum = sum(nums)
        leftSum = 0
        ans = 0
        for i in range(n-1):
            leftSum += nums[i]
            rightSum -= nums[i]
            if leftSum >= rightSum:
                ans += 1
        return ans


class Solution_best_memory:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pref = list(itertools.accumulate(nums))
        return sum(i >= pref[-1]-i for i in pref[:-1])
