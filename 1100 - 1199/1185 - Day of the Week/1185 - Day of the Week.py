class Solution:
    def dayOfTheWeek(
            self, day: int, month: int, year: int) -> str:  # 82.62%  55.01%
        import datetime
        out = datetime.datetime(year, month, day)
        weekdays = [
            'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday'
        ]
        return weekdays[out.weekday()]

    def dayOfTheWeek_best_speed(self, day: int, month: int, year: int) -> str:
        res = [
            'Friday', 'Saturday', 'Sunday',
            'Monday', 'Tuesday', 'Wednesday', 'Thursday'
        ]
        days = -1
        for y in range(1971, year):
            if self.isLeapYear(y):
                days += 366
            else:
                days += 365
        for m in range(1, month):
            if m == 2:
                if self.isLeapYear(year):
                    days += 29
                else:
                    days += 28
            elif m in [1, 3, 5, 7, 8, 10, 12]:
                days += 31
            else:
                days += 30
        days += day
        return res[days % 7]

    def isLeapYear(self, year):
        if year % 400 == 0:
            return True
        if year % 4 == 0 and year % 100 != 0:
            return True
        return False

    def dayOfTheWeek_best_memory(self, day: int, month: int, year: int) -> str:
        ans = datetime.date(year, month, day).strftime('%A')
        return ans
