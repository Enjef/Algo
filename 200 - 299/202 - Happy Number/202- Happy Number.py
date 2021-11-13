class Solution:
    def isHappy(self, n: int) -> bool:
        if n in [1, 7]:
            return True
        if n in [0, 2, 3, 4, 5, 6, 8, 9]:
            return False
        sum = 0
        for num in str(n):
            sum += int(num)*int(num)
        return self.isHappy(sum)

    def isHappy_algo_day_21(self, n: int) -> bool:  # 96.28% 16.24%
        mem = set([n])
        while n not in [1, 7]:
            new = []
            for i in range(1, len(str(n))+1):
                new.append(n % 10)
                n //= 10
            n = sum([x*x for x in new])
            if n in mem:
                return False
            mem.add(n)
        return True

    def isHappy_best_speed(self, n: int) -> bool:
        num_set = set()
        while n != 1:
            if n in num_set:
                return False
            num_set.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return True
