class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:  # 13.20% 12.55%
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        return [x for x in counter if counter.get(x) == 2]

    def findDuplicates_v2(self, nums: List[int]) -> List[int]:  # 50.93% 5.47%
        first = set()
        res = set()
        for num in nums:
            if num not in first:
                first.add(num)
            else:
                res.add(num)
        return res

    def findDuplicates_v3(self, nums: List[int]) -> List[int]:  # 98.85% 5.47%
        first = set()
        res = []
        for num in nums:
            if num not in first:
                first.add(num)
            else:
                res.append(num)
        return res

    def findDuplicates_best_speed(self, nums: List[int]) -> List[int]:
        dict = collections.defaultdict()
        res = []
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                res.append(num)
        return res
