class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:  # 54.99% 9.33%
        out = 0
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        for subset in result:
            temp = 0
            for el in subset:
                temp ^= el
            out += temp
        return out
