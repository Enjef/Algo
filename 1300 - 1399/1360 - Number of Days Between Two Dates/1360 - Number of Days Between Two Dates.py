from datetime import date


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = list(map(int, date1.split('-')))
        date2 = list(map(int, date2.split('-')))
        date1 = date(date1[0], date1[1], date1[2])
        date2 = date(date2[0], date2[1], date2[2])
        delta = date1 - date2
        return(abs(delta.days))

    def daysBetweenDates_best_speed(self, date1: str, date2: str) -> int:
        return abs((datetime.datetime.strptime(date2, "%Y-%m-%d").date() - datetime.datetime.strptime(date1, "%Y-%m-%d").date()).days)

    def daysBetweenDates_2nd_best_speed(self, date1: str, date2: str) -> int:
        return abs(date.fromisoformat(date1) - date.fromisoformat(date2)).days

    def daysBetweenDates_best_memory(self, date1: str, date2: str) -> int:
        def f(date):
            y, m, d = map(int, date.split('-'))
            if m < 3:
                m += 12
                y -= 1
            return 365 * y + y // 4 + y // 400 - y // 100 + d + (153 * m + 8) // 5

        return abs(f(date1) - f(date2))
