class Solution:
    def check(self, nums: List[int]) -> bool:  # 9.05% 62.59%
        n = len(nums)
        min_num = min(nums)
        if nums[0] == nums[-1] == min_num:
            i = -1
            while i > -n and nums[i] == min_num:
                i -= 1
            idx = i+1
        else:
            idx = nums.index(min_num)
        return nums[idx:]+nums[:idx] == sorted(nums)

    def check_best_speed(self, nums: List[int]) -> bool:
        count_decrease = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count_decrease += 1
                if count_decrease > 1:
                    return False
        return True

    def check_2nd_best_speed(self, nums: List[int]) -> bool:
        k = len(nums) - 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                k = i
        k += 1
        temp = nums[:k]
        nums = nums[k:]
        nums = nums + temp
        return nums == sorted(nums)

    def check_3d_best_speed(self, nums: List[int]) -> bool:
        n_decreases = 0
        prev = None
        for elem in nums:
            if prev and elem < prev:
                n_decreases += 1
            prev = elem
        if n_decreases == 0:
            return True
        if n_decreases > 1:
            return False
        return True if nums[-1] <= nums[0] else False

    def check_4th_best_speed(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True
        i = 1
        while nums[i-1] <= nums[i]:
            i += 1
        return nums[i:]+nums[:i] == sorted(nums)

    def check_best_memory(self, nums: List[int]) -> bool:
        count = 0
        for i in range(0, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
        return count <= 1
