class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:  # 24.75% 58.75%
        out = []
        for i in range(2, n+1):
            new = []
            for j in range(1, i+1):
                if j == 1 or j % i and i % j and math.gcd(i, j) == 1:
                    new.append(f'{j}/{i}')
            out.extend(new)
        return out

    def simplifiedFractions_no_gcd(self, n: int) -> List[str]:  # 73.93% 8.25%
        out = []
        seen = set()
        for i in range(2, n+1):
            new = []
            for j in range(1, i):
                if j/i not in seen:
                    new.append(f'{j}/{i}')
                    seen.add(j/i)
            out.extend(new)
        return out

    def simplifiedFractions_best_speed(self, n: int) -> List[str]:
        memo = []
        for i in range(1, n + 1):
            fractions = []
            for j in range(1, i):
                if gcd(j, i) != 1:
                    continue
                fractions.append(f"{j}/{i}")
            memo.append(fractions)
        result = []
        for f in memo:
            result += f
        return result

    def simplifiedFractions_4th_best_speed(self, n: int) -> List[str]:
        if n == 1:
            return []
        X = self.simplifiedFractions(n - 1)
        for m in range(1, n):
            x, y = m, n
            while x:
                y, x = x, y % x
            if y == 1:
                X.append(f'{m}/{n}')
        return X

    def simplifiedFractions_best_memory(self, n: int) -> List[str]:
        def simplify(numerator:int, denominator: int) -> Tuple[int, int]:
            for i in range(2, numerator + 1):
                q1, r1 = divmod(numerator, i)
                q2, r2 = divmod(denominator, i)
                if r1 == 0 and r2 == 0:
                    return simplify(q1, q2)
            return numerator, denominator

        ret = set()
        for denominator in range(1, n + 1):
            for numerator in range(1, denominator):
                n, d = simplify(numerator, denominator)
                ret.add(f'{n}/{d}')
        return ret
