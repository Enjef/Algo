class Solution(object):
    def distributeCandies(self, candyType):  # 92.95% 87.18%
        """
        :type candyType: List[int]
        :rtype: int
        """
        half = len(candyType) / 2
        c_set = set(candyType)
        if len(c_set) >= half:
            return half
        return len(c_set)

    def distributeCandies_mock(
            self,
            candyType: List[int]) -> int:  # 32.09% 65.77%
        return min(len(candyType)//2, len(set(candyType)))
