class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count.pop(num)
        return count.keys()[0]
