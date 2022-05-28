class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:  # 64.78% 60.53%
        for i in range(1, n):
            if not str(i).count('0') and not str(n-i).count('0'):
                return [i, n-i]

    def getNoZeroIntegers_best_speed(self, n: int) -> List[int]:
        arr = []
        flag = False
        while flag == False:
            a = randint(1, n - 1)
            b = n - a
            if str(a).count('0') == 0 and str(b).count('0') == 0:
                arr.append(a)
                arr.append(b)
                return arr

    def getNoZeroIntegers_2nd_best_speed(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' in str(i):
                continue
            if '0' in str(n-i):
                continue
            return [i, n-i]

    def getNoZeroIntegers_3d_best_speed(self, n: int) -> List[int]:
        while True:
            rando = randint(1, n-1)
            b = n - rando
            if str(b).count('0') != 0 or str(rando).count('0') != 0:
                continue
            return [b, rando]

    def getNoZeroIntegers_best_memory(self, n: int) -> List[int]:
        res = []
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n-i):
                res.append(i)
                res.append(n-i)
                break
        return res
