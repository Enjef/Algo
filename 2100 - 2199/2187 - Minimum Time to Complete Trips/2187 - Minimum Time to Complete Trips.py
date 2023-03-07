class Solution:
    # 44.75% 42.75% (46.50% 70.25%)
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def time_to_trips(amt):
            total = 0
            for cur in time:
                total += amt // cur
            return total

        left = 0
        right = max(time) * totalTrips
        while left < right:
            mid = (left+right)//2
            if time_to_trips(mid) >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return left


import numpy as np


def get_trips(t_arr, T):
    return np.sum(T // t_arr)


class Solution_best_speed:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        t_arr = np.array(time, dtype=np.int64)
        hi = 1
        lo = 1
        while get_trips(t_arr, hi) < totalTrips:
            lo = hi
            hi *= 2
        while lo < hi:
            mid = (lo + hi) // 2
            if get_trips(t_arr, mid) >= totalTrips:
                hi = mid
            else:
                lo = mid+1

        return hi


class Solution_2nd_best_speed:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        mint = 0
        maxt = totalTrips * min(time)
        print(mint, maxt)
        while mint < maxt:
            print(mint, maxt)
            mid = (mint + maxt) // 2
            if sum([mid // t for t in time]) < totalTrips:
                mint = mid + 1
            else:
                maxt = mid
        return mint


class Solution_best_memory:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        min_time = sys.maxsize
        for t in time:
            min_time = min(min_time, t)
        l, r = 1, min_time * totalTrips
        result = r
        while l <= r:
            mid = l + (r - l) // 2
            trips = 0
            for t in time:
                trips += mid // t
            if trips < totalTrips:
                l = mid + 1
            else:
                result = mid
                r = mid - 1
        return result







