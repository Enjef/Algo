class Solution:
    def smallestDivisor(self, nums, threshold):  # 83.30% 71.26%
        left, right = 1, 10**6
        while left <= right:
            mid = left + (right-left)//2
            if sum([ceil(num/mid) for num in nums]) <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def smallestDivisor_v2(self, nums, threshold):  # 49.17% 97.92%
        left, right = 1, 10**6
        while left < right:
            mid = left + (right-left)//2
            if sum([-num/mid//1*-1 for num in nums]) > threshold:
                left = mid + 1
            else:
                right = mid
        return right
