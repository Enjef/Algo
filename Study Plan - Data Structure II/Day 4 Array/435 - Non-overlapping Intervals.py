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
