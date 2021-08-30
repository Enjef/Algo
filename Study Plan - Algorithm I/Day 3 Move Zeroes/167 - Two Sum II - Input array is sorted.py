class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x_map = {}
        for i, num in enumerate(numbers):
            if target - num not in x_map:
                x_map[num] = i
            else:
                return [x_map[target - num] + 1, i + 1]
