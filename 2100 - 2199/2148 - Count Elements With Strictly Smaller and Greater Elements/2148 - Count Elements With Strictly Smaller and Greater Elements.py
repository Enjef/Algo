class Solution:
    def countElements(self, nums: List[int]) -> int:  # 81.57% 98.36%
        n = len(nums)
        n_min = float('inf')
        n_min_count = 0
        n_max = float('-inf')
        n_max_count = 0
        for num in nums:
            if num > n_max:
                n_max_count = 1
                n_max = num
            elif num == n_max:
                n_max_count += 1
            if num < n_min:
                n_min_count = 1
                n_min = num
            elif num == n_min:
                n_min_count += 1
        return n - n_max_count - n_min_count if n_min != n_max else 0

    def countElements_v2(self, nums: List[int]) -> int:  # 69.03% 62.60%
        n = len(nums)
        n_min = min(nums)
        n_min_count = nums.count(n_min)
        n_max = max(nums)
        n_max_count = nums.count(n_max)
        return n - n_max_count - n_min_count if n_min != n_max else 0

    def countElements_best_speed(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        output = 0
        for num in nums:
            if min_num < num < max_num:
                output += 1
        return output

    def countElements_2nd_best_speed(self, nums: List[int]) -> int:
        frequency = {}
        for each in nums:
            frequency[each] = frequency.get(each, 0) + 1
        unique_nums = sorted(frequency.keys())
        if len(unique_nums) < 3:
            return 0
        return sum(v for k, v in frequency.items() if k in unique_nums[1:-1])

    def countElements_3d_best_speed(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        min_occurences = 0
        max_occurences = 0
        for num in nums:  
            if num < min_num:
                min_num = num
                min_occurences = 1
            elif num > max_num:
                max_num = num
                max_occurences = 1
            elif num == min_num:
                min_occurences += 1
            elif num == max_num:
                max_occurences += 1
        return max(0, len(nums) - min_occurences - max_occurences)
