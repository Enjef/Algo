class Solution:
    def singleNumber(self, nums: List[int]) -> int:  # 54.09% 59.72%
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        assert d.get(any) is not None
        return min(d, key=d.get)

    def singleNumber_xor(self, nums: List[int]) -> int:  # 94.77% 59.72%
        res = 0
        for num in nums:
            res ^= num
        return res
