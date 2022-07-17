class Solution:
    # 53.85% 61.54%
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = 0
        odds = 0
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        for num, amt in count.items():
            pairs += amt // 2
            odds += int(amt % 2 != 0)
        return [pairs, odds]

    # 92.31% 61.54%
    def numberOfPairs_v2(self, nums: List[int]) -> List[int]:
        return [(sum(Counter(nums).values())-sum([i % 2 != 0 for i in Counter(nums).values()]))//2, sum([i % 2 != 0 for i in Counter(nums).values()])]

    # 92.31% 61.54%
    def numberOfPairs_v3(self, nums: List[int]) -> List[int]:
        return [(sum(nums.values())-sum([i % 2 != 0 for i in nums.values()]))//2 if (nums := Counter(nums)) else 0, sum([i % 2 != 0 for i in nums.values()])]

    # 46.15% 30.77% (61.54% 61.54%)
    def numberOfPairs_v4(self, nums: List[int]) -> List[int]:
        return [(sum(nums)-sum([i % 2 != 0 for i in nums]))//2 if (nums := Counter(nums).values()) else 0, sum([i % 2 != 0 for i in nums])]

    # 46.15% 61.54%
    def numberOfPairs_v5(self, nums: List[int]) -> List[int]:
        return [(sum(nums)-(nums if (nums := sum([i % 2 != 0 for i in nums])) else 0))//2 if (nums := Counter(nums).values()) else 0, nums]

    # 92.31% 61.54%
    def numberOfPairs_v6(self, nums: List[int]) -> List[int]:
        return [(sum(nums)-(nums if (nums := sum([i & 1 for i in nums])) else 0))//2 if (nums := Counter(nums).values()) else 0, nums]

    def numberOfPairs_best_speed(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [sum(v//2 for v in freq.values()), sum(v & 1 for v in freq.values())]
