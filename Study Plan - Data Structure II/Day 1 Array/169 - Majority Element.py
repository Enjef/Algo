class Solution:
    def majorityElement(self, nums: List[int]) -> int:  # 34.34% 54.34%
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count.get(num, 0) > n // 2:
                return num
