from typing import List


# 87.77% 44.60%
class ATM:

    def __init__(self):
        self.banknotes = [0]*5
        self.value = dict([(i, val)
                          for i, val in enumerate([20, 50, 100, 200, 500])])

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, banknote in enumerate(banknotesCount):
            self.banknotes[i] += banknote

    def withdraw(self, amount: int) -> List[int]:
        test = [0]*5
        for i in range(4, -1, -1):
            if not self.banknotes[i] or self.value[i] > amount:
                continue
            if test[i] < self.banknotes[i] and self.value[i] > amount:
                return [-1]
            cur = min(amount//self.value[i], self.banknotes[i])
            test[i] += cur
            amount -= cur*self.value[i]
            if not amount:
                break
        if amount:
            return [-1]
        self.deposit([-x for x in test])
        return test


class ATM_best_speed:
    def __init__(self) -> None:
        self.p20: int = 0
        self.p50: int = 0
        self.p100: int = 0
        self.p200: int = 0
        self.p500: int = 0

    def deposit(self, banknotesCount: List[int]) -> None:
        self.p20 += banknotesCount[0]
        self.p50 += banknotesCount[1]
        self.p100 += banknotesCount[2]
        self.p200 += banknotesCount[3]
        self.p500 += banknotesCount[4]

    def withdraw(self, amount: int) -> List[int]:
        mini: int
        counts: List[int] = [0, 0, 0, 0, 0]
        if self.p500 and amount >= 500:
            mini = min(self.p500, amount // 500)
            counts[4] = mini
            amount -= mini * 500

        if self.p200 and amount >= 200:
            mini = min(self.p200, amount // 200)
            counts[3] = mini
            amount -= mini * 200

        if self.p100 and amount >= 100:
            mini = min(self.p100, amount // 100)
            counts[2] = mini
            amount -= mini * 100

        if self.p50 and amount >= 50:
            mini = min(self.p50, amount // 50)
            counts[1] = mini
            amount -= mini * 50

        if self.p20 and amount >= 20:
            mini = min(self.p20, amount // 20)
            counts[0] = mini
            amount -= mini * 20

        if amount != 0:
            return [-1]
        else:
            self.p500 -= counts[4]
            self.p200 -= counts[3]
            self.p100 -= counts[2]
            self.p50 -= counts[1]
            self.p20 -= counts[0]
            return counts


class ATM_3d_best_speed:
    def __init__(self):
        self.banknotes = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.banknotes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        money = [20, 50, 100, 200, 500]
        copy_bank = self.banknotes.copy()
        ans = [0] * 5
        for i in range(4, -1, -1):
            taken = amount // money[i]
            taken = min(self.banknotes[i], taken)
            amount -= (taken * money[i])
            ans[i] = taken
            self.banknotes[i] -= taken
        if amount == 0:
            return ans
        self.banknotes = copy_bank
        return [-1]


class ATM_best_memory:
    def __init__(self):
        self.notes, self.amts = [0, 0, 0, 0, 0], [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        self.notes = [i+j for i, j in zip(self.notes, banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        used = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            if amount >= self.amts[i]:
                req, have = amount//self.amts[i], self.notes[i]
                amount, used[i] = amount - min(req, have)*self.amts[i], used[i] + min(req, have)
        if not amount:
            self.notes = [i-j for i, j in zip(self.notes, used)]
            return used
        return [-1]
