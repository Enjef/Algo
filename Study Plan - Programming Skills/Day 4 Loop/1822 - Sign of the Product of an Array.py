class Solution:
    def arraySign(self, nums: List[int]) -> int:  # 5.49% 71.32%
        count_negative = 0
        for num in nums:
            if num < 0:
                count_negative += 1
            if not num:
                return 0
        return -1 if count_negative % 2 else 1

    def arraySign_v2(self, nums: List[int]) -> int:  # 91.35% 71.32%
        res = 1
        for num in nums:
            res *= num
        if not res:
            return 0
        return -1 if res < 0 else 1
