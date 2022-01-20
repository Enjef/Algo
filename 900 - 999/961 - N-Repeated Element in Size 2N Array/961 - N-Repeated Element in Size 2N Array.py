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

    def repeatedNTimes_mock(self, nums: List[int]) -> int:  # 41.77% 54.64%
        n = len(nums)//2
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return [x for x, val in count.items() if val == n][0]

    def repeatedNTimes_best(self, nums: List[int]) -> int:
        di = set()
        for i in nums:
            if i in di:
                return i
            else:
                di.add(i)
