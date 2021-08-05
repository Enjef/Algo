class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:  # 27.19% 14.85%
        n = len(nums) // 2
        n_map = {}
        for num in nums:
            if num not in n_map:
                n_map[num] = 0
            n_map[num] += 1
            if n_map[num] == n:
                return num
        return num

    def repeatedNTimes_best(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                return i
