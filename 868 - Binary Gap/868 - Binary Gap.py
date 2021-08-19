class Solution:
    def binaryGap(self, n: int) -> int:  # 59.76% 46.28%
        n_max = 0
        if n == 1:
            return n_max
        last = 0
        str_n = str(bin(n))[2:]
        for i in range(len(str_n)):
            if str_n[i] == '1':
                n_max = max(n_max, i-last)
                last = i
        return n_max

    def binaryGap_best(self, n: int) -> int:
        if(bin(n).count('1')) == 1:
            return 0
        c = 0
        x = bin(n)[2:]
        for i in range(len(x)):
            if(x[i] == '1'):
                j = i + 1
                while j < len(x):
                    if(x[j] == '1'):
                        c = max(j-i, c)
                        break
                    j += 1
        return c
