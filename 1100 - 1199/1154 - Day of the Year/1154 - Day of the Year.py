class Solution:
    def dayOfYear(self, date: str) -> int:  # 5.53% 77.55%
        year, month, day = map(int, date.split('-'))
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100)
        prefix = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        return day + prefix[month-1] + (leap and month > 2)
