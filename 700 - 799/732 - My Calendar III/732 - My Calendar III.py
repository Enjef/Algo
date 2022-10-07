# 80.00% 77.23%
class MyCalendarThree:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> int:
        insort(self.events, (start, 1))
        insort(self.events, (end, -1))
        k = res = 0
        for coord, event in self.events:
            k += event
            res = max(res, k)
        return res


class MyCalendarThree_best_speed:
    def __init__(self):
        self.starts = []
        self.ends = []
        self.k = 0

    def book(self, start: int, end: int) -> int:
        left = bisect.bisect_left(self.ends, start)
        right = bisect.bisect_right(self.starts, end)
        bisect.insort_left(self.starts, start)
        bisect.insort_left(self.ends, end)

        hq = []
        for i in range(left, right + 1):
            while hq and hq[0] <= self.starts[i]:
                hq.pop(0)

            hq.append(self.ends[i])
            self.k = max(self.k, len(hq))

        return self.k


class MyCalendarThree_best_memory:
    def __init__(self):
        self.d_events = collections.defaultdict(int)

    def book(self, start, end):
        self.d_events[start] += 1
        self.d_events[end] -= 1
        max_event = curr_event = 0
        for idx in sorted(self.d_events):
            curr_event += self.d_events[idx]
            max_event = max(max_event, curr_event)
        return max_event


class MyCalendarThree_2nd_best_memory:
    def __init__(self):
        self.start_times = []
        self.end_times = []

    def book(self, start: int, end: int) -> int:
        self.start_times.append(start)
        self.end_times.append(end)
        self.start_times.sort()
        self.end_times.sort()
        count = max_count = 0
        i, j = 0, 0
        while i < len(self.start_times):
            curr_start = self.start_times[i]
            curr_end = self.end_times[j] if j < len(self.end_times) else math.inf
            if curr_start < curr_end:
                count += 1
                max_count = max(max_count, count)
                i += 1
            else:
                count -= 1
                j += 1
        return max_count
