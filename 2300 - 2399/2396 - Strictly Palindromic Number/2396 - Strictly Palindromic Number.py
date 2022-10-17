class Solution:
    # 99.76% 59.60%
    def isStrictlyPalindromic(self, n: int) -> bool:
        def helper(num, base):
            if num == 0:
                return '0'
            dig = []
            while num:
                num, r = divmod(num, base)
                dig.append(str(r))
            return ''.join(reversed(dig))

        b = 2
        while b < n:
            cur = helper(n, b)
            if not cur == cur[::-1]:
                return False
            b += 1
        return True

    def isStrictlyPalindromic_best_speed(self, n: int) -> bool:
        N = n
        N5 = n
        N6 = n
        N7 = n
        N8 = n
        N9 = n
        N10 = n

        base2 = str(bin(n))[2:]
        if base2 != base2[::-1]:
            return False

        base3 = ''
        while n > 0:
            rem = n % 3
            base3 += str(rem)
            n //= 3
        base3 = base3[::-1]

        base4 = ''
        while N > 0:
            rem = N % 4
            base4 += str(rem)
            N //= 3
        base4 = base4[::-1]

        base5 = ''
        while N5 > 0:
            rem = N5 % 5
            base5 += str(rem)
            N5 //= 5
        base5 = base5[::-1]

        base6 = ''
        while N6 > 0:
            rem = N6 % 6
            base6 += str(rem)
            N6 //= 5
        base6 = base6[::-1]

        base7 = ''
        while N7 > 0:
            rem = N7 % 7
            base7 += str(rem)
            N7 //= 7
        base7 = base7[::-1]

        base8 = ''
        while N8 > 0:
            rem = N8 % 8
            base8 += str(rem)
            N8 //= 8
        base8 = base8[::-1]

        base9 = ''
        while N9 > 0:
            rem = N9 % 9
            base9 += str(rem)
            N9 //= 9
        base9 = base9[::-1]

        listx = [base2, base3, base4, base5, base6, base7, base8, base9]

        if N10 > 9:
            N10 = 9

        for i in range(N10-1):
            if listx[i] != listx[i][::-1]:
                return False
        return True

    def isStrictlyPalindromic_2nd_best_speed(self, n: int) -> bool:
        return False

    def isStrictlyPalindromic_3d_best_speed(self, n: int) -> bool:
        for i in range(2, n-2+1):
            t = n
            s = ''
            while t > 0:
                s = s+str((t % i))
                t = t//i
            if s != s[::-1]:
                return False
        return True

    def isStrictlyPalindromic_5th_best_speed(self, n: int) -> bool:
        for b in range(2, n - 1):
            N, m = [], n
            while m:
                N.append(m % b)
                m //= b
            i, j = 0, len(N) - 1
            while i < j and N[i] == N[j]:
                i += 1
                j -= 1
            if i < j:
                return False
        return True
