class Solution:
    def maximumProduct(self, nums) -> int:  # 38.30% 44.54%
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        first_min = second_min = float('inf')
        third_max = second_max = first_max = float('-inf')
        for num in nums:
            if num > first_max:
                third_max, second_max, first_max = second_max, first_max, num
            elif num > second_max:
                third_max, second_max = second_max, num
            elif num > third_max:
                third_max = num
            if num < first_min:
                first_min, second_min = num, first_min
            elif num < second_min:
                second_min = num
        return max(
            first_min*second_min*first_max, third_max*second_max*first_max)

    def maximumProduct_best_speed(self, nums: List[int]) -> int:
        nums.sort()
        return max(
            nums[-1]*nums[-2]*nums[-3],
            nums[0]*nums[1]*nums[-1]
        )
