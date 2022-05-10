class Solution:
    def removeCoveredIntervals(
            self, intervals: List[List[int]]) -> int:  # 35.70% 98.44%
        total = len(intervals)
        for idx, (a, b) in enumerate(intervals):
            for idy, (c, d) in enumerate(intervals):
                if idx != idy and c <= a and b <= d:
                    total -= 1
                    break
        return total

    def removeCoveredIntervals_best_speed(self, intervals):
        intervals.sort()
        cur = intervals[0]
        count = 0
        for interval in intervals[1:]:
            if cur[0] >= interval[0] and cur[1] <= interval[1]:
                cur = interval
                count += 1
            elif cur[0] <= interval[0] and cur[1] >= interval[1]:
                count += 1
            else:
                cur = interval
        return len(intervals) - count

    def removeCoveredIntervals_2nd_best_speed(
            self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        prev_end = 0
        for _, end in intervals:
            if end > prev_end:
                count += 1
                prev_end = end
        return count

    def removeCoveredIntervals_best_memory(self, intervals):
        intervals.sort()
        prime, i = intervals[0], 1
        while i < len(intervals):
            if intervals[i][0] <= prime[0] and intervals[i][1] >= prime[1]:
                intervals.remove(prime)
                i -= 1
            elif intervals[i][0] >= prime[0] and intervals[i][1] <= prime[1]:
                intervals.pop(i)
                i -= 1
            prime = intervals[i]
            i += 1
        return len(intervals)
