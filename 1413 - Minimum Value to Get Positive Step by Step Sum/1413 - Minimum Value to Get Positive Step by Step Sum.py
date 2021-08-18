class Solution:
    def minStartValue(self, nums: List[int]) -> int:  # 65.79% 10.58%
        cur = 0
        minx = 0
        for i in nums:
            cur += i
            minx = min(minx, cur)
        if minx < 1:
            return abs(minx) + 1
        return 1

    def minStartValue_best_speed(self, nums: List[int]) -> int:
        my_sum = 0
        my_min = 0
        firstnegative = 0
        if nums[0] < 1:
            firstnegative = abs(nums[0])+1
        for i in range(1, len(nums)):
            if nums[i-1] + nums[i] < 1:
                my_sum = 0
                my_sum += nums[i-1]+nums[i]
                if my_min > my_sum:
                    my_min = my_sum
            nums[i] = nums[i] + nums[i-1]
        num = abs(my_min)
        if nums[0] < 0 and my_min == 0:
            return abs(nums[0]) + 1
        if firstnegative > num+1:
            return firstnegative
        return num+1
