class Solution:
    def majorityElement(self, nums):  # 90.81% 73.11%
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement_ds_2(self, nums: List[int]) -> int:  # 34.34% 54.34%
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count.get(num, 0) > n // 2:
                return num

    def majorityElement_best_speed(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement_2nd_best_speed(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for n in nums:
            if count == 0:
                res = n
            count += 1 if res == n else -1
        return res
