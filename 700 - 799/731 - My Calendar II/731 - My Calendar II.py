class MyCalendarTwo: # 10.94% 70.35%
    def __init__(self):
        self.calendar = {}

    def book(self, start: int, end: int) -> bool:
        self.calendar[start] = self.calendar.get(start, 0) + 1
        self.calendar[end] = self.calendar.get(end, 0) - 1
        check = 0
        for key in sorted(self.calendar):
            check += self.calendar[key]
            if check > 2:
                self.calendar[start] = self.calendar.get(start, 0) - 1
                self.calendar[end] = self.calendar.get(end, 0) + 1
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


import bisect as bi
class MyCalendarTwo_best_speed:
    def __init__(self):
        self.s_points = []
        self.e_points = []

    def book(self, start: int, end: int) -> bool:
        i = bi.bisect_left(self.s_points, start)
        j = bi.bisect_right(self.e_points, start)
        cur_intv = i - j
        if cur_intv > 1: return False
        while i < len(self.s_points) and j < len(self.e_points) and min(self.s_points[i], self.e_points[j]) < end:
            if self.e_points[j] <= self.s_points[i]:
                cur_intv -= 1
                j += 1
            else:
                cur_intv += 1
                i += 1
            if cur_intv > 1: return False
        bi.insort(self.s_points, start)
        bi.insort(self.e_points, end)
        return True


class MyCalendarTwo_2nd_best_speed:
    def __init__(self):
        self.s = []
        self.d = []

    def book(self, start: int, end: int) -> bool:
        di = bisect.bisect_right(self.d, start)
        dj = bisect.bisect_left(self.d, end)
        if di % 2 == 1 or di != dj:
            return False
        si = bisect.bisect_right(self.s, start)
        sj = bisect.bisect_left(self.s, end)
        t = ([start] if si % 2 == 1 else []) + self.s[si: sj] + ([end] if sj % 2 == 1 else [])
        self.d[di: dj] = t
        self.s[sj: sj] = [end]
        self.s[si: si] = [start]
        return True


class MyCalendarTwo_best_memory:
    def __init__(self):
        self.cal = []
        self.double_booking = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.double_booking:
            if start < e and end > s:
                return False
        for s, e in self.cal:
            if start < e and end > s:
                self.double_booking.append((max(start, s), min(end, e)))
        self.cal.append((start, end))
        return True
