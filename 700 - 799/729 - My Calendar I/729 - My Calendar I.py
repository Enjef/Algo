class MyCalendar:
    def __init__(self):  # 5.04% 93.24%
        self.events = []

    def _insert(self, start, end, index=0):
        self.events.insert(index, (end, -1))
        self.events.insert(index, (start, 1))
        return
        
    def book(self, start: int, end: int) -> bool:
        if not self.events:
            self._insert(start, end)
            return True
        cur = 0
        for i, (_, event) in enumerate(self.events):
            cur += event
            if i == 0 and end <= self.events[0][0]:
                self._insert(start, end, 0)
                return True
            if i == len(self.events)-1 and start >= self.events[-1][0]:
                self._insert(start, end, i+1)
                return True
            if (
                not cur and
                self.events[i][0] <= start and self.events[i+1][0] >= end):
                    self._insert(start, end, i+1)
                    return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


class MyCalendar_best_speed:
    def __init__(self):
        self._start = []
        self._end = []

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_right(self._end, start)
        if i == len(self._start) or self._start[i] >=end:
            self._start.insert(i, start)
            self._end.insert(i, end)
            return True
        return False


class MyCalendar_best_memory:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        if (self.calendar) == 0:
            self.calendar.append([start,end])
            return True
        else:
            for x in self.calendar:
                if (
                    (start >= x[0] and start < x[1]) or
                    (end > x[0] and end < x[1]) or
                    (start < x[0] and end >= x[1])):
                        return False
            self.calendar.append([start,end])
            return True
