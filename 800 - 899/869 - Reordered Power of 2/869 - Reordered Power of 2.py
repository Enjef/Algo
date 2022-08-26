class Solution:
    # 72.19% 64.17%
    def reorderedPowerOf2(self, n: int) -> bool:
        valid = {1, 2, 4, 8}
        if n in valid:
            return True
        n_len = len(str(n))
        down, up = int('9'*(n_len-1)), int('1'+'0'*(n_len))
        cur = 2
        while cur <= up:
            if down <= cur <= up:
                valid.add(''.join(sorted(str(cur))))
            cur *= 2
        if ''.join(sorted(str(n))) in valid:
            return True
        return False

    def reorderedPowerOf2_best_speed(self, n: int) -> bool:
        l = sorted(list(str(n)))
        for i in range(30):
            a = 2**i
            b = sorted(list(str(a)))
            if l == b:
                return True
        else:
            return False

    def reorderedPowerOf2_2nd_best_speed(self, n: int) -> bool:
        p2 = set()
        x = 1
        d = len(str(n))
        while True:
            sx = str(x)
            if len(sx) == d:
                srted = sorted(list(sx))
                tpl = tuple(srted)
                p2.add(tpl)
            elif len(sx) > d:
                break
            x *= 2
        srtedn = sorted(list(str(n)))
        tpln = tuple(srtedn)
        return tpln in p2

    def reorderedPowerOf2_best_memory(self, n: int) -> bool:
        ndcnts = [0] * 10
        while n > 0:
            ndcnts[n % 10] += 1
            n = n//10
        ndnum = sum(ndcnts)
        p2 = 1
        for i in range(31):
            tdnum = len(str(p2))
            if tdnum < ndnum:
                p2 = 2*p2
                continue
            if tdnum > ndnum:
                return False
            dcnts = [0] * 10
            x = p2
            while x > 0:
                dcnts[x % 10] += 1
                x = x//10
            matched = True
            for i in range(10):
                if dcnts[i] != ndcnts[i]:
                    matched = False
                    break
            if matched:
                return True
            p2 = 2*p2
        return False

    def reorderedPowerOf2_2nd_best_memory(self, n: int) -> bool:
        for p in itertools.permutations(str(n)):
            if p[0] == '0':
                continue
            if bin(int(''.join(p))).count('1') == 1:
                return True
        return False
