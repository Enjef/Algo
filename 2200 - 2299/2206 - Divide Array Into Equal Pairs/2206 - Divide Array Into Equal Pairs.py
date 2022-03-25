class Solution:
    def divideArray(self, nums: List[int]) -> bool:  # 52.37% 22.83%
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        for key in counter:
            if counter[key] % 2:
                return False
        return True

    def divideArray_best_speed(self, nums: List[int]) -> bool:
        d = collections.defaultdict(int)
        for n in nums:
            if d[n]:
                d[n] -= 1
            else:
                d[n] = 1
        for k, v in d.items():
            if v:
                return False
        return True

    def divideArray_best_memory(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0)+1
        for key in d.keys():
            if d[key] % 2 != 0:
                return False
        return True
