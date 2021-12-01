class Solution:
    def eraseOverlapIntervals(
            self,
            intervals: List[List[int]]) -> int:  # 35.13% 8.70%
        erase = 0
        intervals.sort()
        print(intervals)
        cur = float('-inf')
        for interval in intervals:
            if interval[0] >= cur:
                cur = interval[1]
            else:
                erase += 1
                cur = min(cur, interval[1])
        return erase

    def eraseOverlapIntervals_3d_best_speed(
            self,
            intervals: List[List[int]]) -> int:
        end, cnt = float('-inf'),0
        for s, e in sorted(intervals, key = lambda x: x[1]):
            if s >= end:
                end = e
            else:
                cnt+=1
        return cnt

    def eraseOverlapIntervals_best_memory(
            self,
            intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda l: l[0])
        prev = 0
        i = 1
        while i < len(intervals):
            if intervals[prev][1] > intervals[i][0]:
                if intervals[prev][1] > intervals[i][1]:
                    intervals.pop(prev)
                else:
                    intervals.pop(i)
                count += 1
                continue
            else:
                prev = i
            i += 1
        return count
