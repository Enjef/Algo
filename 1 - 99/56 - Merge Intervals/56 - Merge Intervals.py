class Solution:
    def merge(
            self,
            intervals: List[List[int]]) -> List[List[int]]:  # 92.50% 56.13%
        intervals.sort()
        out = []
        cur = intervals[0]
        for interval in intervals[1:]:
            if cur[1] >= interval[0]:
                cur[1] = max(cur[1], interval[1])
            else:
                out.append(cur)
                cur = interval
        out.append(cur)
        return out

    def merge_best_speed(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        result_intervals = []
        current_start = intervals[0][0]
        current_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > current_end:
                result_intervals.append([current_start, current_end])
                current_start, current_end = intervals[i][0], intervals[i][1]
            else:
                current_end = max(current_end, intervals[i][1])
        result_intervals.append([current_start, current_end])
        return result_intervals

    def merge_3d_memory(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        n = len(intervals)
        i = 1
        while i < n:
            if intervals[i-1][1] >= intervals[i][0]:
                if intervals[i-1][1] < intervals[i][1]:
                    intervals[i-1][1] = intervals[i][1]
                intervals.pop(i)
                n -= 1
            else:
                i += 1
        return intervals
