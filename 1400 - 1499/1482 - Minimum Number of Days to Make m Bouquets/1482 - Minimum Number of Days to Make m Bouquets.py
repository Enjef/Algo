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

    def minDays_best_speed(self, bloomDay: List[int], M: int, k: int) -> int:
        N = len(bloomDay)
        if N < M * k:
            return -1
        if N == M * k:
            return max(bloomDay)
        
        q = deque()
        ci, cv = (0, 0)
        for i, b in enumerate(bloomDay):
            if b >= cv:
                q.clear()
                ci, cv = i, b
            else:
                while q and q[-1][1] <= b:
                    q.pop()
                q.append((i, b))
            if ci + k <= i:
                ci, cv = q.popleft()
            bloomDay[i] = cv
        
        bloomDay = bloomDay[k-1:] + [1 << 32]*(k-1)
        days = sorted(set(bloomDay))
        
        def doable(day):
            count = 0
            i = 0
            while i < N and count < M:
                if bloomDay[i] <= day:
                    count += 1
                    i += k
                else:
                    i += 1
            return count == M
        
        lo, hi = 0, len(days)
        while lo < hi:
            mid = (lo + hi) // 2
            if doable(days[mid]):
                hi = mid
            else:
                lo = mid + 1
        return days[lo]


class Solution_best_memory:
    def bloom(self, bloomDay, m, k, x):
        ans = 0
        flag = 0
        for i in bloomDay:
            if i <= x:
                flag += 1
                if (flag == k):
                    ans += 1
                    flag = 0
            else:
                flag = 0
        if (ans >= m):
            return True
        else:
            return False
        
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = min(bloomDay)
        r = max(bloomDay)+1
        while(l < r):
            mid = (l+r)//2
            if (self.bloom(bloomDay,m,k,mid)):
                r = mid
            else:
                l = mid + 1
        if (l == max(bloomDay)+1):
            return -1
        else:
            return l
