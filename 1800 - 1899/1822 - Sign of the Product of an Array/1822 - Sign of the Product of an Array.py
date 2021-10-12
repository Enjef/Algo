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
