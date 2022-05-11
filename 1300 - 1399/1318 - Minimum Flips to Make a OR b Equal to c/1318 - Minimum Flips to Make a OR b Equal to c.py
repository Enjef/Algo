class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:  # 90.91% 25.57%
        a, b, c = str(bin(a))[2:], str(bin(b))[2:], str(bin(c))[2:]
        len_max = max(len(a), len(b), len(c))
        a, b, c = a.zfill(len_max), b.zfill(len_max), c.zfill(len_max)
        diff = 0
        for i in range(len_max):
            if c[i] == '0':
                if a[i] != c[i]:
                    diff += 1
                if b[i] != c[i]:
                    diff += 1
            else:
                if a[i] != c[i] and b[i] != c[i]:
                    diff += 1
        return diff

    def minFlips_best_speed(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            if c & (1 << i) == 0:
                if a & (1 << i) and b & (1 << i):
                    ans += 2
                elif a & (1 << i) or b & (1 << i):
                    ans += 1
            elif c & (1 << i):
                if a & (1 << i) == 0 and b & (1 << i) == 0:
                    ans += 1
        return ans

    def minFlips_2nd_best_speed(self, a: int, b: int, c: int) -> int:
        flip = 0
        while a or b or c:
            lsb_a = a & 1
            lsb_b = b & 1
            lsb_c = c & 1
            if lsb_c == 1:
                flip += lsb_a == lsb_b == 0
            else:
                flip += lsb_a + lsb_b
            a >>= 1
            b >>= 1
            c >>= 1
        return flip

    def minFlips_3d_best_speed(self, a: int, b: int, c: int) -> int:
        res = 0
        temp = (a | b) ^ c
        temp1 = a & b & temp
        while temp:
            if temp & 1:
                res += 1
            if temp1 & 1:
                res += 1
            temp >>= 1
            temp1 >>= 1
        return res
