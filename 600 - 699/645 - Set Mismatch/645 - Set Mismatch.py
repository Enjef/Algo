class Solution:
    # 18.55% 55.86% (28.48% 41.20%)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sum_set_nums = sum(set(nums))
        dubble = sum(nums) - sum_set_nums
        n = len(nums)
        sum_n = (n + 1) * n / 2
        target = int(sum_n) - sum_set_nums
        return [dubble, target]

    # 24.22% 60.69%
    def findErrorNums_daily(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = [None, None]
        for num in range(1, len(nums)+1):
            if count[num] == 2:
                res[0] = num
            if num not in count:
                res[1] = num
        return res

    # 99.89% 60.69%
    def findErrorNums_daily_v2(self, nums: List[int]) -> List[int]:
        total = sum(range(1, len(nums)+1))
        raw = sum(nums)
        double = raw - sum(set(nums))
        missing = total + double - raw
        return [double, missing]


class Solution_best_speed:
    def findErrorNums_2nd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        range_sum = n*(n+1)//2
        actual_sum = sum(nums)
        set_sum = sum(set(nums))
        return [actual_sum - set_sum, range_sum - set_sum]

    def findErrorNums_3d(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), int(len(nums)*(len(nums)+1)/2 - sum(set(nums)))]


class Solution_best_memory:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        orig = range(1, len(nums)+1)
        duplicate = None
        for num in orig:
            try:
                nums.remove(num)
            except ValueError:
                duplicate = num
        return [nums[0], duplicate]
