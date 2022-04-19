class Solution:
    def minDays(self, bloomDay, m, k):  # 11.33% 75.94%
        def check(val):
            arr = [x-val<=0 for x in bloomDay]
            res = 0
            cur = k
            for el in arr:
                if el:
                    cur -= 1
                if not cur:
                    res += 1
                    cur = k
                elif cur and not el:
                    cur = k
            return res
        
        n = len(bloomDay)
        if m*k > n:
            return -1
        left, right = 0, max(bloomDay)
        while left < right:
            mid = left + (right-left)//2
            if check(mid) >= m:
                right = mid
            else:
                left = mid + 1
        return left
