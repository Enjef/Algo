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

    def minEatingSpeed_best_speed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        L = total//h
        R = 1 + total//max(h-len(piles), 1)
        while L < R:
            M = (L+R) // 2
            if M == 0:
                return 1
            curr = 0
            for p in piles:
                curr += math.ceil(p/M)
            if curr > h:
                L = M + 1
            else:
                R = M
        return L

    def minEatingSpeed_2nd_best_speed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        sumVal = sum(piles)
        maxVal = max(piles)
        average = sumVal//h
        left, right = max(average, 1), (sumVal)//(h-len(piles)) + 1
        while left < right:
            mid = (left + right)//2
            totalTime = sum([int(x/mid) + int(x % mid > 0) for x in piles])
            if totalTime <= h:
                right = mid
            else:
                left = mid + 1
        return left

    def minEatingSpeed_3d_best_speed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        s = sum(piles)
        l, r = (s - 1) // h + 1, (s - 1) // (h - len(piles)) + 1

        def doable(cap):
            return sum([(x - 1)//cap + 1 for x in piles]) <= h

        while l < r:
            m = (l + r) // 2
            if doable(m):
                r = m
            else:
                l = m + 1
        return l
