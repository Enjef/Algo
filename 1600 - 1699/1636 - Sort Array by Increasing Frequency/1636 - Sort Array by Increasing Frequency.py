class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:  # 60.20% 58.14%
        map_n = {}
        for num in nums:
            map_n[num] = map_n.get(num, 0) + 1
        arr = [[key]*map_n[key] for key in map_n]
        arr.sort(reverse=True)
        arr.sort(key=len)
        return [item for tup in arr for item in tup]

    def frequencySort_best(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return sorted(nums, key=lambda x: (counts[x], -x))
