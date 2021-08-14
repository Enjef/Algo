class Solution:
    def findLucky_dict(self, arr: List[int]) -> int:  # 11.62% 45.10%
        num_map = {}
        for num in arr:
            num_map[num] = num_map.get(num, 0) + 1
        x_max = -1
        for key, value in num_map.items():
            if key > x_max and key == value:
                x_max = key
        return x_max

    def findLucky_max_variant(self, arr: List[int]) -> int:  # 17.77% 75.63%
        num_map = {}
        for num in arr:
            num_map[num] = num_map.get(num, 0) + 1
        x_max = -1
        for key, value in num_map.items():
            if key == value:
                x_max = max(x_max, key)
        return x_max

    def findLucky_set(self, arr: List[int]) -> int:  # 35.88% 45.10%
        num_set = set(arr)
        x_max = -1
        for num in num_set:
            if num == arr.count(num):
                x_max = max(x_max, num)
        return x_max
