class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool: # 86.21% 32.02%
        def breaker(first, second):
            for i in range(len(first)):
                if first[i] < second[i]:
                    return False
            return True

        s1 = sorted(s1)
        s2 = sorted(s2)
        return breaker(s1, s2) or breaker(s2, s1)      

    def checkIfCanBreak_best_speed(self, s1: str, s2: str) -> bool:
        a, b = True, True
        d = 0
        for c in ascii_lowercase:
            d += s1.count(c) - s2.count(c)
            if d > 0:
                a = False
            elif d < 0:
                b = False
            if not (a or b): return False
        return True

    def checkIfCanBreak_2nd_best_speed(self, s1: str, s2: str) -> bool:
        def chk(c1, c2):
            s = 0
            for k in 'abcdefghijklmnopqrstuvwxyz':
                s += c1[k] - c2[k]
                if s < 0:
                    return False
            return True
        c1, c2 = Counter(s1), Counter(s2)
        return chk(c1, c2) | chk(c2, c1)

    def checkIfCanBreak_version_78_56(self, s1: str, s2: str) -> bool:
        lst1, lst2 = sorted(s1), sorted(s2)
        return (all(a >= b for a, b in zip(lst1, lst2)) or
                all(a <= b for a, b in zip(lst1, lst2)))

class Solution_best_memory:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        return self.can_break(s1, s2) or self.can_break(s2, s1)
    
    def can_break(self, s1, s2):
        count = [0] * 26
        for char in s1:
            count[ord(char) - ord('a')] += 1
        for char in s2:
            count[ord(char) - ord('a')] -= 1
        diff = 0
        for num in count:
            diff += num
            if diff < 0: return False
        return True
