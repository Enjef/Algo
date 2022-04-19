class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:  # 73.78% 70.00%
        def check(val):
            res = 1
            prev = position[0]
            for i in range(1, n):
                if position[i]-prev >= val:
                    res += 1
                    prev = position[i]
            return res

        position.sort()
        n = len(position)
        left, right = 0, position[-1]-position[0]
        while left <= right:
            mid = left + (right-left)//2
            if check(mid) >= m:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def maxDistance_best_speed(self, position: List[int], m: int) -> int:
        position.sort()
        lo, hi, ans = 1, (max(position) - min(position))//(m-1)+1, 0
        while lo < hi:
            mid, cnt, pre = (lo+hi)//2, 1, position[0]
            for p in position[1:]:
                if p - pre >= mid:
                    cnt += 1
                    pre = p
                    if cnt > m:
                        break
            if cnt >= m:
                ans = max(ans,mid)
                lo = mid + 1
            else:
                hi = mid
        return ans

    def maxDistance_best_memory(self, position: List[int], m: int) -> int:
        position = sorted(position)
        low = 1
        high = 10 ** 9
        ans = -1
        while(low <= high):
            mid = low + (high - low)//2
            mn = position[0]
            count = 1
            for i in range(1, len(position)):
                if(position[i] - mn >= mid):
                    mn = position[i]
                    count += 1
            if(count < m):
                high = mid-1
            else:
                ans = max(ans, mid)
                low = mid +1
        return ans
