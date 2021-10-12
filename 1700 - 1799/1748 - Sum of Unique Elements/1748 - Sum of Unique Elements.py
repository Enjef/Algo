class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:  # 54.58% 90.37%
        x_map = {}
        for num in nums:
            if num not in x_map:
                x_map[num] = 0
            x_map[num] += 1
        return sum([key for key, value in x_map.items() if value == 1 ])
