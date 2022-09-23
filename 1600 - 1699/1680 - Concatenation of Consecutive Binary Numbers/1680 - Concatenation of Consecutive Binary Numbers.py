class Solution:
    # 14.17% 7.09%
    def concatenatedBinary(self, n: int) -> int:
        arr = []
        for i in range(1, n+1):
            arr.append(str(bin(i))[2:])
        return int(''.join(arr), 2) % (10**9 + 7)

    # 81.10% 14.17%
    def concatenatedBinary_v2(self, n: int) -> int:
        return int(''.join(bin(i)[2:] for i in range(1, n+1)), 2) % (10**9 + 7)

    def concatenatedBinary_best_speed(self, n):
        def bin_pow(num):
            return [1 << i for i, b in enumerate(bin(num)[:1:-1]) if b == "1"]

        ans, MOD, q = 0, 10**9 + 7, len(bin(n)) - 3
        B = bin_pow((1 << q) - 1) + bin_pow(n - (1 << q) + 1)[::-1]
        C = list(range(1, q+1)) + [q+1]*(len(B) - q)
        D = list(accumulate(
            i*j for i, j in zip(B[::-1], C[::-1])))[::-1][1:] + [0]
        for a, b, c, d in zip(accumulate(B), B, C, D):
            t1 = pow(2, b*c, MOD) - 1
            t2 = pow(pow(2, c, MOD)-1, MOD - 2, MOD)
            ans += t2*((a-b+1+t2)*t1-b)*pow(2, d, MOD)
        return ans % MOD

    def concatenatedBinary_3_best_speed(self, n: int) -> int:
        s = ('{:b}' * n).format(*range(1, n + 1))
        return int(s, 2) % (10 ** 9 + 7)

    def concatenatedBinary_best_memory(self, n: int) -> int:
        ans = 0
        curr = 0
        val = 1
        for i in range(1, n+1):
            if i == val:
                mul = 2 << curr
                curr += 1
                val <<= 1
            ans = (ans*mul + i) % (10**9 + 7)
        return ans

    def concatenatedBinary_2nd_best_memory(self, n: int) -> int:
        MOD = 10**9 + 7
        length = 0
        result = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                length += 1
            result = ((result << length) | i) % MOD
        return result
