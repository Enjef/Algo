class Solution:
    def thirdMax(self, nums):
        nums.sort()
        one_max = float('-inf')
        two_max = float('-inf')
        three_max = float('-inf')
        for num in nums:
            if num > three_max:
                one_max, two_max, three_max = two_max, three_max, num
        if one_max == float('-inf'):
            return max(two_max, three_max)
        else:
            return one_max

    def thirdMax_index(self, nums):
        nums = sorted(set(nums))
        return nums[-3] if len(nums) >= 3 else nums[-1]
