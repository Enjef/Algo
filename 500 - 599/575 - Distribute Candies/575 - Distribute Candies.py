class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        half = len(candyType) / 2
        c_set = set(candyType)
        if len(c_set) >= half:
            return half
        return len(c_set)
