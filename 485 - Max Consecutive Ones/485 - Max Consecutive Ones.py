class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for i in nums:
            if i == 0:
                if count > max_count:
                    max_count = count
                count = 0
            if i == 1:
                count += 1
        if count > max_count:
            max_count = count
        return max_count
