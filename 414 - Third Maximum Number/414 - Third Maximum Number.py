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
