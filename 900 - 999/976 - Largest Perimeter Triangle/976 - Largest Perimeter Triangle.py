class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:  # 42.10%  87.93%
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

    def largestPerimeter_best_speed(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

    def largestPerimeter_best_memory(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        for a, b, c in zip(nums, nums[1:], nums[2:]):
            if b + c > a:
                return a + b + c
        return 0
