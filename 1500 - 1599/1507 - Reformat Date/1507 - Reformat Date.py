class Solution:
    def reformatDate(self, date: str) -> str:  # 65.11% 90.06%
        month_map = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12',
        }
        day, month, year = date.split()
        day = ''.join([x for x in day if x.isdigit()])
        if len(day) == 1:
            day = ''.join(['0', day])
        return '-'.join([year, month_map[month], day])

    def reformatDate_best_speed(self, date: str) -> str:
        months_to_nums = {
            'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
            'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
            'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
        }
        day, month_name, year = date.split()
        day = day[:-2].zfill(2)
        month = str(months_to_nums[month_name]).zfill(2)
        year = year
        return '{}-{}-{}'.format(year, month, day)

    def reformatDate_best_memory(self, date: str) -> str:
        parts = date.split()
        day = int(parts[0][:-2])
        month = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(parts[1]) + 1
        year = int(parts[2])
        return '{:04d}-{:02d}-{:02d}'.format(year, month, day)
