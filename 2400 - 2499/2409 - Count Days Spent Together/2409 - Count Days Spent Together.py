class Solution:
    # 74.41% 18.72% (23.67% 59.76%)
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        pref = [0]
        for day in days:
            pref.append(pref[-1]+day)

        alice_month, alice_day = map(int, arriveAlice.split('-'))
        alice_month2, alice_day2 = map(int, leaveAlice.split('-'))

        bob_month, bob_day = map(int, arriveBob.split('-'))
        bob_month2, bob_day2 = map(int, leaveBob.split('-'))

        alice = set(range(pref[alice_month-1]+alice_day,
                    pref[alice_month2-1]+alice_day2+1))
        bob = set(range(pref[bob_month-1]+bob_day,
                  pref[bob_month2-1]+bob_day2+1))
        return len(alice & bob)

    def countDaysTogether_best_speed(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def month(s):
            if s[0] == '0':
                return int(s[1])
            else:
                return int(s)

        def date(s):
            if s[0] == '0':
                return int(s[1])
            else:
                return int(s)

        def calcDays(n):
            res = 0
            for i in range(n):
                res += months[i]
            return res

        aliceArr = calcDays(month(arriveAlice[:2])) + date(arriveAlice[3:])
        aliceLea = calcDays(month(leaveAlice[:2])) + date(leaveAlice[3:])

        bobArr = calcDays(month(arriveBob[:2])) + date(arriveBob[3:])
        bobLea = calcDays(month(leaveBob[:2])) + date(leaveBob[3:])

        if aliceArr <= bobArr <= bobLea <= aliceLea:
            return bobLea - bobArr + 1
        elif bobArr <= aliceArr <= aliceLea <= bobLea:
            return aliceLea - aliceArr + 1
        elif aliceArr <= bobArr <= aliceLea:
            return aliceLea - bobArr + 1
        elif bobArr <= aliceArr <= bobLea:
            return bobLea - aliceArr + 1
        return 0

    def countDaysTogether_2nd_best_speed(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        return max(
            min(
                self.get_date(leaveBob),
                self.get_date(leaveAlice)) -
            max(
                self.get_date(arriveAlice),
                self.get_date(arriveBob)) + 1,
            0)

    def get_date(self, date):
        month_day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(date[:2])
        day = int(date[3:])
        return sum(month_day_list[:month]) + day

    def countDaysTogether_best_memory(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        import datetime

        def parse(date):
            mm, dd = map(int, date.split('-'))
            return datetime.date(year=2001, month=mm, day=dd)
        return max((min(parse(leaveAlice), parse(leaveBob))-max(parse(arriveAlice), parse(arriveBob))).days+1, 0)
