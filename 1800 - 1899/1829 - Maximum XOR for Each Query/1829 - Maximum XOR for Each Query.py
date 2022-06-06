class Solution:
    # 24.69% 41.84%
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        out = []
        cur = 2**maximumBit - 1
        for i in range(n):
            cur ^= nums[i]
            out.append(cur)
        return out[::-1]

    def getMaximumXor_best_speed(self, nums: list[int], maximumBit: int) -> list[int]:
        nums = [pow(2, maximumBit)-1]+nums
        return list(accumulate((nums), xor))[1:][::-1]

    def getMaximumXor_2nd_best_speed(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = 2 ** maximumBit - 1
        results = list()
        for num in nums:
            max_val ^= num
            results.append(max_val)

        return results[::-1]

    def getMaximumXor_best_memory(self, nums: List[int], maximumBit: int) -> List[int]:
        result = []
        x = (2**maximumBit)-1
        for i in range(len(nums)):
            nums[i] ^= x
            x = nums[i]
        return nums[::-1]
