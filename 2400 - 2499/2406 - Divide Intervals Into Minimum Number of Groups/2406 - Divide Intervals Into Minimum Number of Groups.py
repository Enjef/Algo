class Solution:
    # 32.43% 42.49% (31.98% 54.36%)
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.extend([(start, 1), (end+1, -1)])
        events.sort()
        cur = 0
        res = 1
        for time, event in events:
            cur += event
            res = max(res, cur)
        return res

    def minGroups_best_speed(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        start = sorted(start)
        end = sorted(end)
        mg, i, j = 1, 1, 0
        while i < len(start):
            if end[j] >= start[i]:
                mg += 1
                i += 1
            else:
                i += 1
                j += 1
        return mg

    def minGroups_3d_best_speed(self, intervals: List[List[int]]) -> int:
        d = defaultdict(int)
        for start, end in intervals:
            d[start] += 1
            d[end+1] -= 1
        return max(accumulate([d[n] for n in sorted(d.keys())]))

    def minGroups_5th_best_speed(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        pq = [intervals[0][1]]
        for s, e in intervals[1:]:
            if s <= pq[0]:
                heapq.heappush(pq, e)
            else:
                heapq.heappop(pq)
                heapq.heappush(pq, e)
        return len(pq)

    def minGroups_best_memory(self, intervals: List[List[int]]) -> int:
        import heapq
        intervals = sorted(intervals, key=lambda ele: (ele[0], ele[1]))
        q = []
        for i in range(len(intervals)):
            if len(q) > 0 and q[0] < intervals[i][0]:
                heapq.heappop(q)
            heapq.heappush(q, intervals[i][1])
        return len(q)
