class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  # 91.56% 78.82%
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right-left)//2
            if sum([ceil(pile/mid) for pile in piles]) > h:
                left = mid + 1
            else:
                right = mid
        return left
