class Solution:
    def isHappy(self, n: int) -> bool:  # 96.28% 16.24%
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
