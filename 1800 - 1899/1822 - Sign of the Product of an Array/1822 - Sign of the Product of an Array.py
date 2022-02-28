class Solution(object):
    def arraySign(self, nums):
        count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                count += 1
        if count % 2 == 0:
            return 1
        return -1

    def top_one(self, nums):
        total = 1

        if 0 in nums:
            return 0

        for x in nums:
            if x < 0:
                total *= -1
        return total

    def arraySign_best_speed(self, nums: list[int]) -> int:
        ans = 1
        for n in nums:
            if n== 0:
                return 0
            if n < 0:
                ans*= -1
        return ans  

    def arraySign_2nd_best_speed(self, nums: List[int]) -> int:
        neg_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            if nums[i] < 0:
                neg_count += 1
        
        if neg_count % 2 == 0:
            return 1
        else: 
            return -1

    def arraySign_best_memory(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            sign = sign*(-1) if num < 0 else sign
        return sign
